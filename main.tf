provider "aws" {
  
}
resource "aws_instance" "public_ec2" {
  ami = "ami-038bba9a164eb3dc1"
  instance_type   = "t2.micro" 
  key_name = "west"
  tags = {
    name="public"
  }
}
