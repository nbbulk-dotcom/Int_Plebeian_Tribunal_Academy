
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region for infrastructure deployment"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (development, staging, production)"
  type        = string
  default     = "production"
}

variable "cluster_name" {
  description = "Name of the Kubernetes cluster"
  type        = string
  default     = "plebeian-academy-cluster"
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "plebeian-academy-vpc"
    Environment = var.environment
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name        = "plebeian-academy-igw"
    Environment = var.environment
  }
}

resource "aws_subnet" "public" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.${count.index}.0/24"
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name        = "plebeian-academy-public-subnet-${count.index + 1}"
    Environment = var.environment
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name        = "plebeian-academy-public-rt"
    Environment = var.environment
  }
}

resource "aws_route_table_association" "public" {
  count          = 2
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "cluster" {
  name        = "plebeian-academy-cluster-sg"
  description = "Security group for Plebeian Academy cluster"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "plebeian-academy-cluster-sg"
    Environment = var.environment
  }
}

resource "aws_db_instance" "main" {
  identifier           = "plebeian-academy-db"
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.medium"
  allocated_storage    = 100
  storage_type         = "gp3"
  db_name              = "plebeian_academy"
  username             = "admin"
  password             = var.db_password
  skip_final_snapshot  = false
  final_snapshot_identifier = "plebeian-academy-final-snapshot"

  vpc_security_group_ids = [aws_security_group.cluster.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name

  tags = {
    Name        = "plebeian-academy-db"
    Environment = var.environment
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "plebeian-academy-db-subnet-group"
  subnet_ids = aws_subnet.public[*].id

  tags = {
    Name        = "plebeian-academy-db-subnet-group"
    Environment = var.environment
  }
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

resource "aws_s3_bucket" "assets" {
  bucket = "plebeian-academy-assets-${var.environment}"

  tags = {
    Name        = "plebeian-academy-assets"
    Environment = var.environment
  }
}

resource "aws_s3_bucket_public_access_block" "assets" {
  bucket = aws_s3_bucket.assets.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "database_endpoint" {
  value     = aws_db_instance.main.endpoint
  sensitive = true
}

output "assets_bucket_name" {
  value = aws_s3_bucket.assets.id
}
