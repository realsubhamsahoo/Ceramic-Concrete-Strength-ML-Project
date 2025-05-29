import os
import yaml

class ConfigurationManager:
    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path
        self.config = self._read_yaml()

    def _read_yaml(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get(self, section: str):
        if section in self.config:
            return self.config[section]
        else:
            raise KeyError(f"Section '{section}' not found in config.yaml")
