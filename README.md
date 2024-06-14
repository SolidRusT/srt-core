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

To use the `Logger` class:

```python
from srt_core.utils.logger import Logger

logger = Logger()
```

Ensure you have a `config.yaml` file in the root of your project and set the necessary environment variables:

You can find an example configuration file in `config-example.yaml`.

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

For any inquiries or support, please contact [Suparious](mailto:suparious@solidrust.net).
