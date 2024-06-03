# srt-core

SolidRusT Core Libraries

## Overview

`srt-core` provides essential configuration management utilities for SolidRusT projects. This package helps load configurations from YAML files and environment variables, and it supports multiple language model providers.

## Installation

To install the package, use pip:

```sh
pip install srt-core
```

## Usage

Here is an example of how to use the `Config` class in your project:

```python
from srt_core.config import Config

config = Config()

# Access configuration variables
print(config.server_name)
print(config.default_llm_name)
```

Ensure you have a `config.yaml` file in the root of your project and necessary environment variables set:

```yaml
debug: true
llms:
  default:
    type: 'some_type'
    filename: 'some_filename'
    huggingface: 'some_model'
    url: 'some_url'
    agent_provider: 'some_provider'
  # Add other LLM configurations here
personas:
  Default:
    theme: 'dark'
    name: 'Default User'
    title: 'User Title'
    avatar: 'avatar.png'
    description: 'Default user description'
    system_message: 'System message for Default user'
    persona: 'Persona message for Default user'
    topic_examples: 'Topic examples for Default user'
    temperature: 0.5
    preferences: 'User preferences'
tokens_per_summary: 100
tokens_search_results: 50
number_of_search_results: 5
logs_path: './logs'
```

Set the environment variables:

```sh
export PERSONA='Default'
export PORT=8650
export SERVER_NAME='0.0.0.0'
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [Your Name](mailto:suparious@solidrust.net).
