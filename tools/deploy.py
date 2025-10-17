"""
International Plebeian Academy - Deployment Tool
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

import os
import sys
import subprocess
import click
from datetime import datetime

@click.group()
def cli():
    """
    International Plebeian Academy Deployment Tools
    """
    pass

@cli.command()
@click.option('--environment', default='production', help='Deployment environment')
def deploy_frontend(environment):
    """
    Deploy frontend application
    """
    click.echo(f"Deploying frontend to {environment}...")
    
    click.echo("Building frontend...")
    subprocess.run(['npm', 'run', 'build'], cwd='../frontend', check=True)
    
    click.echo("Building Docker image...")
    subprocess.run([
        'docker', 'build',
        '-f', '../infrastructure/Dockerfile.frontend',
        '-t', f'plebeian-academy-frontend:{environment}',
        '../frontend'
    ], check=True)
    
    click.echo(f"Frontend deployed to {environment} successfully!")

@cli.command()
@click.option('--environment', default='production', help='Deployment environment')
def deploy_backend(environment):
    """
    Deploy backend application
    """
    click.echo(f"Deploying backend to {environment}...")
    
    click.echo("Building Docker image...")
    subprocess.run([
        'docker', 'build',
        '-f', '../infrastructure/Dockerfile.backend',
        '-t', f'plebeian-academy-backend:{environment}',
        '../backend'
    ], check=True)
    
    click.echo(f"Backend deployed to {environment} successfully!")

@cli.command()
@click.option('--environment', default='production', help='Deployment environment')
def deploy_full_stack(environment):
    """
    Deploy complete application stack
    """
    click.echo(f"Deploying full stack to {environment}...")
    
    ctx = click.get_current_context()
    
    ctx.invoke(deploy_frontend, environment=environment)
    ctx.invoke(deploy_backend, environment=environment)
    
    click.echo("Starting services with Docker Compose...")
    subprocess.run([
        'docker-compose',
        '-f', '../infrastructure/docker-compose.yml',
        'up', '-d'
    ], check=True)
    
    click.echo(f"Full stack deployed to {environment} successfully!")

@cli.command()
def deploy_kubernetes():
    """
    Deploy to Kubernetes cluster
    """
    click.echo("Deploying to Kubernetes...")
    
    click.echo("Applying Kubernetes configurations...")
    subprocess.run([
        'kubectl', 'apply',
        '-f', '../infrastructure/kubernetes/deployment.yaml'
    ], check=True)
    
    subprocess.run([
        'kubectl', 'apply',
        '-f', '../infrastructure/kubernetes/service.yaml'
    ], check=True)
    
    click.echo("Deployed to Kubernetes successfully!")

@cli.command()
def rollback():
    """
    Rollback to previous deployment
    """
    click.echo("Rolling back deployment...")
    
    subprocess.run([
        'kubectl', 'rollout', 'undo',
        'deployment/plebeian-academy-backend'
    ], check=True)
    
    subprocess.run([
        'kubectl', 'rollout', 'undo',
        'deployment/plebeian-academy-frontend'
    ], check=True)
    
    click.echo("Rollback completed successfully!")

@cli.command()
def backup_database():
    """
    Create database backup
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'backup_{timestamp}.sql'
    
    click.echo(f"Creating database backup: {backup_file}")
    
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        click.echo("ERROR: DATABASE_URL not configured")
        return
    
    subprocess.run([
        'pg_dump',
        database_url,
        '-f', backup_file
    ], check=True)
    
    click.echo(f"Database backup created: {backup_file}")

if __name__ == '__main__':
    cli()
