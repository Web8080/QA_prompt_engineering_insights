# Deployment Guide

## Production Deployment

This guide covers deploying the QA Prompt Engineering project to production.

### Prerequisites

- Python 3.8 or higher
- Virtual environment
- Production API keys and credentials
- Deployment infrastructure (Docker/Kubernetes/Cloud)

### Configuration

1. Copy environment template:
```bash
cp config/.env.example .env
```

2. Update production configuration in `production/config.py`:
   - Replace `******` placeholders with actual values
   - Set production API keys
   - Configure database URLs
   - Set monitoring endpoints

3. Update `production/deploy.py`:
   - Configure deployment target
   - Set up CI/CD integration
   - Configure rollback procedures

### Deployment Steps

#### Option 1: Docker Deployment

```bash
# Build Docker image (create Dockerfile)
docker build -t qa-prompt-engineering:latest .

# Run container
docker run -d \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your_key \
  -e ENVIRONMENT=production \
  qa-prompt-engineering:latest
```

#### Option 2: Kubernetes Deployment

```bash
# Apply Kubernetes manifests (create k8s/ directory)
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

#### Option 3: Cloud Deployment

**AWS:**
- Deploy using ECS/EKS
- Use Elastic Beanstalk
- Use Lambda for serverless

**GCP:**
- Deploy using Cloud Run
- Use GKE for Kubernetes
- Use App Engine

**Azure:**
- Deploy using Container Instances
- Use AKS for Kubernetes
- Use App Service

### Post-Deployment

1. Run health checks:
```bash
curl http://your-domain/health
```

2. Run production tests:
```bash
API_BASE_URL=https://your-domain python testing/run_qa_suite.py
```

3. Monitor logs and metrics:
   - Check application logs
   - Monitor error rates
   - Track performance metrics

### Monitoring Setup

Configure monitoring in `production/monitoring.py`:

- **Metrics**: Prometheus, Datadog, CloudWatch
- **Logging**: ELK Stack, CloudWatch Logs, Splunk
- **Alerting**: PagerDuty, Slack, Email

### Rollback Procedure

```bash
# Rollback using deployment script
python production/deploy.py --rollback

# Or manually revert deployment
# (implementation depends on your deployment method)
```

### Security Checklist

- [ ] All `******` placeholders replaced
- [ ] API keys secured (use secrets management)
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Monitoring enabled
- [ ] Logging configured
- [ ] Backup procedures in place
- [ ] Security testing completed

## Environment Variables

Required production environment variables:

- `OPENAI_API_KEY`: OpenAI API key
- `SECRET_KEY`: Application secret key
- `PRODUCTION_DATABASE_URL`: Database connection string
- `PRODUCTION_REDIS_URL`: Redis connection string (if used)
- `ENVIRONMENT`: Set to "production"
- `LOG_LEVEL`: Logging level (INFO, WARNING, ERROR)
- `CORS_ORIGINS`: Allowed CORS origins (comma-separated)

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies installed
2. **Connection errors**: Check API endpoints and network
3. **Configuration errors**: Verify all placeholders replaced
4. **Performance issues**: Check rate limits and resource usage

### Support

For deployment issues, check:
- Application logs
- Monitoring dashboards
- Error tracking (Sentry, etc.)

