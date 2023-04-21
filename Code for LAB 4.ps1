# Write a PowerShell script that automates the configuration of the required settings:
## 1.1.5 (L1)
## 18.3.2 (L1)

# Set the AWS region
$region = "us-west-2"

# Configure the required security controls
# 1.1.5 (L1): Ensure IAM password policy requires at least one uppercase letter
Write-Host "Configuring IAM password policy..."
$policy = Get-IAMAccountPasswordPolicy
$policy.RequireUppercaseCharacters = $true
$policy | Set-IAMAccountPasswordPolicy

# 18.3.2 (L1): Ensure Amazon S3 bucket policies are configured to restrict access to specific IAM roles or users
Write-Host "Configuring S3 bucket policies..."
$s3Buckets = Get-S3Bucket
foreach ($bucket in $s3Buckets) {
    $policy = Get-S3BucketPolicy -BucketName $bucket.BucketName -ErrorAction SilentlyContinue
    if ($policy -ne $null) {
        Write-Host "Bucket policy found for $($bucket.BucketName). Configuring..."
        $policyDocument = ConvertFrom-Json -InputObject $policy.Policy
        $policyDocument.Statement | ForEach-Object {
            if ($_.Principal.AWS -ne $null) {
                $_.Principal.AWS = $_.Principal.AWS | Where-Object { $_ -match "^arn:aws:iam::[0-9]+:role/.+" -or $_ -match "^arn:aws:iam::[0-9]+:user/.+" }
            }
        }
        $newPolicy = $policyDocument | ConvertTo-Json -Depth 100
        Write-S3BucketPolicy -BucketName $bucket.BucketName -Policy $newPolicy
    }
}

Write-Host "Configuration complete."

# Reference
# OpenAI