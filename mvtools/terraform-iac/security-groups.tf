resource "aws_security_group" "alb" {
    name_prefix                 = "mvws9"
    revoke_rules_on_delete      = true
    vpc_id                      = aws_vpc.this.id

    tags = {
        Name = "multiverse-alb"
    }
}

resource "aws_security_group" "ec2" {
    name_prefix                 = "mvws9-ec2"
    revoke_rules_on_delete      = true
    vpc_id                      = aws_vpc.this.id

    tags = {
        Name = "multiverse-ec2"
    }
}