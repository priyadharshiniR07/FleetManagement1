provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_db_instance" "app_db" {
  allocated_storage    = 20
  engine               = "mysql"
  instance_class       = "db.t3.micro"           # <-- changed from db.t2.micro
  identifier           = "appdb-instance"
  db_name              = "appdb"
  username             = "admin"
  password             = "password123"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
}

resource "aws_instance" "app_server" {
  ami           = "ami-010876b9ddd38475e"
  instance_type = "t2.micro"
  key_name      = "mynewpair"   # <-- Add this line

  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y docker.io
    systemctl start docker
    systemctl enable docker
    usermod -aG docker ubuntu
    docker run -d -p 80:80 --env DB_HOST=${aws_db_instance.app_db.address} --env DB_USER=admin --env DB_PASS=password123 priyadharshiniro7/fleet-management-app:latest
    EOF

  tags = {
    Name = "AppServer"
  }
}