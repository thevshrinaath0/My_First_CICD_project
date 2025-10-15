# CI/CD Automation with Python and Makefile

## 📘 Overview
A simple project that demonstrates Continuous Integration and Deployment (CI/CD) workflows using Python and Makefile.

## ⚙️ Features
- Automated installation, linting, formatting, testing, and refactoring
- Click-based CLI app (`add` and `subtract` commands)
- Automated tests using Pytest and Click Test Runner
- Dockerfile linting and deploy placeholder

## 🧩 Makefile Commands
| Command | Description |
|----------|--------------|
| `make install` | Install dependencies |
| `make lint` | Check code style issues |
| `make format` | Format code using Black |
| `make test` | Run tests with coverage |
| `make refactor` | Run both lint + format |
| `make deploy` | Placeholder for deployment |

## 🧪 Running the CLI
```bash
./main.py add 2 3
./main.py subtract 5 2
