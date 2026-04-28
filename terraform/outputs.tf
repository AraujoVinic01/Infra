output "bucket_name" {
  description = "Name of the S3 bucket created"
  value       = aws_s3_bucket.learning_bucket.bucket
}

output "bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.learning_bucket.arn
}

output "bucket_region" {
  description = "AWS region where the bucket lives"
  value       = aws_s3_bucket.learning_bucket.region
}