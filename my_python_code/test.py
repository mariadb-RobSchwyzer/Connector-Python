# Module Import
import mariadb
import sys
# Instantiate Connection
try:
   conn = mariadb.connect(
      user="connpy_test",
      password="passwd",
      host="localhost",
      port=3306)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)