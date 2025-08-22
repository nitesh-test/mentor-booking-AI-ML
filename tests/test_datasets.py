import csv

def test_questions_csv_structure(dataset_dir):
    path = dataset_dir / "questions.csv"
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
        rows = list(reader)
        assert len(rows) == 50
        assert rows[0]["question_id"] == "Q1"


def test_question_metadata_csv_structure(dataset_dir):
    path = dataset_dir / "question_metadata.csv"
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
        rows = list(reader)
        assert len(rows) == 50
        assert rows[0]["topic"] == "Quadratic Equations"


def test_student_responses_csv_structure(dataset_dir):
    path = dataset_dir / "student_responses.csv"
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
        rows = list(reader)
        assert len(rows) == 50 * 50
        assert rows[0]["student_id"] == "S1"
