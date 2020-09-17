# Module Import
import mariadb
import sys
import os

# Pull defaults from OS environment if they exist
user = os.environ.get('MARIADB_USER', 'connpy_test')
password = os.environ.get('MARIADB_PASS', 'passwd')
host = os.environ.get('MARIADB_HOST', 'localhost')
port = int(os.environ.get('MARIADB_PORT', 3306))

# Instantiate Connection
try:
   conn = mariadb.connect(
      user=user,
      password=password,
      host=host,
      port=port)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)