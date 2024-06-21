import os

bind = "0.0.0.0:{}".format(os.environ.get("PORT", 3000))  # Bind to all interfaces and extracted port
workers = 3  # Adjust the number of worker processes as needed

# Optional configurations (refer to Gunicorn documentation for details):
# accesslog = "-"  # Log to standard output
# errorlog = "-"  # Log errors to standard output
# log_level = "info"  # Set logging level

# The application object to be used by Gunicorn
wsgi_app = "Main:app"
