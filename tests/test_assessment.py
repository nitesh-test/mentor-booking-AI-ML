
from mentor_booking_ai_ml import (
    Question,
    Response,
    calculate_topic_scores,
    cluster_students,
    recommend_courses,
    load_question_bank,
    load_student_responses,
    strong_weak_topics_for_students,
)


def test_calculate_topic_scores():
    questions = [
        Question("Q1", "A", "Topic1"),
        Question("Q2", "B", "Topic1"),
        Question("Q3", "A", "Topic2"),
    ]
    responses = [
        Response("Q1", "A"),  # correct
        Response("Q2", "C"),  # incorrect
        Response("Q3", "A"),  # correct
    ]

    scores = calculate_topic_scores(questions, responses)
    assert scores == {"Topic1": 50.0, "Topic2": 100.0}


def test_cluster_and_recommend():
    student_scores = [
        {"Topic1": 90.0, "Topic2": 50.0},
        {"Topic1": 85.0, "Topic2": 55.0},
        {"Topic1": 20.0, "Topic2": 95.0},
    ]

    labels = cluster_students(student_scores, n_clusters=2)
    assert len(labels) == 3
    assert set(labels) == {0, 1}

    course_map = {"Topic1": "Intro Topic1", "Topic2": "Intro Topic2"}
    recommendations = recommend_courses(student_scores[0], course_map, threshold=60)
    assert recommendations == ["Intro Topic2"]

def test_strong_weak_topics_from_csv(dataset_dir):
    questions = load_question_bank(dataset_dir / "questions.csv", dataset_dir / "question_metadata.csv")
    responses = load_student_responses(dataset_dir / "student_responses.csv")
    analysis = strong_weak_topics_for_students(questions, responses)
    assert analysis["S1"] == {"strong": "Roots", "weak": "Discriminant"}

