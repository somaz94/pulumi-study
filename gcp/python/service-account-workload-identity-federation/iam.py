# iam.py
from pulumi_gcp import projects

class IAMPermissions:
    def __init__(self, project, workload_identity_pool_id, service_account_email):
        self.project = project
        self.workload_identity_pool_id = workload_identity_pool_id
        self.service_account_email = service_account_email
        self.assign_permissions()

    def assign_permissions(self):
        # 권한 목록
        roles = [
            "roles/iam.serviceAccountAdmin",
            "roles/iam.serviceAccountKeyAdmin",
            "roles/iam.serviceAccountTokenCreator",
            "roles/iam.workloadIdentityPoolAdmin"
        ]

        for role in roles:
            # 워크로드 ID에 권한 부여
            wip_member = self.workload_identity_pool_id.apply(lambda wip_id: 
                f"principalSet://iam.googleapis.com/projects/{self.project}/locations/global/workloadIdentityPools/{wip_id}/*")
            projects.IAMBinding(f"{role}-wip-binding",
                role=role,
                project=self.project,
                members=[wip_member])

            # 서비스 계정에 권한 부여
            sa_member = self.service_account_email.apply(lambda email: f"serviceAccount:{email}")
            projects.IAMBinding(f"{role}-sa-binding",
                role=role,
                project=self.project,
                members=[sa_member])


