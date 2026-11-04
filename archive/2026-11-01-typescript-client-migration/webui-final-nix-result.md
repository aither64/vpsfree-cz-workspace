# WebUI final Nix verification result

- Operation: `webui-final-nix-observed` (observer PID 970129)
- Result: passed; command exit status 0
- Tested revision: `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab`
- Command: the exact five-output command in `w-final-nix-five-output-command.txt`
- Elapsed: 53.328 seconds; finished 2026-11-02T00:11:12.916496+00:00
- Observer state: `webui-final-nix-observed-state.json`
- Observer exit receipt: `webui-final-nix-observed-exit.json`
- Observer output: `webui-final-nix-observer-output.log`
- Build log: `webui-final-nix-observed.log`

Printed output identities:

1. Frontend: `/nix/store/bicyxsc4phw6n82q55ssz9xfas0v238n-vpsadmin-webui-frontend-1.0.0`
2. BFF: `/nix/store/a9rn1bkz0hz2kyc71kcy09hickd5j4gw-vpsadmin-webui-bff-0.1.0`
3. Provenance: `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance`
4. Source contents: `/nix/store/fc1yp9005gd21473li0sbzrfh67xwp5g-vpsadmin-webui-source-contents`
5. Package contents: `/nix/store/500jbhwhsna2qqik6zr43pw62408zlca-vpsadmin-webui-package-contents`

Read-only frontend and BFF build-info metadata both report schemaVersion 1, commit `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab`, shortCommit `14cfdcb6d2a3`, dirty `false`, and source `environment`. The frontend metadata is at `build-info.json`; BFF metadata is at `share/vpsadmin-webui-bff/build-info.json`.
