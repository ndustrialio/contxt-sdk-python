from contxt.services.assets import AssetsService
from contxt.auth.cli import CLIAuth

if __name__ == "__main__":
    auth = CLIAuth()
    organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"
    af = AssetsService(auth, organization_id, env="staging")
    mv = af.get_metric_values("92785985-4498-4735-adf4-18ce0c06a58f")
    v = mv[0].post()
    print("done")
