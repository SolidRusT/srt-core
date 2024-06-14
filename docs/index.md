# Welcome to srt-core Documentation

Welcome to the official documentation for `srt-core`, a powerful and flexible configuration management library designed by SolidRusT Networks. This library is essential for managing configurations in SolidRusT projects, offering seamless integration with YAML files and environment variables, and supporting multiple language model providers.

![SolidRusT Networks](https://solidrust.net/images/android-chrome-192x192.png)

## Overview

`srt-core` provides a robust system for loading and managing configurations, making it easier to handle application settings dynamically and efficiently. Whether you need to configure logging, manage API keys, or handle complex persona configurations, `srt-core` has you covered.

### Key Features

- **Dynamic Configuration Loading**: Load settings from YAML files and override them with environment variables.
- **Flexible Logging**: Set up advanced logging configurations with support for multiple logging levels.
- **Support for Multiple LLM Providers**: Easily manage configurations for various language model providers.
- **Error Handling**: Robust error handling to ensure smooth operation even with missing or incomplete configurations.
- **Extensible**: Easily extendable to fit the specific needs of your projects.

## Getting Started

To get started with `srt-core`, follow these steps:

1. **Installation**: Install the package using pip.

    ```sh
    pip install srt-core
    ```

2. **Configuration**: Create a `config.yaml` file in the root of your project. You can use the example configuration provided in `config-example.yaml`.

3. **Set Environment Variables**: Set necessary environment variables to customize your configurations.

### Example Usage

#### Config Class

```python
from srt_core.config import Config

# Initialize the config
config = Config()

# Access various configuration variables
print(config.server_name)
print(config.default_llm_name)
print(config.openai_compatible_api_key)
print(config.huggingface_api_key)
```

#### Logger Class

```python
from srt_core.utils.logger import Logger

# Initialize the logger
logger = Logger()

# Example of logging messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
```

For detailed configuration options and examples, please refer to the [Configuration](config.md) and [Logger](logger.md) documentation pages.

## Configuration

The `Config` class provides a robust system for loading configurations from YAML files and environment variables. It includes default values, error handling, and dynamic reloading capabilities.

Learn more on the [Configuration](config.md) page.

## Logger

The `Logger` class sets up logging based on a YAML configuration file and environment variables. It supports various logging levels and is highly customizable.

Explore its features on the [Logger](logger.md) page.

## Documentation Structure

- **[Home](index.md)**: This introduction and overview.
- **[Configuration](config.md)**: Detailed documentation on the `Config` class and its usage.
- **[Logger](logger.md)**: Comprehensive guide on using the `Logger` class.

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository on GitHub.
2. Create a new branch with your changes.
3. Submit a pull request for review.

For more details on how to contribute, see the [GitHub repository](https://github.com/SolidRusT/srt-core).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/SolidRusT/srt-core/blob/main/LICENSE) file for details.

## Contact

For any inquiries or support, please contact [Suparious](mailto:suparious@solidrust.net).

## Social

Stay updated by following us on [GitHub](https://github.com/SolidRusT/srt-core).

---

Copyright &copy; 2024 SolidRusT Networks
