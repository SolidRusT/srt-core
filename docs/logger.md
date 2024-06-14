# Logger

## Overview

The `Logger` class in `srt-core` sets up logging based on a YAML configuration file and environment variables.

## Usage

Here is an example of how to use the `Logger` class:

```python
from srt_core.utils.logger import Logger

# Initialize the logger
logger = Logger()

# Example of logging a message
import logging

logging.info("This is an info message.")
logging.debug("This is a debug message.")
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
