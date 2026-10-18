require '/home/aither/.local/state/dev-workspaces/profile/libexec/workspace-coordination-execution'
root = '/home/aither/workspace/ai/vpsfree.cz'
records = File.join(root, 'work/2026-10-16-session-archive-local-first')
engine = WorkspaceCoordination::Engine.new(state: '/home/aither/.local/state/dev-workspaces', package: '/home/aither/.local/state/dev-workspaces/profile', profile: '/home/aither/.local/state/dev-workspaces/profile', workspace: root, entry: {'root' => root, 'name' => 'vpsfree-cz'})
ranges = {
  'workspace' => ['90f878616573e3f16b444e3a28709293c0f552d2', 'abdeefc472bb96da2ca15f3aee2599987d10ab6e'],
  'vpsfree-cz-configuration' => ['0bc45716f64e095dc38281537d24d157c7023826', 'b066d2514892364702461d3e1427c059895846f3']
}
results = {}
ranges.each do |name, (base, head)|
  path = File.join(root, 'worktrees/2026-10-16-session-archive-local-first', name)
  target = engine.capture('git', '-C', path, 'rev-parse', 'origin/master').strip
  final = engine.capture('git', '-C', path, 'rev-parse', 'HEAD').strip
  results[name] = if name == 'vpsfree-cz-configuration'
    parameters = JSON.parse(File.read('/home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/integration.json')).fetch('refreshes').fetch(name).fetch('parameters')
    payload = {'schema' => 1, 'action' => 'verify', 'source' => path, 'from' => head, 'to' => final, 'parameters' => parameters, 'heads' => {'dev-workspace' => '598336522fbb490e7606670d5fdb504e66c607ec'}}
    command = '/nix/store/c8jzzj38an84hp56kvwqxniw2h9jd72n-vpsfree-dev-workspace-tools-0.1.0/bin/workspace-integration-recipe'
    result = JSON.parse(engine.capture(command, input: JSON.generate(payload)))
    raise 'generated pin was not proved' unless result['verified'] == true && result['head'] == final
    result.fetch('proof').merge('recipe' => 'workspace-pins')
  else
    WorkspaceCoordination::Certification.new(engine).prove(path, from_base: base, from: head, to_base: target, to: final)
  end
  File.write(File.join(records, "premerge-#{name}-range-diff.txt"), engine.capture('git', '-C', path, 'range-diff', '--no-color', "#{base}..#{head}", "#{target}..#{final}"))
end
File.write(File.join(records, 'premerge-equivalence-proofs.json'), JSON.pretty_generate(results) + "\n")
puts results.transform_values { |proof| proof.slice('relation', 'from', 'to', 'tree', 'reconstructedTree') }.to_json
