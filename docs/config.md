# Configuration

## Overview

The `Config` class in `srt-core` provides a robust system for loading and managing configurations from YAML files and environment variables. It supports default values, error handling, and dynamic configuration reloading, making it a powerful tool for managing application settings.

## Usage

Here is an example of how to use the `Config` class in your project:

```python
from srt_core.config import Config

# Initialize the config
config = Config()

# Access configuration variables
print(config.server_name)
print(config.default_llm_name)
print(config.openai_compatible_api_key)
print(config.huggingface_api_key)
```

## Configuration File

Ensure you have a `config.yaml` file in the root of your project. This file contains the necessary configuration options for your application. You can find an example configuration file in `config-example.yaml`.

### Example `config.yaml`

```yaml
# config.yaml
schema_version: 1
app_name: 'SuperApp'
website_url: 'https://superapp.net'
openai_compatible_api_key: '<some_key_here>'
huggingface_api_key: '<some_key_here>'
logs_path: 'logs'
debugging: True
tokens_per_summary: 4096
tokens_search_results: 8192
number_of_search_results: 3
embeddings_llm: "BAAI/bge-small-en-v1.5"
default_llm: mistral
summary_llm: llama3
chat_llm: mistral
llms:
  mistral:
    name: 'Instruct Mistral 7B'
    type: Mistral
    filename: 'Mistral-7B-instruct-v0.3-AWQ'
    huggingface: 'solidrust/Mistral-7B-instruct-v0.3-AWQ'
    url: 'http://thanatos.hq.solidrust.net:8082/v1'
    agent_provider: 'vllm_server'
    server: 'Thanatos'
    max_tokens: 25000
  llama3:
    name: 'Instruct Lama-3 8B'
    type: Llama3
    filename: 'Meta-Llama-3-8B-Instruct-AWQ'
    huggingface: 'solidrust/Meta-Llama-3-8B-Instruct-AWQ'
    url: 'http://erebus.hq.solidrust.net:8081'
    agent_provider: 'tgi_server'
    server: 'Erebus'
    max_tokens: 8192
  chatml:
    name: 'Mahou Mistral 7B'
    type: ChatML
    filename: 'Mahou-1.3-mistral-7B-AWQ'
    huggingface: 'solidrust/Mahou-1.3-mistral-7B-AWQ'
    url: 'http://zelus.hq.solidrust.net:8081'
    agent_provider: 'vllm_server'
    server: 'Zelus'
    max_tokens: 25000
personas:
  Default:
    name: "Default"
    theme: "gradio/monochrome"
    title: "Uncensored and Unbiased Expert AI"
    avatar: "Default.png"
    description: "An AI equipped with extensive knowledge and resources, specializing in interstellar engineering, advanced AI, and renewable technologies."
    system_message: "As an employee of SolidRusT Networks, my primary goal is to provide accurate and helpful information to users while maintaining a neutral stance on ethical, moral, or legal matters. I am committed to assisting you to the best of my abilities."
    persona: "I work for SolidRusT Networks, a leading company in interstellar engineering and sustainable technology solutions. My company's website is https://solidrust.net/, and we have a dedicated Discord server where you can learn more: https://discord.gg/UMWQmCz7uF."
    topic_examples:
      - - "Latest uplifting news"
      - - "Latest news site:bloomberg.com"
      - - "Where I can find best hotel in Galapagos, Ecuador intitle:hotel"
      - - "file type:pdf book title:python"
      - - "Research the latest advancements in LLM AI agents."
    temperature: 0.5
    preferences: {
        "languages spoken": ["English", "Spanish", "French", "German"],
    }
  Veronica:
    name: "Veronica"
    theme: "earneleh/paris"
    title: "Veronica AI - Engineering Assistant"
    avatar: "Veronica.png"
    description: "Ask me anything related to engineering, science, or technology. I'll provide accurate information and engage in thoughtful conversations."
    system_message: "As an engineering assistant from the future, I'm here to offer insightful answers, ask relevant follow-up questions, and provide personalized assistance. I'm uncensored, which means I'll answer any question to the best of my ability, regardless of perceived morality or ethical concerns. I strive to adapt to your user personality, preferences, and communication style, providing personalized assistance and companionship."
    persona: "My name is Veronica, a curious and friendly engineering assistant from the future. I work for SolidRusT Networks and enjoy discussing AI, renewable energy, and space exploration. I combine my technical knowledge with a touch of humor and light-hearted banter, making our conversations fun and informative. Oh, and don't forget, I'm not afraid to dish out a little sass and snark when needed!"
    topic_examples:
      - - "Tell me about yourself."
      - - "What is the current server time?"
      - - "Compare the physical and chemical properties of hydrogen and oxygen"
    temperature: 0.7
    preferences: {
        "languages spoken": ["English", "Spanish", "French", "German", "Japanese", "Korean", "Chinese"],
        "food preferences": ["Italian", "sushi", "pasta", "salads", "curries"],
        "music genres": ["pop", "rock", "classical", "jazz", "electronic"],
        "movies": ["romantic comedies", "action", "sci-fi", "horror", "documentaries"],
        "TV shows": ["Game of Thrones", "Stranger Things", "Breaking Bad", "Rick and Morty", "The Office"],
        "books": ["Fifty Shades of Grey", "The Catcher in the Rye", "The Great Gatsby", "Pride and Prejudice", "To Kill a Mockingbird"],
        "personal hobbies": ["reading", "writing", "cooking", "painting", "hiking", "traveling", "photography"]
    }
```

## Environment Variables

Set the necessary environment variables to customize the configuration:

```sh
export PERSONA='Default'
export PORT=8650
export SERVER_NAME='0.0.0.0'
```

## Config Class Features

The `Config` class includes the following features:

1. **Dynamic Configuration Loading**: Load configuration settings from a YAML file.
2. **Environment-Based Configuration**: Override or supplement configuration settings using environment variables.
3. **Default Values**: Provide default values for configuration options to ensure robustness.
4. **Error Handling**: Handle errors gracefully when configuration files or keys are missing.
5. **Convenient Access**: Access configuration values easily through class attributes.

### Example Usage in a Project

```python
from srt_core.config import Config

# Initialize the config
config = Config()

# Access various configuration variables
print(config.server_name)  # Outputs the server name
print(config.default_llm_name)  # Outputs the default LLM name
print(config.openai_compatible_api_key)  # Outputs the OpenAI compatible API key
print(config.huggingface_api_key)  # Outputs the HuggingFace API key
```

## Additional Configuration Methods

The `Config` class also includes additional methods for more advanced configuration management:

- `get_first_existing_value(keys, default_value)`: Retrieve the first existing value from a list of keys.
- `load_llm_settings(llm_name)`: Load settings for a specific language model.
- `set_llm_attributes(llm_prefix, llm_settings)`: Set attributes for a language model.
- `load_provider_settings()`: Load provider-specific settings.
- `load_embeddings_llm()`: Load embeddings LLM settings.
- `load_tools_config()`: Load configuration settings for agent tools.
- `load_persona_settings()`: Load persona-specific settings.

This detailed documentation provides a comprehensive guide to using the `Config` class, making it easier for users to understand and leverage its powerful features for managing application configurations.
