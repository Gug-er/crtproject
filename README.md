# 📂 crtproject

`crtproject` is a simple Python CLI tool for generating projects from templates.

With `crtproject`, you can quickly create project structures for **APIs, CLI tools, libraries**, or any custom template.

---

## ⚡ Features

- Generate a new project from a template with a single command
- Supports multiple project types: API, basic
- Simple and clean code structure
- Editable mode installation (`pip install -e .`) for active development

---

## 📦 Installation

1. Clone the repository or download the project:

```bash
git clone <https://github.com/Gug-er/crtproject.git>
cd crtproject
```

2. Install the package in editable mode:

```bash
pip install -e .
```

Now the `crtproject` command is available in your terminal.

⚠️ On Windows, make sure the Python\Scripts folder is added to your PATH.

## 🚀 Usage
⚠️ In `cli.py` change path to your already existing directory 
Syntax:

```bash
crtproject <template> <project_name>
```

## 📂 Template Structure

Templates are located inside the templates/ folder:

```
templates/
├── api/
├── cli/
└── basic/
```

Each template contains a project structure that will be copied to the new project folder.

## 🛠 Adding a New Template
1. Create a new folder in `templates/`, e.g., `bot/`
2. Add your template project structure inside
3. Generate a new project with your template:
```bash
crtproject bot MyBot
```

## 📜 Project Architecture
`cli.py` — CLI entry point, handles arguments\
`generator.py` — Main logic for generating projects and replacing variables\
`templates/` — Project template folders\
`pyproject.toml` — Project configuration and CLI command registration

## crtproject

![Python](https://img.shields.io/badge/python-3.14-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
