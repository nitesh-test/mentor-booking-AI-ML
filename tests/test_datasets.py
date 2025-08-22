import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def test_questions_csv_structure():
    path = DATA_DIR / "questions.csv"
    with path.open() as f:
        reader = csv.DictReader(f)
        assert set(reader.fieldnames) == {
            "question_id",
            "content",
            "correct_answer",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
        }
        first = next(reader)
        assert first["question_id"] == "Q1"


def test_question_metadata_csv_structure():
    path = DATA_DIR / "question_metadata.csv"
    with path.open() as f:
        reader = csv.DictReader(f)
        assert set(reader.fieldnames) == {
            "question_id",
            "topic",
            "sub_topics",
            "difficulty",
            "marks",
            "question_type",
        }
        first = next(reader)
        assert first["topic"] == "Biology"


def test_student_responses_csv_structure():
    path = DATA_DIR / "student_responses.csv"
    with path.open() as f:
        reader = csv.DictReader(f)
        assert set(reader.fieldnames) == {
            "student_id",
            "question_id",
            "student_response",
            "correct_answer",
            "time_taken_sec",
            "is_correct",
        }
        first = next(reader)
        assert first["student_id"] == "S1"
