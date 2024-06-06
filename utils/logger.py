import os
import yaml
import logging

class Logger:
    def __init__(self):
        # Load configuration from yaml file
        with open("config.yaml", "r") as stream:
            self.config = yaml.safe_load(stream)

        # Check for 'debugging' variable in yaml
        self.debug = self.config.get("debug", False)

        # Get persona name from environment variables
        self.persona_name = os.environ.get("PERSONA", "Default")
        
        # Setup logging
        self.setup_logging()        

    def setup_logging(self):
        log_level = logging.DEBUG if self.debug else logging.INFO
        logs_path = self.config["logs_path"]
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
        persona = self.config["personas"][self.persona_name]
        persona_full_name = persona["name"]
        
        logging.basicConfig(
            filename=f"{logs_path}/client-chat-{persona_full_name}.log",
            level=log_level,
            format="%(asctime)s:%(levelname)s:%(message)s",
        )

logger = Logger()
