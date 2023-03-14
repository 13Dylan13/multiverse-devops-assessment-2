data "aws_availability_zones" "eu_west_2" { 
    state = "available"

    filter {
        name = "region-name"
        values = ["eu-west-2"] 
        }

    filter {
        name = "opt-in-status"
        values = ["opt-in-not-required"] }
        }
    }