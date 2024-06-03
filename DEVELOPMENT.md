# Development Workflow

Setup your environment

```bash
git clone https://github.com/SolidRusT/srt-core.git
cd srt-core
mkdir -p ~/venvs
python -m venv ~/venvs/venv-srt-core-dev
source ~/venvs/venv-srt-core-dev/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
pip install -e .
```

Run the tests

```bash
python -m unittest discover tests
```

Build the package

```bash
python setup.py sdist bdist_wheel
```

Upload to PyPI

```bash
twine upload dist/*
```
