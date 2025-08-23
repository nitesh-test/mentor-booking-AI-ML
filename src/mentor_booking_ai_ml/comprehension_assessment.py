from __future__ import annotations

"""Utilities for analyzing comprehension responses without touching existing modules."""

from pathlib import Path
from .assessment import (
    load_question_bank,
    load_student_responses,
    strong_weak_topics_for_students,
)


def analyze_comprehension(data_dir: Path):
    """Return per-student strong and weak topics for the comprehension dataset.

    Parameters
    ----------
    data_dir:
        Directory containing ``comprehension_questions.csv``,
        ``comprehension_question_metadata.csv`` and
        ``comprehension_student_responses.csv``.
    """
    questions = load_question_bank(
        data_dir / "comprehension_questions.csv",
        data_dir / "comprehension_question_metadata.csv",
    )
    responses = load_student_responses(
        data_dir / "comprehension_student_responses.csv"
    )
    return strong_weak_topics_for_students(questions, responses)
