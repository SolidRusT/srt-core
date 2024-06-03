# Contributing to srt-core

Thank you for your interest in contributing to `srt-core`! This document outlines the process for testing the `Config` class and publishing changes to PyPI.

## Testing the `Config` Class

To ensure the `Config` class works correctly, follow these steps:

1. **Set up your development environment**:

   ```sh
   git clone https://github.com/SolidRusT/srt-core.git
   cd srt-core
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   pip install -e .
   ```

2. **Create a `config.yaml` file**:

   Ensure you have a `config.yaml` file in the root of your project with the necessary configuration.

3. **Set the required environment variables**:

   ```sh
   export PERSONA='Default'
   export PORT=8650
   export SERVER_NAME='0.0.0.0'
   ```

4. **Run the tests**:

   We use `unittest` for testing. Ensure your `tests/test_config.py` file contains meaningful tests for the `Config` class.

   ```sh
   python -m unittest discover tests
   ```

## Publishing Changes to PyPI

To publish changes to PyPI, follow these steps:

1. **Update version number**:

   Update the version number in `setup.py` to reflect the new version.

2. **Build the package**:

   Ensure you have the latest versions of `setuptools` and `wheel` installed.

   ```sh
   python -m pip install --upgrade setuptools wheel
   python setup.py sdist bdist_wheel
   ```

3. **Upload to PyPI**:

   Ensure you have `twine` installed.

   ```sh
   python -m pip install --upgrade twine
   twine upload dist/*
   ```

   You will be prompted to enter your PyPI username and password.

## Additional Guidelines

- **Branching**: Use descriptive names for your branches, such as `feature/new-feature` or `bugfix/issue-number`.
- **Pull Requests**: Submit pull requests with clear descriptions of the changes and related issues.
- **Code Style**: Follow PEP 8 guidelines for Python code style.

We appreciate your contributions and efforts to improve `srt-core`!

## Contact

For any inquiries or support, please contact [Suparious](mailto:suparious@solidrust.net).
