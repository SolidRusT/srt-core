import os
import yaml

class Config:
    def __init__(self):
        # Load configuration from yaml file
        with open("config.yaml", "r") as stream:
            self.config = yaml.safe_load(stream)

        # Check for 'debugging' variable in yaml
        self.debug = self.config.get("debug", False)

        # From environment variables
        self.persona_name = os.environ.get("PERSONA", "Default")
        self.server_port = int(os.environ.get("PORT", 8650))
        self.server_name = os.environ.get("SERVER_NAME", "0.0.0.0")

        # Load provider configuration
        self.default_llm_name = self.get_first_existing_value(
            ["llm_default", "llms.default"], "default"
        )
        self.summary_llm_name = self.get_first_existing_value(
            ["llm_summary", "llms.summary"], "summary"
        )
        self.chat_llm_name = self.get_first_existing_value(
            ["llm_chat", "llms.chat"], "default"
        )
        self.load_provider_settings()

        # Load Agent Tools
        self.load_tools_config()
        self.load_embeddings_llm()

        # Load persona specific settings
        self.load_persona_settings()

    def get_first_existing_value(self, keys, default_value):
        for key in keys:
            parts = key.split(".")
            value = self.config
            try:
                for part in parts:
                    value = value[part]
                return value
            except KeyError:
                continue
        return default_value

    def load_llm_settings(self, llm_name):
        llm_config = self.config["llms"][llm_name]
        return {
            "type": llm_config["type"],
            "filename": llm_config["filename"],
            "huggingface": llm_config["huggingface"],
            "url": llm_config["url"],
            "agent_provider": llm_config["agent_provider"],
            "server_name": llm_config["server"],
            "max_tokens": llm_config["max_tokens"],
        }

    def set_llm_attributes(self, llm_prefix, llm_settings):
        setattr(self, f"{llm_prefix}_llm_type", llm_settings["type"])
        setattr(self, f"{llm_prefix}_llm_filename", llm_settings["filename"])
        setattr(self, f"{llm_prefix}_llm_huggingface", llm_settings["huggingface"])
        setattr(self, f"{llm_prefix}_llm_url", llm_settings["url"])
        setattr(self, f"{llm_prefix}_llm_agent_provider", llm_settings["agent_provider"])
        setattr(self, f"{llm_prefix}_llm_server_name", llm_settings["server_name"])
        setattr(self, f"{llm_prefix}_llm_max_tokens", llm_settings["max_tokens"])

    def load_provider_settings(self):
        self.default_llm_settings = self.load_llm_settings(self.default_llm_name)
        self.summary_llm_settings = self.load_llm_settings(self.summary_llm_name)
        self.chat_llm_settings = self.load_llm_settings(self.chat_llm_name)

        self.set_llm_attributes('default', self.default_llm_settings)
        self.set_llm_attributes('summary', self.summary_llm_settings)
        self.set_llm_attributes('chat', self.chat_llm_settings)

    def load_embeddings_llm(self):
        self.embeddings_llm = self.get_first_existing_value(
            ["llm_embeddings", "llms.embeddings"], "BAAI/bge-small-en-v1.5"
        )
        self.embedding_model = self.config["llm_embeddings"]

    def load_tools_config(self):
        self.tokens_per_summary = self.config["tokens_per_summary"]
        self.tokens_search_results = self.config["tokens_search_results"]
        self.number_of_search_results = self.config["number_of_search_results"]

    def load_persona_settings(self):
        persona = self.config["personas"][self.persona_name]
        self.persona_ui_theme = persona["theme"]
        self.persona_full_name = persona["name"]
        self.persona_app_title = persona["title"]
        self.persona_avatar_image = f"images/{persona['avatar']}"
        self.persona_description = persona["description"]
        self.persona_system_message = persona["system_message"]
        self.persona_prompt_message = persona["persona"]
        self.persona_topic_examples = persona["topic_examples"]
        self.persona_temperature = persona["temperature"]
        self.persona_preferences = persona["preferences"]

config = Config()
