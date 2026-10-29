# History consolidation receipt

Repository: `git@github.com:vpsfreecz/haveapi.git`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-client-formatting-audit/haveapi`.
Branch: `2026-10-29-client-formatting-audit`.
Owner: implementer2, under the lead's exclusive team Git grant.
Recorded after consolidation on 2026-10-30.

## Exact ranges and disposition

- Old reviewed range: `ae46cf27a9afb6558d386c293cec7231dd6c423d..864b80bc177625008ee843e9790564c8e9bc2b27` (10 owned commits).
- Old accepted fixed range: `ae46cf27a9afb6558d386c293cec7231dd6c423d..436332b5cef6b8c852eea02b5d13fc7975cbef49` (11 owned commits).
- New consolidated range: `ae46cf27a9afb6558d386c293cec7231dd6c423d..d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038` (10 owned commits).
- Initial/inherited base is unchanged: `ae46cf27a9afb6558d386c293cec7231dd6c423d`.
- Reviewer0 reported only R1 Important; the lead accepted its prescribed narrow
  fix after direct inspection and focused verification. No other findings remain.
- Folded `436332b5cef6b8c852eea02b5d13fc7975cbef49` into its owning release commit `5d0d81a16377a7fba120bc76ecf23081682f49f1`,
  now `5e871ab42cdb348e43fd02cc46c8c42afd822a56`. Seven preceding commits retain their literal identities.
  The following shared-tooling and Rust commits retain identical patches with
  rewritten parent identities, as independently compared below.
- The accepted R1 patch changes only relative PRETTIER resolution and its focused
  regression in `utils/release/typescript_smoke.rb` and
  `utils/release/spec/typescript_spec.rb`.
- No database migrations; no migration/schema files change in this owned range.
  Existing manifest format 1 and its supported predecessor remain unchanged
  relative to the accepted fixed tree. No release, deployment or external
  consumption occurred for these feature commits.
- No push, default-branch integration, ref deletion or lifecycle action occurred.
  This receipt grants no integration approval and does not remove the inherited
  documentation-redesign baseline dependency.

## Independent final-tree and accepted-delta proofs

Both `436332b5cef6b8c852eea02b5d13fc7975cbef49` and `d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038` resolve to the same tree:

```text
41dd4a998d7f0289a4e45019db1c50afea4bd732
```

`git diff --binary 436332b5cef6b8c852eea02b5d13fc7975cbef49 d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038` is empty, exit 0.
The binary diff from `5d0d81a16377a7fba120bc76ecf23081682f49f1` to `5e871ab42cdb348e43fd02cc46c8c42afd822a56` is byte-for-byte identical
to the accepted R1 diff from `864b80bc177625008ee843e9790564c8e9bc2b27` to `436332b5cef6b8c852eea02b5d13fc7975cbef49`. Both have SHA-256:

```text
0dbc3caa02935317d8e53ce1789e14448cbf9c076e902badfa2b185d03230325
```

All nine unaffected commits compare equal in the complete range-diff. The owning
release commit gains exactly R1, and the separate fix row is absorbed. There
were no source conflicts or manual source resolutions. No source, config or
migration change was introduced by consolidation.

## Preserved local recovery refs

```text
refs/review/2026-10-29-client-formatting-audit/consolidated d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038
refs/review/2026-10-29-client-formatting-audit/fixed-before-consolidation 436332b5cef6b8c852eea02b5d13fc7975cbef49
refs/review/2026-10-29-client-formatting-audit/reviewed-before-consolidation 864b80bc177625008ee843e9790564c8e9bc2b27
```

No existing ref was deleted or overwritten. Recovery refs were created with
zero-old-value guards. The feature ref was updated by ordinary interactive
rebase only; the shared checkout/default branch was untouched.

## Complete resulting series

```text
5aa2de000c5d5e8f63103ce85c576a41d0c9cbc9 clients/js: normalize authored source with Prettier defaults
058e9315c8e348dac376e7eee05dd5456d4b0bfc clients/js: enforce shared Prettier defaults for authored source
26f578cecae02b0d82151f4bc3e00ae3af6835fb ci: cover Ruby tooling inputs in RuboCop triggers
8bd669389aeb087f63c41197e725d1fcba05d556 clients/go: cover formatting failures and canonical output
05082918c71e1571f5dc9005b4d00208901cb49b clients/php: apply canonical source formatting
08e8716de5206e36c7871d2d8311421c9613f707 clients/php: enforce style and PHP 8.0 syntax
31f2a08126789656f7aaa8274aa47e94ee4f3027 clients/typescript: format generated clients with Prettier
5e871ab42cdb348e43fd02cc46c8c42afd822a56 release: verify formatted TypeScript generator packages
86e32916da1c7236416cac1771fabc412620794e clients: align formatting tools and contributor checks
d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038 clients/rust: verify fixture formatting and failures
```

## Native hooks and operation effects

Interactive rebase was limited to the four commits following
`31f2a08126789656f7aaa8274aa47e94ee4f3027`: pick release, fixup R1,
then replay shared tooling and Rust. Native configuration-signature verification
stopped `prepare-commit-msg` twice: baseline config during fixup, then restoration
of the reviewed shared config. Each time actual HEAD/index/effects were inspected;
`.overcommit.yml` and `.git-hooks` were verified byte-exact against their retained
owning commit (`5d0d81a1`, then `e800d40b`); the custom plugins were read;
ordinary `bundle exec overcommit --sign` and `git rebase --continue` resumed.
No bypass, reset, clean, stash, disabled signatures or changed hook settings.

Postfold `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bundle exec overcommit --run`
completed with exit 0: PythonChecks, HaveapiI18n, JsFormat, PhpCsFixer and RuboCop
all reported OK. Config/plugins match the accepted fixed tree. An earlier
`--run pre_commit` invocation selected no individual checks; its empty success
is not used as verification evidence. The complete native run took longer
than the earlier aggregate check, so own command status was inspected and
reconciled before ownership release. No full tests or integration were rerun.

Final index/worktree are clean; rebase and native-hook commands have completed.
Lead retains the parity/metadata rerun and any publication/integration decision.

## Complete reviewed-range comparison

`git range-diff --no-color ae46cf27a9afb6558d386c293cec7231dd6c423d..864b80bc177625008ee843e9790564c8e9bc2b27 ae46cf27a9afb6558d386c293cec7231dd6c423d..d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038`:

```diff
 1:  5aa2de00 =  1:  5aa2de00 clients/js: normalize authored source with Prettier defaults
 2:  058e9315 =  2:  058e9315 clients/js: enforce shared Prettier defaults for authored source
 3:  26f578ce =  3:  26f578ce ci: cover Ruby tooling inputs in RuboCop triggers
 4:  8bd66938 =  4:  8bd66938 clients/go: cover formatting failures and canonical output
 5:  05082918 =  5:  05082918 clients/php: apply canonical source formatting
 6:  08e8716d =  6:  08e8716d clients/php: enforce style and PHP 8.0 syntax
 7:  31f2a081 =  7:  31f2a081 clients/typescript: format generated clients with Prettier
 8:  5d0d81a1 !  8:  5e871ab4 release: verify formatted TypeScript generator packages
    @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScri
          locks['clients/typescript/Gemfile.lock'] = lock.sub("haveapi-typescript-client (#{artifacts.version})", 'haveapi-typescript-client (999.0.0)')
          File.write(File.join(tmp, 'release-manifest.json'), JSON.generate(manifest))
          expect { candidate.verify(tmp) }.to raise_error(HaveAPI::Release::Error, %r{typescript/Gemfile.lock})
    +@@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScriptSmoke do
    +       .to raise_error(HaveAPI::Release::Error, /differs from source/)
    +   end
    + 
    +-  it 'extracts both artifacts and removes ambient load overrides before invoking the consumer' do
    ++  it 'extracts both artifacts with stable formatter paths and removes ambient load overrides' do
    +     typescript_gem
    +     build_gem('clients/ruby', 'haveapi-client')
    +     runtime = File.join(tmp, 'runtime')
     @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScriptSmoke do
          allow(Digest::SHA256).to receive(:file).with(File.join(runtime, 'dist/haveapi-client.js'))
                                                 .and_return(double(hexdigest: HaveAPI::Release::TypeScriptSmoke::RUNTIME_SHA256))
          allow(HaveAPI::Release).to receive(:capture).and_return('["source",{}]')
     -    allow(HaveAPI::Release).to receive(:run) do |env, ruby, disable, shared_flag, shared_lib, flag, library, expression, _script, extracted, shared, version, identity, prepared_runtime, compiler, **options|
    ++    forwarded_prettier = []
     +    allow(HaveAPI::Release).to receive(:run) do |env, ruby, disable, shared_flag, shared_lib, flag, library, expression, script, extracted, shared, version, identity, prepared_runtime, compiler, **options|
            expect([ruby, disable, shared_flag, flag, expression]).to eq([RbConfig.ruby, '--disable-gems', '-I', '-I', '-e'])
            expect(shared_lib).to eq(File.join(shared, 'lib'))
    @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScri
            expect(File).to exist(File.join(extracted, 'Gemfile'))
     +      expect(File.read(File.join(extracted, 'lib/haveapi/typescript_client/prettier.json'))).to eq("{}\n")
            expect(env).to include('RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil)
    -+      expect(env.fetch('PRETTIER')).to eq(ENV.fetch('PRETTIER', 'prettier'))
    ++      forwarded_prettier << env.fetch('PRETTIER')
     +      expect(script).to include('formatter config loaded outside extracted artifact', "manifest.fetch('formatter') == formatter.new.provenance")
            ENV.keys.grep(/\ABUNDLE_/).each { |key| expect(env.fetch(key)).to be_nil }
            expect([version, identity, prepared_runtime]).to eq([artifacts.version, '["source",{}]', runtime])
            expect(compiler).to eq(File.join(root, 'clients/js/node_modules/typescript/bin/tsc'))
    +       expect(options.fetch(:chdir)).to eq(File.dirname(extracted))
    +     end
    +-    described_class.run(artifacts, tmp, runtime)
    +-    expect(HaveAPI::Release).to have_received(:run).once
    ++    allow(ENV).to receive(:fetch).and_call_original
    ++    ['./tools/prettier', 'prettier'].each do |prettier|
    ++      allow(ENV).to receive(:fetch).with('PRETTIER', 'prettier').and_return(prettier)
    ++      Dir.chdir(tmp) { described_class.run(artifacts, tmp, runtime) }
    ++    end
    ++    expect(forwarded_prettier).to eq([File.join(tmp, 'tools/prettier'), 'prettier'])
    ++    expect(HaveAPI::Release).to have_received(:run).twice
    +   end
    + end
     
      ## utils/release/typescript_smoke.rb ##
     @@ utils/release/typescript_smoke.rb: module HaveAPI
    +           raise Error, 'Wrong shared Ruby client gem identity'
              end
      
    ++        prettier = ENV.fetch('PRETTIER', 'prettier')
    ++        prettier = File.expand_path(prettier) if prettier.include?(File::SEPARATOR)
              env = ENV.keys.grep(/\ABUNDLE_/).to_h { |key| [key, nil] }.merge(
     -          'RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil
     +          'RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil,
    -+          'PRETTIER' => ENV.fetch('PRETTIER', 'prettier')
    ++          'PRETTIER' => prettier
              )
              identity = Release.capture(env, RbConfig.ruby, '--disable-gems',
                                         '-I', File.join(artifacts.root, 'clients/ruby/lib'),
 9:  e800d40b =  9:  86e32916 clients: align formatting tools and contributor checks
10:  864b80bc = 10:  d6c2748a clients/rust: verify fixture formatting and failures
```

## Complete accepted-fixed-range comparison

`git range-diff --no-color ae46cf27a9afb6558d386c293cec7231dd6c423d..436332b5cef6b8c852eea02b5d13fc7975cbef49 ae46cf27a9afb6558d386c293cec7231dd6c423d..d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038`:

```diff
 1:  5aa2de00 =  1:  5aa2de00 clients/js: normalize authored source with Prettier defaults
 2:  058e9315 =  2:  058e9315 clients/js: enforce shared Prettier defaults for authored source
 3:  26f578ce =  3:  26f578ce ci: cover Ruby tooling inputs in RuboCop triggers
 4:  8bd66938 =  4:  8bd66938 clients/go: cover formatting failures and canonical output
 5:  05082918 =  5:  05082918 clients/php: apply canonical source formatting
 6:  08e8716d =  6:  08e8716d clients/php: enforce style and PHP 8.0 syntax
 7:  31f2a081 =  7:  31f2a081 clients/typescript: format generated clients with Prettier
 8:  5d0d81a1 !  8:  5e871ab4 release: verify formatted TypeScript generator packages
    @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScri
          locks['clients/typescript/Gemfile.lock'] = lock.sub("haveapi-typescript-client (#{artifacts.version})", 'haveapi-typescript-client (999.0.0)')
          File.write(File.join(tmp, 'release-manifest.json'), JSON.generate(manifest))
          expect { candidate.verify(tmp) }.to raise_error(HaveAPI::Release::Error, %r{typescript/Gemfile.lock})
    +@@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScriptSmoke do
    +       .to raise_error(HaveAPI::Release::Error, /differs from source/)
    +   end
    + 
    +-  it 'extracts both artifacts and removes ambient load overrides before invoking the consumer' do
    ++  it 'extracts both artifacts with stable formatter paths and removes ambient load overrides' do
    +     typescript_gem
    +     build_gem('clients/ruby', 'haveapi-client')
    +     runtime = File.join(tmp, 'runtime')
     @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScriptSmoke do
          allow(Digest::SHA256).to receive(:file).with(File.join(runtime, 'dist/haveapi-client.js'))
                                                 .and_return(double(hexdigest: HaveAPI::Release::TypeScriptSmoke::RUNTIME_SHA256))
          allow(HaveAPI::Release).to receive(:capture).and_return('["source",{}]')
     -    allow(HaveAPI::Release).to receive(:run) do |env, ruby, disable, shared_flag, shared_lib, flag, library, expression, _script, extracted, shared, version, identity, prepared_runtime, compiler, **options|
    ++    forwarded_prettier = []
     +    allow(HaveAPI::Release).to receive(:run) do |env, ruby, disable, shared_flag, shared_lib, flag, library, expression, script, extracted, shared, version, identity, prepared_runtime, compiler, **options|
            expect([ruby, disable, shared_flag, flag, expression]).to eq([RbConfig.ruby, '--disable-gems', '-I', '-I', '-e'])
            expect(shared_lib).to eq(File.join(shared, 'lib'))
    @@ utils/release/spec/typescript_spec.rb: RSpec.describe HaveAPI::Release::TypeScri
            expect(File).to exist(File.join(extracted, 'Gemfile'))
     +      expect(File.read(File.join(extracted, 'lib/haveapi/typescript_client/prettier.json'))).to eq("{}\n")
            expect(env).to include('RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil)
    -+      expect(env.fetch('PRETTIER')).to eq(ENV.fetch('PRETTIER', 'prettier'))
    ++      forwarded_prettier << env.fetch('PRETTIER')
     +      expect(script).to include('formatter config loaded outside extracted artifact', "manifest.fetch('formatter') == formatter.new.provenance")
            ENV.keys.grep(/\ABUNDLE_/).each { |key| expect(env.fetch(key)).to be_nil }
            expect([version, identity, prepared_runtime]).to eq([artifacts.version, '["source",{}]', runtime])
            expect(compiler).to eq(File.join(root, 'clients/js/node_modules/typescript/bin/tsc'))
    +       expect(options.fetch(:chdir)).to eq(File.dirname(extracted))
    +     end
    +-    described_class.run(artifacts, tmp, runtime)
    +-    expect(HaveAPI::Release).to have_received(:run).once
    ++    allow(ENV).to receive(:fetch).and_call_original
    ++    ['./tools/prettier', 'prettier'].each do |prettier|
    ++      allow(ENV).to receive(:fetch).with('PRETTIER', 'prettier').and_return(prettier)
    ++      Dir.chdir(tmp) { described_class.run(artifacts, tmp, runtime) }
    ++    end
    ++    expect(forwarded_prettier).to eq([File.join(tmp, 'tools/prettier'), 'prettier'])
    ++    expect(HaveAPI::Release).to have_received(:run).twice
    +   end
    + end
     
      ## utils/release/typescript_smoke.rb ##
     @@ utils/release/typescript_smoke.rb: module HaveAPI
    +           raise Error, 'Wrong shared Ruby client gem identity'
              end
      
    ++        prettier = ENV.fetch('PRETTIER', 'prettier')
    ++        prettier = File.expand_path(prettier) if prettier.include?(File::SEPARATOR)
              env = ENV.keys.grep(/\ABUNDLE_/).to_h { |key| [key, nil] }.merge(
     -          'RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil
     +          'RUBYOPT' => nil, 'RUBYLIB' => nil, 'RUBYGEMS_GEMDEPS' => nil, 'NODE_PATH' => nil,
    -+          'PRETTIER' => ENV.fetch('PRETTIER', 'prettier')
    ++          'PRETTIER' => prettier
              )
              identity = Release.capture(env, RbConfig.ruby, '--disable-gems',
                                         '-I', File.join(artifacts.root, 'clients/ruby/lib'),
 9:  e800d40b =  9:  86e32916 clients: align formatting tools and contributor checks
10:  864b80bc = 10:  d6c2748a clients/rust: verify fixture formatting and failures
11:  436332b5 <  -:  -------- release: resolve relative formatter paths before smoke
```
