# Mentor Booking AI/ML

Initial scaffolding for the Mentor Booking AI/ML project.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest
```

## Project Structure

```
.
├── src/
│   └── mentor_booking_ai_ml/
│       ├── __init__.py
│       ├── assessment.py
│       ├── datasets.py
│       └── example.py
├── scripts/
│   └── generate_quadratic_dataset.py
├── tests/
│   ├── conftest.py
│   ├── test_assessment.py
│   ├── test_datasets.py
│   └── test_example.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

The `datasets.generate_dataset` function can be used to recreate example CSV
files for experimentation; tests generate these files in a temporary directory
at runtime.
