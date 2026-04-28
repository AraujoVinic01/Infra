provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
# Random suffix to ensure unique bucket name globally
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# S3 bucket for learning purposes
resource "aws_s3_bucket" "learning_bucket" {
  bucket = "${var.project_name}-${var.environment}-${random_id.bucket_suffix.hex}"
}
