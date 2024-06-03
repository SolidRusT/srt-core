# Development Workflow

Setup your environment

```bash
git clone https://github.com/SolidRusT/srt-core.git
cd srt-core
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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
