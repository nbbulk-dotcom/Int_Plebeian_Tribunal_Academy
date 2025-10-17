"""
International Plebeian Academy - Setup Tool
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

import os
import sys
import subprocess
import click
from pathlib import Path

@click.group()
def cli():
    """
    International Plebeian Academy Setup Tools
    """
    pass

@cli.command()
def install_dependencies():
    """
    Install all project dependencies
    """
    click.echo("Installing frontend dependencies...")
    subprocess.run(['npm', 'install'], cwd='../frontend', check=True)
    
    click.echo("Installing backend dependencies...")
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd='../backend', check=True)
    
    click.echo("Installing blockchain dependencies...")
    subprocess.run(['npm', 'install'], cwd='../blockchain', check=True)
    
    click.echo("Installing bot dependencies...")
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd='../bots', check=True)
    
    click.echo("All dependencies installed successfully!")

@cli.command()
def setup_database():
    """
    Setup database and run migrations
    """
    click.echo("Setting up database...")
    
    from backend.app import create_app
    from backend.models import db
    
    app = create_app()
    
    with app.app_context():
        db.create_all()
        click.echo("Database tables created successfully!")

@cli.command()
def compile_contracts():
    """
    Compile smart contracts
    """
    click.echo("Compiling smart contracts...")
    subprocess.run(['npx', 'truffle', 'compile'], cwd='../blockchain', check=True)
    click.echo("Smart contracts compiled successfully!")

@cli.command()
def migrate_contracts():
    """
    Migrate smart contracts to blockchain
    """
    click.echo("Migrating smart contracts...")
    subprocess.run(['npx', 'truffle', 'migrate'], cwd='../blockchain', check=True)
    click.echo("Smart contracts migrated successfully!")

@cli.command()
def build_frontend():
    """
    Build frontend application
    """
    click.echo("Building frontend...")
    subprocess.run(['npm', 'run', 'build'], cwd='../frontend', check=True)
    click.echo("Frontend built successfully!")

@cli.command()
def check_environment():
    """
    Check environment configuration
    """
    click.echo("Checking environment configuration...")
    
    required_env_vars = [
        'DATABASE_URL',
        'JWT_SECRET_KEY',
        'BLOCKCHAIN_NETWORK_URL'
    ]
    
    missing_vars = []
    
    for var in required_env_vars:
        if not os.environ.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        click.echo(f"Missing environment variables: {', '.join(missing_vars)}")
        click.echo("Please configure these in your .env file")
    else:
        click.echo("All required environment variables are configured!")

@cli.command()
def full_setup():
    """
    Run complete setup process
    """
    click.echo("Running full setup...")
    
    ctx = click.get_current_context()
    
    ctx.invoke(install_dependencies)
    ctx.invoke(setup_database)
    ctx.invoke(compile_contracts)
    ctx.invoke(build_frontend)
    ctx.invoke(check_environment)
    
    click.echo("Full setup completed successfully!")

if __name__ == '__main__':
    cli()
