import * as pulumi from "@pulumi/pulumi";
import { ArtifactRegistry } from "./artifactRegistry";

// Create the dev repositories
const devRepositories = ArtifactRegistry.createDevRepositories();

// Create the prod repositories
const prodRepositories = ArtifactRegistry.createProdRepositories();

// Export any required outputs
pulumi.output({
    devRepositories: devRepositories,
    prodRepositories: prodRepositories
});