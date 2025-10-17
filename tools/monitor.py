"""
International Plebeian Academy - Monitoring Tool
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

import os
import sys
import time
import click
import psutil
import requests
from datetime import datetime

@click.group()
def cli():
    """
    International Plebeian Academy Monitoring Tools
    """
    pass

@cli.command()
@click.option('--interval', default=5, help='Monitoring interval in seconds')
def system_health(interval):
    """
    Monitor system health continuously
    """
    click.echo(f"Monitoring system health (interval: {interval}s)")
    click.echo("Press Ctrl+C to stop")
    
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            click.echo(f"\n[{timestamp}]")
            click.echo(f"CPU: {cpu_percent}%")
            click.echo(f"Memory: {memory.percent}% ({memory.used / (1024**3):.2f}GB / {memory.total / (1024**3):.2f}GB)")
            click.echo(f"Disk: {disk.percent}% ({disk.used / (1024**3):.2f}GB / {disk.total / (1024**3):.2f}GB)")
            
            time.sleep(interval)
    except KeyboardInterrupt:
        click.echo("\nMonitoring stopped")

@cli.command()
@click.option('--url', default='http://localhost:8000', help='Backend URL')
def check_backend(url):
    """
    Check backend service status
    """
    click.echo(f"Checking backend at {url}...")
    
    try:
        response = requests.get(f"{url}/api/health", timeout=5)
        
        if response.status_code == 200:
            click.echo("✓ Backend is healthy")
            data = response.json()
            click.echo(f"  CPU: {data.get('cpu', {}).get('percent', 'N/A')}%")
            click.echo(f"  Memory: {data.get('memory', {}).get('percent', 'N/A')}%")
        else:
            click.echo(f"✗ Backend returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        click.echo(f"✗ Backend is unreachable: {e}")

@cli.command()
@click.option('--url', default='http://localhost:3000', help='Frontend URL')
def check_frontend(url):
    """
    Check frontend service status
    """
    click.echo(f"Checking frontend at {url}...")
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            click.echo("✓ Frontend is accessible")
        else:
            click.echo(f"✗ Frontend returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        click.echo(f"✗ Frontend is unreachable: {e}")

@cli.command()
@click.option('--url', default='http://localhost:8545', help='Blockchain node URL')
def check_blockchain(url):
    """
    Check blockchain node status
    """
    click.echo(f"Checking blockchain node at {url}...")
    
    try:
        response = requests.post(
            url,
            json={
                "jsonrpc": "2.0",
                "method": "eth_blockNumber",
                "params": [],
                "id": 1
            },
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            block_number = int(data.get('result', '0x0'), 16)
            click.echo("✓ Blockchain node is running")
            click.echo(f"  Block Number: {block_number}")
        else:
            click.echo(f"✗ Blockchain node returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        click.echo(f"✗ Blockchain node is unreachable: {e}")

@cli.command()
def check_all_services():
    """
    Check all services status
    """
    click.echo("Checking all services...\n")
    
    ctx = click.get_current_context()
    
    ctx.invoke(check_frontend)
    click.echo()
    
    ctx.invoke(check_backend)
    click.echo()
    
    ctx.invoke(check_blockchain)

@cli.command()
def view_logs():
    """
    View Docker container logs
    """
    click.echo("Viewing container logs...")
    
    import subprocess
    
    subprocess.run([
        'docker-compose',
        '-f', '../infrastructure/docker-compose.yml',
        'logs', '--tail=100', '-f'
    ])

if __name__ == '__main__':
    cli()
