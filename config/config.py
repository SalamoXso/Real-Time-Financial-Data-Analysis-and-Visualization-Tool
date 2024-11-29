import os
import yaml
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    def __init__(self, environment='development'):
        self.environment = environment
        self.settings = self.load_settings()

    def load_settings(self):
        config_path = f'config/settings/{self.environment}_config.yaml'
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def get(self, key, default=None):
        return self.settings.get(key, os.getenv(key, default))

# Instantiate the Config class
config = Config(environment=os.getenv('FLASK_ENV', 'development'))
