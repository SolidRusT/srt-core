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

        self.debugging = self.config.get("debugging", False)
        self.persona_name = os.environ.get("PERSONA", "Default")

    def setup_logging(self):
        """Setup logging based on the configuration."""
        log_level = logging.DEBUG if self.debugging else logging.INFO
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

        self.logger = logging.getLogger(persona_full_name)

    def log(self, level, message):
        """Log a message with a given severity level."""
        self.logger.log(level, message)

    def debug(self, msg, *args, **kwargs):
        """Log a message with severity 'DEBUG'."""
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """Log a message with severity 'INFO'."""
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Log a message with severity 'WARNING'."""
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """Log a message with severity 'ERROR'."""
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """Log a message with severity 'CRITICAL'."""
        self.logger.critical(msg, *args, **kwargs)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
