## Overview

Three methods exist for creating Cloud Armor rules:

- ip_allow_standard_policy
- ip_allow_policy
- region_block_policy

The policy with "standard" was created in Basic mode, while the others were crafted in Advanced mode.

<br/>

### Basic Mode
In Basic mode, you can swiftly create rules using only IP addresses or ranges for both blocked and allowed lists.

<br/>

### Advanced Mode
Advanced mode offers flexibility in defining custom match criteria. You can specify parameters such as the source IP range, source region, and more using the Common Expression Language (CEL).

Choose the method that best aligns with your needs. All the policy types mentioned are edge security policies.

<br/>

# Reference
- [gcp.compute](https://www.pulumi.com/registry/packages/gcp/api-docs/compute/#gcp-compute)