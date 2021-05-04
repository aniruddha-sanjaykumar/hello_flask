import sys
import site

site.addsitedir('/var/www/venv/lib/python3.6/site-packages')

sys.path.insert(0, '/var/www/hello_flask')

from app import app as application
