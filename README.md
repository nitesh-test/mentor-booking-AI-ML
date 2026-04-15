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

## Run the assessment pipeline

This project includes a trigger-style pipeline that:
- analyzes student quiz performance by topic,
- clusters students by performance profile,
- recommends remediation courses for weak topics.

Use the Python API:

```python
from mentor_booking_ai_ml import run_assessment_pipeline

course_map = {
    "Factoring": "Factoring Foundations",
    "Roots": "Roots Refresher",
    "Vertex": "Vertex Basics",
    "Discriminant": "Discriminant Practice",
    "Graphing": "Graphing Essentials",
}

result = run_assessment_pipeline(
    "data/questions.csv",
    "data/question_metadata.csv",
    "data/student_responses.csv",
    course_map,
    threshold=60.0,
    n_clusters=3,
)

print(result["strong_weak_by_student"]["S1"])
```

Quick command-line one-liner:

```bash
python -c "from mentor_booking_ai_ml import run_assessment_pipeline; cm={'Factoring':'Factoring Foundations','Roots':'Roots Refresher','Vertex':'Vertex Basics','Discriminant':'Discriminant Practice','Graphing':'Graphing Essentials'}; r=run_assessment_pipeline('data/questions.csv','data/question_metadata.csv','data/student_responses.csv',cm); print(r['strong_weak_by_student']['S1'])"
```

## Project Structure

```
.
├── src/
│   └── mentor_booking_ai_ml/
│       ├── __init__.py
│       └── example.py
├── tests/
│   └── test_example.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

The `src` directory contains the Python package with initial code.
