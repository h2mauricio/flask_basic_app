# flask_basic_app
Basic Web Application with Flask

# Introduction
This application is a basic web application that uses Flask to create a web server. The application has a two single routes. One of the routes returns a simple string, while the other returns a JSON object.


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
After installing the dependencies, the Flask application can be run. The Flask application can be executed using the following command:


```bash

flask --app app --debug run
```
, where:
- --app: Identifies the Python file to run (which is called in this example app.py), and 
- --debug: Run the server in debug mode

This also can be done by exporting the settings manually (In Windows use `set` instead of `export`) :
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

- Run Flask
```bash
flask run
```

## Returning JSON
- Test in command line return a serialized object as JSON
```bash
curl -X GET -i localhost:5000
curl -X GET -i localhost:5000/json
```

## Optional
Reduce the size of the command prompt (in Windows use set instead of export):
```bash
export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$"
```