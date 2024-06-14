# Configuration

## Overview

The `Config` class in `srt-core` helps load configurations from YAML files and environment variables.

## Usage

Here is an example of how to use the `Config` class in your project:

```python
from srt_core.config import Config

config = Config()

# Access configuration variables
print(config.server_name)
print(config.default_llm_name)
```

## Configuration File

Ensure you have a `config.yaml` file in the root of your project. You can find an example configuration file in `config-example.yaml`.

## Environment Variables

Set the necessary environment variables:

```sh
export PERSONA='Default'
export PORT=8650
export SERVER_NAME='0.0.0.0'
```
