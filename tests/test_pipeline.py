from pathlib import Path

from mentor_booking_ai_ml.pipeline import run_assessment_pipeline


def test_run_assessment_pipeline_outputs_expected_keys_and_student_data():
    data_dir = Path(__file__).resolve().parents[1] / "data"
    course_map = {
        "Factoring": "Factoring Foundations",
        "Roots": "Roots Refresher",
        "Vertex": "Vertex Basics",
        "Discriminant": "Discriminant Practice",
        "Graphing": "Graphing Essentials",
    }

    result = run_assessment_pipeline(
        data_dir / "questions.csv",
        data_dir / "question_metadata.csv",
        data_dir / "student_responses.csv",
        course_map,
        threshold=60.0,
        n_clusters=3,
    )

    assert set(result.keys()) == {
        "scores_by_student",
        "strong_weak_by_student",
        "cluster_by_student",
        "recommendations_by_student",
    }

    # deterministic property from dataset fixture
    assert result["strong_weak_by_student"]["S1"] == {"strong": "Roots", "weak": "Discriminant"}

    # each student should have a cluster label
    assert set(result["cluster_by_student"].keys()) == set(result["scores_by_student"].keys())
    assert all(isinstance(label, int) for label in result["cluster_by_student"].values())

    # weak topic for S1 should map to a remediation course
    assert "Discriminant Practice" in result["recommendations_by_student"]["S1"]
