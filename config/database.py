import os
from dotenv import load_dotenv

load_dotenv()

def get_main_driver():
    return os.getenv('DB_CONNECTION', 'mysql')

connections = {
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '3306'),
        'database': os.getenv('DB_DATABASE', 'forge'),
        'username': os.getenv('DB_USERNAME', 'forge'),
        'password': os.getenv('DB_PASSWORD', ''),
    },
    'pgsql': {
        'driver': 'pgsql',
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '5432'),
        'database': os.getenv('DB_DATABASE', 'forge'),
        'username': os.getenv('DB_USERNAME', 'forge'),
        'password': os.getenv('DB_PASSWORD', ''),
    }
}

def get_connection():
    return connections[get_main_driver()]



