import os
import re
from os import environ

# Load environment variables
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

# Regex pattern to validate admin IDs
id_pattern = re.compile(r'^(\d+)$')

# Load admin IDs from environment variables and validate them
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
