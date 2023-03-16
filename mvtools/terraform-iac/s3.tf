resource "aws_s3_bucket" "this" { 
    bucket_prefix           = "mvws9-dylan-rickerby" 
    force_destroy           = true

    tags = {
        Name                = "multiverse"
    }
}

resource "aws_s3_bucket_acl" "this" {
    bucket                  = aws_s3_bucket.this.id
    acl                     = "private"
}

resource "aws_s3_object" "this" {
    bucket                  = aws_s3_bucket.this.id
    key                     = "results.csv"
    source                  = "$/resuts.csv"
    etag                    = filemd5("$/results.csv")
}