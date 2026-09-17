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
end
