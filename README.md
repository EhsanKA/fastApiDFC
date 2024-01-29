# Delivery Fee Calculator

[![Test Status](https://github.com/EhsanKA/fastApiDFC/actions/workflows/main.yaml/badge.svg)](https://github.com/EhsanKA/fastApiDFC/actions/workflows/main.yaml)

This project is an implementation of the assignment for the [Wolt Software (Backend) 2024 Summer Internship](https://github.com/woltapp/engineering-internship-2024). It includes a delivery fee calculation service built with FastAPI and is designed to showcase best practices in code quality, maintainability, and testing.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python 3.8+ installed on your system. You can check your Python version by running:

```bash
python --version
```

### Installation

1. Clone the repo

```bash
git clone https://github.com/EhsanKA/fastApiDFC.git
cd fastApiDFC
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Running the Application
To run the FastAPI application locally, use the following command:

```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000/orders/` or to have it tested, use `http://127.0.0.1:8000/docs/`.

### Environment Setup
Before running the tests, set the `PYTHONPATH` environment variable to ensure the test framework can locate all necessary project files.

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/your/project
```
Replace `/path/to/your/project` with the actual path to your project directory.

### Running Tests
Navigate to the tests directory and run the tests using `pytest`:


```bash
cd tests
pytest unit_test.py
pytest integration_test.py
```

### CI/CD Integration
Our project uses GitHub Actions for Continuous Integration and Continuous Deployment, ensuring that every change is automatically tested and stable before being merged into the master branch.

The CI/CD pipeline is defined in the [`.github/workflows/main.yaml`](https://github.com/EhsanKA/fastApiDFC/actions/workflows/main.yaml) file. This workflow triggers on every push to the master branch


## Contact
Ehsan Karimiara 
- [@ehsan-ka](https://www.linkedin.com/in/ehsan-ka/) on Linkedin 
- E.karimiara@gmail.com
- [@EhsanKA](https://github.com/EhsanKA) on Github