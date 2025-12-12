"""
Production Configuration
Placeholder for production-specific settings
"""

import os

class ProductionConfig:
    """Production configuration settings"""
    
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = os.getenv('SECRET_KEY', '******')
    API_KEY = os.getenv('PRODUCTION_API_KEY', '******')
    
    DATABASE_URL = os.getenv('PRODUCTION_DATABASE_URL', '******')
    REDIS_URL = os.getenv('PRODUCTION_REDIS_URL', '******')
    
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', '/var/log/app.log')
    
    RATE_LIMIT_ENABLED = True
    RATE_LIMIT_PER_MINUTE = 60
    
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '******').split(',')
    
    MONITORING_ENABLED = True
    MONITORING_ENDPOINT = os.getenv('MONITORING_ENDPOINT', '******')
    
    BACKUP_ENABLED = True
    BACKUP_SCHEDULE = os.getenv('BACKUP_SCHEDULE', '******')
    
    SSL_ENABLED = True
    SSL_CERT_PATH = os.getenv('SSL_CERT_PATH', '******')
    SSL_KEY_PATH = os.getenv('SSL_KEY_PATH', '******')

