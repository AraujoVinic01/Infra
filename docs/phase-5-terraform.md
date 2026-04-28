# Phase 5 — Infrastructure as Code with Terraform & AWS

## 🎯 Goal

Provision real cloud infrastructure on AWS using Terraform, replacing manual console clicks with versioned, reproducible code.

## 🧠 Concepts learned

- **Infrastructure as Code (IaC)** — describing infrastructure declaratively in `.tf` files
- **Provider** — Terraform plugin that translates code into API calls (AWS, random)
- **Resource** — a single piece of infrastructure (S3 bucket, IAM user, etc.)
- **Variables & Outputs** — parameterize input, expose useful data after apply
- **State** — Terraform's memory of what exists (`terraform.tfstate`)
- **Default tags** — automatic tagging of every AWS resource

## 🛠️ What was built

- AWS account with **billing alert** (zero-spend budget)
- IAM user `terraform-user` with programmatic access
- AWS CLI installed and configured locally
- Terraform configuration to create:
  - One S3 bucket with globally unique name (random suffix)
  - Default tags applied to all resources
- Outputs exposing bucket name, ARN, and region

## 📁 Files

```text
terraform/
├── versions.tf      # Terraform & provider version pinning
├── variables.tf     # Input variables (region, project, environment)
├── main.tf          # AWS provider config + resources
├── outputs.tf       # Values exposed after apply
└── .gitignore       # Protects state files & secrets
```

## ⚙️ Workflow

```bash
# Initialize providers (first time or after adding providers)
terraform init

# Preview changes without applying
terraform plan

# Apply changes (creates/updates real AWS resources)
terraform apply

# Destroy all managed resources
terraform destroy
```

## 🔐 Security notes

- Access keys are **never committed** to Git
- `terraform.tfstate` is gitignored — it can contain secrets
- IAM user has only programmatic access (no console login)
- Billing alert configured to catch unexpected charges

## 🧗 Challenges faced

- **Nested folder mistake** — VS Code created `terraform/terraform/` due to a `mkdir` typo; fixed by deleting and recreating in the right place
- **Provider not loading** — first `terraform init` ignored a newly added `random` provider; solved with `terraform init -upgrade`
- **Bucket name uniqueness** — S3 bucket names are globally unique; solved using `random_id` resource as suffix

## 📚 References

- [Terraform AWS Provider docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [HashiCorp Learn — Terraform](https://developer.hashicorp.com/terraform/tutorials)
- [AWS Free Tier](https://aws.amazon.com/free/)