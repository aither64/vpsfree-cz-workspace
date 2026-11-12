command: nix develop --offline --command sh -eu -c './tools/regenerate --haveapi-source ../haveapi-ts-tools --check; HAVEAPI_SOURCE=../haveapi-ts-tools node --test test/regeneration/sources.test.mjs; npm test; npm run test:package; npm run typecheck; npm run typecheck:consumer'
exit: 0
elapsed_seconds: 77
revision: e5786f69b7c223c3bb5b1de99b7f97186eec368a
