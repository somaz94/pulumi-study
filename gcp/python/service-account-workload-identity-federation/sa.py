# sa.py not prefix
from pulumi_gcp import serviceaccount

class ServiceAccount:
    def __init__(self, name, project):
        self.account = serviceaccount.Account(
            name,
            account_id=name,
            display_name=name,
            description=f"{name} admin",
            project=project
        )

    @property
    def account_id(self) -> str:
        return self.account.account_id

