import os
import yaml
import logging

class Logger:
    def __init__(self, config_path="config.yaml"):
        """
        Initialize the Logger class.
        
        Parameters:
        config_path (str): The path to the YAML configuration file.
        """
        self.config_path = config_path
        self.load_config()
        self.setup_logging()

    def load_config(self):
        """Load configuration from the YAML file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file {self.config_path} not found.")
        
        with open(self.config_path, "r") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                raise ValueError(f"Error reading YAML file: {e}")

        self.debug = self.config.get("debug", False)
        self.persona_name = os.environ.get("PERSONA", "Default")

    def setup_logging(self):
        """Setup logging based on the configuration."""
        log_level = logging.DEBUG if self.debug else logging.INFO
        logs_path = self.config.get("logs_path", "./logs")
        
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
        
        persona = self.config["personas"].get(self.persona_name, {})
        persona_full_name = persona.get("name", "Unknown")

        logging.basicConfig(
            filename=f"{logs_path}/client-chat-{persona_full_name}.log",
            level=log_level,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

# Example usage
if __name__ == "__main__":
    logger = Logger()
