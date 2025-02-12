# flask_basic_app
Basic Web Application with Flask


# Setup Python Project using UV

1. Install UV, a Python project manager
2. Install Python version and create project

```bash
uv python install <VERSION> --path <PATH TO INSTALL>
uv init <NAME OF PROJECT>
```

3. Create Environment
```bash
uv venv --python 3.13
```

4. Activate Environment
```bash
.venv\Scripts\activate
```

5. Add packages
```bash
uv add <PACKAGE NAME>	
```

6. Run Python script:
```bash
uv run <PYTHON SCRIPT NAME>
```

To check that the package added have the correct version and dependencies:

```bash
uv sync
```

Remove package:
```bash
uv remove <PACKAGE NAME>
```


## Install dependencies from pyproject.toml

```bash
uv pip install -r pyproject.toml --all-extras
```

## Running Flask

Pass Argument to Flask executable
```bash
flask --app app --debug run
```

This also can be done by exporting the settings manually:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

- Run Flask
```bash
flask run
```