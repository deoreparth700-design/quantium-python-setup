# Quantium Software Engineering – Local Development Environment

This repository contains the local development environment setup completed as part of the Quantium Software Engineering Virtual Experience Program on Forage.

## Environment

- Python 3.9
- Virtual Environment (venv)

## Installed Packages

- dash
- pandas
- dash[testing]

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment (Windows):

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install dash
pip install pandas
pip install "dash[testing]"
```

Generate requirements:

```bash
pip freeze > requirements.txt
```

## Status

- Virtual environment created
- Required dependencies installed
- Repository ready for development
