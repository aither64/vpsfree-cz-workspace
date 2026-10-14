require 'json'
require 'digest'
require 'open3'
require '/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source/cluster/lib/kb_runtime'
root='/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14/campaign/state'
state=KbRuntime::State.new(root,'same-slug')
engine=KbRuntime::Engine.new(state: state,software: nil,controller: nil)
state.transaction(create: false,wait: false) do
  state.identity
  launch=engine.launch
  raise 'G14 identity changed' unless launch['instance_id']=='31f2a709-4906-45fe-8224-dec594ce9471' && launch['run_id']=='91c20a6a-948a-447c-aeb1-338b9581a0b4'
  raise 'G14 not completely stopped' unless engine.phase['phase']=='stopped' && engine.gone?(launch)
  engine.verify_tree(state.directory)
  output,error,status=Open3.capture3('python3','finish-g14-pre-reset-private-evidence1.py')
  raise 'private evidence copy failed; no reset selected' unless status.success?
  puts output
end
