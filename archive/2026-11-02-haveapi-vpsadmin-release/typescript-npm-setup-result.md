# TypeScript npm setup result

- Result: passed (exit status 0)
- Tested revision: `e5786f69b7c223c3bb5b1de99b7f97186eec368a`; the intended package.json dependency edit was present.
- Command: `nix develop --offline --command sh -eu -c 'npm install --package-lock-only --ignore-scripts --no-audit --no-fund; npm ci --ignore-scripts --no-audit --no-fund; npm ls haveapi-client prettier typescript; npm view haveapi-client@0.32.0 version dist.integrity --json --registry https://registry.npmjs.org'`
- Elapsed: 7 seconds.
- Full stdout/stderr and exit evidence: [typescript-npm-setup.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-02-haveapi-vpsadmin-release/typescript-npm-setup.log)
- `npm ls` resolved haveapi-client 0.32.0, prettier 3.9.10, and typescript 6.0.3. Registry metadata reported version 0.32.0 and integrity `sha512-ldZcLcQEV2hSEznKdrNGnpjwJLsyu5QyhHxf5DzrfBC12+L7ZVCKqC4Hz4KmjTG8B8HLXXgbOXF6503yXBQQYA==`.
- No failures or still-running operations. `package-lock.json` and `node_modules` were updated by the assigned setup command.
