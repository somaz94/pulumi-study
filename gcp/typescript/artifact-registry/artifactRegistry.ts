import * as pulumi from "@pulumi/pulumi";
import * as artifactregistry from "@pulumi/gcp/artifactregistry";
import { REGION, devRepo, prodRepo } from "./config";
import { Utils } from "./utils";

export class ArtifactRegistry {
    static createRepositories(repoList: string[]): { [key: string]: pulumi.CustomResource } {
        const repositories: { [key: string]: pulumi.CustomResource } = {};
        for (const repo of repoList) {
            const repoName = Utils.resourceName(repo);
            repositories[repoName] = new artifactregistry.Repository(repoName, {
                location: REGION,
                format: "DOCKER",
                repositoryId: repoName,
                labels: {
                    createdby: "pulumi",
                },
            });
        }
        return repositories;
    }

    static createDevRepositories(): { [key: string]: pulumi.CustomResource } {
        return this.createRepositories(devRepo);
    }

    static createProdRepositories(): { [key: string]: pulumi.CustomResource } {
        return this.createRepositories(prodRepo);
    }
}
