let
  profileTarget = {
    kind = "repository";
    origin = "github.com/vpsfreecz/vpsfree-cz-configuration";
    name = "cz.vpsfree/machines/aitherdev";
  };
in
{
  schema = 1;
  inherit profileTarget;
  legacyAliases = [
    {
      resource = "machine:vpsfree:aitherdev";
      identity = profileTarget;
    }
  ];
}
