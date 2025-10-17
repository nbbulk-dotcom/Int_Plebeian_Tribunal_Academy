# Deployment Guide

This guide provides comprehensive instructions for deploying the International Plebeian Academy platform to various environments.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Configuration](#environment-configuration)
3. [Local Development Deployment](#local-development-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Kubernetes Deployment](#kubernetes-deployment)
6. [Cloud Deployment (AWS)](#cloud-deployment-aws)
7. [Monitoring and Maintenance](#monitoring-and-maintenance)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

- **Docker:** version 20.10.0 or higher
- **Docker Compose:** version 2.0.0 or higher
- **Kubernetes:** version 1.24.0 or higher (for Kubernetes deployment)
- **kubectl:** version 1.24.0 or higher
- **Terraform:** version 1.0.0 or higher (for cloud deployment)
- **Node.js:** version 18.0.0 or higher
- **Python:** version 3.11.0 or higher
- **PostgreSQL:** version 15.0 or higher

### Recommended System Requirements

**Minimum:**
- CPU: 4 cores
- RAM: 8 GB
- Storage: 50 GB

**Recommended:**
- CPU: 8 cores
- RAM: 16 GB
- Storage: 200 GB SSD

---

## Environment Configuration

### 1. Clone Repository

```bash
git clone https://github.com/nbbulk-dotcom/Int_Plebeian_Tribunal_Academy.git
cd Int_Plebeian_Tribunal_Academy
```

### 2. Configure Environment Variables

Create environment files for each component:

**Backend (.env):**
```bash
cp backend/.env.example backend/.env
```

Edit `backend/.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/plebeian_academy
JWT_SECRET_KEY=your-secret-key-here
BLOCKCHAIN_NETWORK_URL=http://localhost:8545
REDIS_URL=redis://localhost:6379
APP_VERSION=1.0.0
ENVIRONMENT=production
```

**Frontend (.env):**
```bash
cp frontend/.env.example frontend/.env
```

Edit `frontend/.env`:
```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
VITE_APP_VERSION=1.0.0
```

**Blockchain (.env):**
```bash
cp blockchain/.env.example blockchain/.env
```

Edit `blockchain/.env`:
```env
NETWORK_ID=1337
MNEMONIC=your-mnemonic-here
INFURA_KEY=your-infura-key-here
```

---

## Local Development Deployment

### 1. Install Dependencies

```bash
python tools/setup.py install-dependencies
```

### 2. Setup Database

```bash
python tools/setup.py setup-database
```

### 3. Compile Smart Contracts

```bash
python tools/setup.py compile-contracts
```

### 4. Build Frontend

```bash
python tools/setup.py build-frontend
```

### 5. Start Services

**Backend:**
```bash
cd backend
python app.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

**Blockchain:**
```bash
cd blockchain
npx ganache-cli --networkId 1337
```

Access the application at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Blockchain: http://localhost:8545

---

## Docker Deployment

### 1. Build Docker Images

```bash
# Build frontend
docker build -f infrastructure/Dockerfile.frontend -t plebeian-academy-frontend:latest frontend/

# Build backend
docker build -f infrastructure/Dockerfile.backend -t plebeian-academy-backend:latest backend/
```

### 2. Start Services with Docker Compose

```bash
cd infrastructure
docker-compose up -d
```

### 3. Verify Services

```bash
docker-compose ps
```

All services should be in "Up" state.

### 4. View Logs

```bash
docker-compose logs -f
```

### 5. Stop Services

```bash
docker-compose down
```

Access the application at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

---

## Kubernetes Deployment

### 1. Prerequisites

Ensure you have a Kubernetes cluster running and `kubectl` configured.

### 2. Create Namespace

```bash
kubectl create namespace plebeian-academy
```

### 3. Configure Secrets

Create a `secrets.yaml` file:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: plebeian-academy-secrets
  namespace: plebeian-academy
type: Opaque
stringData:
  database-url: "postgresql://user:password@postgres:5432/plebeian_academy"
  jwt-secret: "your-secret-key-here"
  blockchain-private-key: "your-private-key-here"
```

Apply secrets:
```bash
kubectl apply -f secrets.yaml
```

### 4. Deploy Application

```bash
kubectl apply -f infrastructure/kubernetes/deployment.yaml
kubectl apply -f infrastructure/kubernetes/service.yaml
```

### 5. Verify Deployment

```bash
kubectl get deployments -n plebeian-academy
kubectl get services -n plebeian-academy
kubectl get pods -n plebeian-academy
```

### 6. Access Application

Get the external IP:
```bash
kubectl get service plebeian-academy-frontend -n plebeian-academy
```

Access the application using the external IP address.

### 7. Scale Deployment

```bash
kubectl scale deployment plebeian-academy-backend --replicas=5 -n plebeian-academy
```

### 8. Update Deployment

After making changes:
```bash
kubectl rollout restart deployment/plebeian-academy-backend -n plebeian-academy
kubectl rollout status deployment/plebeian-academy-backend -n plebeian-academy
```

### 9. Rollback Deployment

If issues occur:
```bash
kubectl rollout undo deployment/plebeian-academy-backend -n plebeian-academy
```

---

## Cloud Deployment (AWS)

### 1. Prerequisites

- AWS account with appropriate permissions
- AWS CLI configured
- Terraform installed

### 2. Configure Terraform Variables

Create `terraform.tfvars`:

```hcl
aws_region      = "us-east-1"
environment     = "production"
cluster_name    = "plebeian-academy-cluster"
db_password     = "your-secure-password"
```

### 3. Initialize Terraform

```bash
cd infrastructure/terraform
terraform init
```

### 4. Plan Deployment

```bash
terraform plan
```

Review the planned infrastructure changes.

### 5. Apply Configuration

```bash
terraform apply
```

Type `yes` to confirm.

### 6. Get Outputs

```bash
terraform output
```

Note the VPC ID, database endpoint, and other important values.

### 7. Deploy Application to AWS

Use the Python deployment tool:

```bash
python tools/deploy.py deploy-full-stack --environment=production
```

### 8. Configure DNS

Point your domain to the load balancer:
```bash
aws elbv2 describe-load-balancers --names plebeian-academy-lb
```

### 9. Setup SSL/TLS

Use AWS Certificate Manager to provision SSL certificates:
```bash
aws acm request-certificate --domain-name plebeianacademy.org --subject-alternative-names www.plebeianacademy.org
```

---

## Monitoring and Maintenance

### Health Checks

**Check all services:**
```bash
python tools/monitor.py check-all-services
```

**Monitor system health:**
```bash
python tools/monitor.py system-health --interval=10
```

### Logs

**View Docker logs:**
```bash
python tools/monitor.py view-logs
```

**View Kubernetes logs:**
```bash
kubectl logs -f deployment/plebeian-academy-backend -n plebeian-academy
```

### Database Backups

**Create backup:**
```bash
python tools/deploy.py backup-database
```

**Restore backup:**
```bash
pg_restore -d plebeian_academy backup_20251017_120000.sql
```

### Updates and Upgrades

**Update application:**
```bash
python tools/deploy.py deploy-full-stack --environment=production
```

**Update Kubernetes deployment:**
```bash
kubectl set image deployment/plebeian-academy-backend backend=plebeian-academy-backend:v1.1.0 -n plebeian-academy
```

---

## Troubleshooting

### Service Not Starting

**Check logs:**
```bash
docker-compose logs [service-name]
```

**Check environment variables:**
```bash
docker-compose config
```

### Database Connection Issues

**Verify database is running:**
```bash
docker-compose ps postgres
```

**Test connection:**
```bash
psql postgresql://user:password@localhost:5432/plebeian_academy
```

### Kubernetes Pod Crashes

**Check pod status:**
```bash
kubectl describe pod [pod-name] -n plebeian-academy
```

**Check logs:**
```bash
kubectl logs [pod-name] -n plebeian-academy
```

### High Resource Usage

**Check resource usage:**
```bash
python tools/monitor.py system-health
```

**Scale services:**
```bash
kubectl scale deployment plebeian-academy-backend --replicas=3 -n plebeian-academy
```

### Blockchain Node Issues

**Check node status:**
```bash
python tools/monitor.py check-blockchain
```

**Restart node:**
```bash
docker-compose restart blockchain
```

---

## Security Considerations

1. **Change default passwords** in all .env files
2. **Use secrets management** (AWS Secrets Manager, Kubernetes Secrets)
3. **Enable SSL/TLS** for all production deployments
4. **Configure firewalls** to restrict access
5. **Regular security updates** for all dependencies
6. **Enable audit logging** for all critical operations
7. **Implement rate limiting** on public endpoints

---

## Performance Optimization

1. **Enable caching** with Redis
2. **Use CDN** for static assets
3. **Database indexing** for frequently queried fields
4. **Load balancing** across multiple instances
5. **Connection pooling** for database connections
6. **Async processing** for long-running tasks

---

## Disaster Recovery

### Backup Strategy

- **Database:** Daily automated backups
- **Files:** Hourly incremental backups
- **Configuration:** Version-controlled in Git

### Recovery Procedures

1. Restore database from latest backup
2. Redeploy application from version control
3. Verify all services are operational
4. Run integrity checks

---

## Support

For deployment support:
- Documentation: https://docs.plebeianacademy.org/deployment
- GitHub Issues: https://github.com/nbbulk-dotcom/Int_Plebeian_Tribunal_Academy/issues
- Email: devops@plebeianacademy.org

---

## Changelog

- **v1.0.0** - Initial deployment documentation
