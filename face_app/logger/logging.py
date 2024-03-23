import logging
import os
from datetime import datetime

# Define the directory for logs
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)

# Get the current timestamp
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Define the filename with the timestamp
log_filename = f'{current_time}.log'

# Configure the logging
logging.basicConfig(
    filename=os.path.join(logs_path, log_filename),
    format='[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Example usage
logging.info('This is a test log message.')
