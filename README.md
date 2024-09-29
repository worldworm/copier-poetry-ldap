<h1 align="center">📋 copier-poetry-ldap</h1>
<p align="center">
  <i><a href="https://github.com/copier-org/copier">Copier</a> template for <a href="https://github.com/python-poetry/poetry">poetry</a>-<a href="https://github.com/cannatag/ldap3">ldap</a> projects.</i>
</p>


<!-- Place https://shields.io/ badges here -->
[![GitHub repo stars](https://img.shields.io/github/stars/worldworm/copier-poetry-ldap)](https://github.com/worldworm/copier-poetry-ldap)
[![License](https://img.shields.io/badge/license-MIT-green?logo=opensourceinitiative&logoColor=fff)](https://github.com/worldworm/copier-poetry-ldap/blob/main/LICENSE)
[![GitHub last commit (main)](https://img.shields.io/github/last-commit/worldworm/copier-poetry-ldap/main)](https://github.com/worldworm/copier-poetry-ldap/commits/main/)
[![GitHub release](https://img.shields.io/github/v/release/worldworm/copier-poetry-ldap)](https://github.com/worldworm/copier-poetry-ldap/releases/latest)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/worldworm/copier-poetry-ldap/latest/main)](https://github.com/worldworm/copier-poetry-ldap/releases/latest)
[![Copier supported version](https://img.shields.io/badge/Copier-v9-blue)](https://github.com/copier-org/copier)


## Features
- 🌐 [LDAP3](https://github.com/cannatag/ldap3) (pool) connection setup
- 🛠 LDAP helper utilities
- ⚙️ Settings management using [pydantic-settings](https://github.com/pydantic/pydantic-settings)
- 📚 Logging powered by [loguru](https://github.com/Delgan/loguru)
- 🧪 Predefined [pytest](https://github.com/pytest-dev/pytest/) testing with LDAP3 mock connection
- 📦 [Poetry](https://github.com/python-poetry/poetry) setup with a pre-defined pyproject.toml
- 🔄 Continuous integration (CI) pipelines for Github Actions and GitLab CI/CD
- 🐳 Docker support with build and publish pipelines
- 🔗 [pre-commit](https://github.com/pre-commit/pre-commit) hooks
- 📝 [pylint](https://github.com/pylint-dev/pylint) code linter
- 💻 [VSCode](https://github.com/microsoft/vscode) configuration


## Requirements
First install copier:<br>
([from the official installation documentation](https://copier.readthedocs.io/en/stable/#installation))
```bash
pip install copier
```


## Usage

Make sure the requirements are met, then:
```bash
copier copy --trust "https://github.com/worldworm/copier-poetry-ldap.git" .
```

### Update
To update a template after creating a project, run:
```bash
copier update --trust -a .project/.copier-answers.poetry-ldap.yml .
```


## Explore more Copier templates
In addition to this template, there are a number of other Copier templates available. For an overview of all available templates, visit the [Templates Showcase repository](https://github.com/worldworm/copier-showcase).

---
<p align="center">
  <i>© <a href="https://github.com/worldworm">worldworm</a> 2023</i>
  <br><i>Licensed under <a href="https://github.com/worldworm/copier-poetry-ldap/blob/main/LICENSE">MIT</a></i>
</p>
