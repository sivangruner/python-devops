# TextAnalyzer Project

This is a **test project** designed for educational purposes to practice Python packaging and DevOps automation.

## Getting Started

**Fork this repository** to your GitHub account and work on your fork. Your final solution should be a link to your completed fork repository containing all the implemented tasks.

## Project Structure

```
new-devops-task/
├── README.md                   # This file
├── text_analyzer/             # Main package directory
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt       # Dependencies (to be replaced)
│   ├── setup.py              # Setup script (to be replaced)
│   └── TextAnalyzer/         # Package source code
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── analyzer.py   # Main TextAnalyzer class
│       ├── utils/
│       │   ├── __init__.py
│       │   └── text_ops.py   # Text processing utilities
│       └── config/
│           ├── __init__.py
│           └── settings.py   # Configuration management
└── test_script/              # Testing environment
    └── main.py              # Test script
```

## Tasks

This project is designed to help you practice modern Python packaging and DevOps automation. Complete the following tasks in order:

### Task 1: Build a Wheel Package

1. Fix any missing dependencies in the package configuration
2. Build a wheel (pip) package using `uv` (https://docs.astral.sh/uv/)

### Task 2: Create UV Virtual Environment And Test the Package

1. Navigate to the `test_script/` directory
2. Create a virtual environment and install the package you built earlier
3. Run `main.py` to verify the package works correctly
   
   **Note:** The `main.py` file should remain unchanged (except for code formatting if needed)

### Task 3: Modernize Package Configuration

1. Replace `requirements.txt` and `setup.py` in `text_analyzer/` with a modern `pyproject.toml` file.

### Task 4: Setup Pre-commit with Ruff

1. Create a `.pre-commit-config.yaml` and run pre-commit hooks for the entire repo and fix any code formatting issues

### Task 5: Automate with Taskfile

1. Create a `Taskfile.yml` in `text_analyzer/`
2. Implement the following tasks:
   ```bash
   task lint          # Run pre-commit hooks (ruff, formatting)
   task clean         # Clean build artifacts
   task build ver=1.2.3  # Build package with specified version
   task test          # Install and test the test_script main.py
   ```

### Task 6: Create CI/CD Pipeline with Jenkins

1. Create a `Jenkinsfile` in `text_analyzer/CI/`
2. Configure pipeline to trigger on semantic version tags (e.g., v1.2.3)
3. Pipeline should use Taskfile to verify code format, build the package, and then run the main.py after installing the packge.
   The pipeline needs to run automatically when a new semantic versioning (SemVer) tag is created, and it must validate that the tag's format is correct.

### Task 7: Containerize with Docker

1. Create a `Dockerfile` in `text_analyzer/`
2. Build a Docker image that installs the TextAnalyzer package and runs the test_script
3. Add Docker tasks to your `Taskfile.yml`:
   ```bash
   task docker:build     # Build Docker image
   task docker:run       # Run container and execute tests
   task docker:clean     # Remove Docker artifacts
   ```

### Task 8 (Extra): Local Jenkins with Docker Compose

1. Create a `docker-compose.yml` in the project root
2. Set up Jenkins server with:
   - Required plugins (Pipeline, Git)
3. Configure Jenkins to:
   - Connect to your GitHub repository
   - Load the Jenkinsfile from `text_analyzer/CI/`
   - Trigger on git tags (semantic versioning)
4. Add Jenkins tasks to your `Taskfile.yml`:
   ```bash
   task jenkins:up       # Start Jenkins server
   task jenkins:down     # Stop Jenkins server
   task jenkins:logs     # View Jenkins logs
   ```

## Submission

Your completed solution should be a **link to your forked GitHub repository** containing:
- All implemented tasks
- Working code and configuration files
- Documentation of any issues encountered and how you resolved them

## Evaluation Criteria

- ✅ All tasks completed successfully
- ✅ Code quality and best practices
- ✅ Working CI/CD pipeline
- ✅ Proper documentation
- ✅ Creative solutions to challenges
