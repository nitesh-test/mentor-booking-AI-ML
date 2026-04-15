"""Pipeline trigger utilities for student assessment workflows."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from .assessment import (
    calculate_topic_scores,
    cluster_students,
    load_question_bank,
    load_student_responses,
    recommend_courses,
    strong_weak_topics_for_students,
)


def run_assessment_pipeline(
    questions_csv: str | Path,
    metadata_csv: str | Path,
    responses_csv: str | Path,
    course_map: Dict[str, str],
    *,
    threshold: float = 60.0,
    n_clusters: int = 3,
) -> Dict[str, Any]:
    """Run the end-to-end assessment pipeline for all students.

    The pipeline performs the following steps:
      1. Load question bank and student responses from CSV files.
      2. Calculate topic scores for each student.
      3. Determine strongest and weakest topics per student.
      4. Cluster students by their topic-score vectors.
      5. Recommend remediation courses for weak topics.

    Returns a dictionary keyed by output artifact names.
    """

    questions = load_question_bank(Path(questions_csv), Path(metadata_csv))
    responses_by_student = load_student_responses(Path(responses_csv))

    student_ids = sorted(responses_by_student.keys())
    scores_by_student = {
        sid: calculate_topic_scores(questions, responses_by_student[sid]) for sid in student_ids
    }

    strong_weak_by_student = strong_weak_topics_for_students(questions, responses_by_student)

    score_vectors = [scores_by_student[sid] for sid in student_ids]
    labels = cluster_students(score_vectors, n_clusters=n_clusters)
    cluster_by_student = {sid: labels[index] for index, sid in enumerate(student_ids)}

    recommendations_by_student = {
        sid: recommend_courses(scores_by_student[sid], course_map, threshold=threshold)
        for sid in student_ids
    }

    return {
        "scores_by_student": scores_by_student,
        "strong_weak_by_student": strong_weak_by_student,
        "cluster_by_student": cluster_by_student,
        "recommendations_by_student": recommendations_by_student,
    }


__all__ = ["run_assessment_pipeline"]
