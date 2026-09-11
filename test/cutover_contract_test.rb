# frozen_string_literal: true

require 'minitest/autorun'

class CutoverContractTest < Minitest::Test
  SCRIPT = File.expand_path('../bin/aitherdev-workspace-cutover', __dir__)

  def setup
    @source = File.read(SCRIPT)
  end

  def test_script_is_strict_shell
    assert(system('bash', '-n', SCRIPT))
    assert_includes(@source, 'set -Eeuo pipefail')
  end

  def test_initial_inventory_gate_precedes_every_mutation
    prepare = function_body('prepare')
    inventory = prepare.index('assert_exact_authorities "$OLD_AUTHORITY_DIR"')
    validation = prepare.index('"$OLD_PROFILE/bin/dev-session" validate')
    session_contract = prepare.index('assert_session_contract')
    stoppable = prepare.index('assert_stoppable_authorities')
    cluster_inventory = prepare.index('expected_cluster_inventory')
    first_mutation = prepare.index('router_gate_close')
    refute_nil(inventory)
    refute_nil(validation)
    refute_nil(session_contract)
    refute_nil(stoppable)
    refute_nil(cluster_inventory)
    refute_nil(first_mutation)
    [inventory, validation, session_contract, stoppable, cluster_inventory].each do |gate|
      assert_operator(gate, :<, first_mutation)
    end
  end

  def test_forward_mutations_and_exact_sources_are_explicit
    prepare = function_body('prepare')
    assert_includes(prepare, 'assert_exact_workspace_checkout "$reviewed_workspace_commit"')
    assert_includes(prepare, 'assert_exact_clean_checkout "$CONFIGURATION_WORKTREE"')
    assert_includes(prepare, 'assert_exact_clean_checkout "$MIGRATION_SOURCE"')
    assert_includes(prepare, 'assert_exact_clean_checkout "$COMPATIBILITY_WORKTREE"')
    assert_includes(function_body('forward'), '--scope user --workspace-root "$WORKSPACE_ROOT" --yes')
    assert_includes(function_body('assert_exact_workspace_checkout'),
                    "':(exclude)tmp/**'")
    refute_includes(function_body('assert_exact_workspace_checkout'), 'grep -Ev')
  end

  def test_session_classification_uses_tracking_lifecycle_and_has_no_legacy_restart
    contract = function_body('assert_session_contract')
    assert_includes(contract, 'assert_tracking_lifecycle')
    assert_includes(contract, 'assert_manifest_phase')
    assert_includes(contract, 'assert_no_pending_lifecycle')
    refute_includes(@source, 'LEGACY_IDENTITY_SESSIONS')
    refute_match(/^rollback\(\)/, @source)
  end

  def test_forced_stop_is_limited_to_audited_authorities
    body = function_body('force_stop_audited_authorities')
    assert_includes(body, 'for slug in "${AUDITED_AUTHORITIES[@]}"')
    assert_includes(body, "'@vpsfree_dev_session_slug'")
    assert_includes(body, 'VPSFREE_DEV_SESSION_TMUX_IDENTITY')
    refute_includes(body, 'show-environment -t "$session_id" -v')
    refute_includes(body, "jq -er '.tmux_identity // empty'")
    assert_includes(body, 'kill-session -t "$session_id"')
    assert_includes(body, 'if ! tmux -S "$OLD_TMUX_SOCKET" has-session')
    assert_includes(function_body('assert_stoppable_authorities'),
                    'audited tmux session is absent before mutation')
  end

  def test_forward_phases_are_retryable_and_state_is_durable
    prepare = function_body('prepare')
    forward = function_body('forward')
    assert_includes(prepare, 'test "$(current_stage)" = preparing')
    assert_includes(forward, 'test "$stage" = prepared || test "$stage" = forwarding')
    assert_includes(function_body('write_state'),
                    'File.open(ARGV.fetch(0), "r") { |file| file.fsync }')
  end

  def test_router_opens_only_in_accept_after_local_gates
    forward = function_body('forward')
    refute_includes(forward, 'router_gate_open')
    assert_includes(forward, 'assert_router_gated')

    accept = function_body('accept')
    router = accept.index('router_gate_open')
    refute_nil(router)
    assert_operator(accept.index('assert_recreated_session_contract'), :<, router)
    assert_operator(accept.index('assert_no_legacy_process_environments'), :<, router)
    assert_operator(accept.index('credential_inventory new'), :<, router)
  end

  def test_certificate_writer_uses_an_independent_runtime_condition_gate
    stop = function_body('certificate_writer_stop')
    start = function_body('certificate_writer_start')
    assert_includes(stop, 'ConditionPathExists=%s')
    assert_includes(stop, '90-aitherdev-cutover.conf')
    refute_includes(stop, 'systemctl mask --runtime')
    assert_includes(start, '90-aitherdev-cutover.conf')
    assert_includes(start, 'systemctl daemon-reload')
  end

  def test_acceptance_checks_conversation_and_authenticated_tls_continuity
    assert_includes(function_body('assert_recreated_session_contract'), 'recreated manifest and authority thread differ')
    accept = function_body('accept')
    assert_includes(accept, 'assert_authenticated_portal')
    assert_includes(accept, 'router_gate_close')
  end

  def test_archived_authority_is_stopped_but_not_recreated
    assert_includes(@source, 'readonly ARCHIVED_AUTHORITY=2026-09-07-fix-ip-charged-environments')
    assert_includes(array_body('AUDITED_AUTHORITIES'), '2026-09-07-fix-ip-charged-environments')
    refute_includes(array_body('RECREATED_SESSIONS'), '2026-09-07-fix-ip-charged-environments')
    assert_includes(function_body('assert_session_contract'), 'state.md" complete')
  end

  private

  def function_body(name)
    match = @source.match(/^#{Regexp.escape(name)}\(\) \{\n(.*?)^\}\n/m)
    refute_nil(match, "missing #{name} function")
    match[1]
  end

  def array_body(name)
    match = @source.match(/^readonly -a #{Regexp.escape(name)}=\(\n(.*?)^\)\n/m)
    refute_nil(match, "missing #{name} array")
    match[1]
  end
end
