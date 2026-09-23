# frozen_string_literal: true

require 'minitest/autorun'

class AgentInstructionsTest < Minitest::Test
  ROOT = File.expand_path('..', __dir__)

  def test_core_leaves_headroom_below_codex_discovery_limit
    core = File.binread(File.join(ROOT, 'AGENTS.md'))

    assert_operator(core.bytesize, :<=, 16 * 1024,
                    'Move detailed procedures behind explicit routes; never truncate rules')
  end

  def test_every_procedure_is_routed_and_readable
    core = File.read(File.join(ROOT, 'AGENTS.md'), encoding: 'UTF-8')
    routes = core.scan(/\]\((docs\/agent-instructions\/[^)]+\.md)\)/).flatten.uniq
    files = Dir.glob('docs/agent-instructions/*.md', base: ROOT)

    refute_empty(routes, 'The core must explicitly route required procedures')
    assert_equal(files.sort, routes.sort, 'Every procedure needs a direct route')

    routes.each do |path|
      assert(File.file?(File.join(ROOT, path)), "Missing required procedure: #{path}")
      refute_empty(File.read(File.join(ROOT, path), encoding: 'UTF-8').strip,
                   "Empty procedure: #{path}")
    end
  end

  def test_feature_merge_needs_explicit_user_direction
    core = File.read(File.join(ROOT, 'AGENTS.md'))
    git = File.read(File.join(ROOT, 'docs/agent-instructions/git.md'))
    sessions = File.read(File.join(ROOT, 'docs/agent-instructions/sessions.md'))

    assert_match(/Feature content may enter a repository's default branch only after the user/, core)
    assert_match(/direct default-branch pushes.*\n.*pull-request merges/m, git)
    assert_match(/tracking-only coordination commits/, git)
    assert_match(/patch\s+equivalence/, git)
    assert_match(/ready, awaiting merge approval/, sessions)
  end

  def test_review_uses_saved_member_settings_or_catalog_fallback
    core = File.read(File.join(ROOT, 'AGENTS.md'))
    verification = File.read(File.join(ROOT, 'docs/agent-instructions/verification.md'))

    assert_match(/retained reviewers, honor the member's saved model and reasoning effort/, core)
    assert_match(/installed catalog's default development reviewer/, verification)
    assert_match(/including for solo sessions/, verification)
  end
end
