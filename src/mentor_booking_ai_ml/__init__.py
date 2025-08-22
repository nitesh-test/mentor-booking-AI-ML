"""Mentor Booking AI/ML project package."""

from .example import add
from .assessment import (
    Question,
    Response,
    calculate_topic_scores,
    cluster_students,
    recommend_courses,
    load_question_bank,
    load_student_responses,
    strong_weak_topics_for_students,

)

__all__ = [
    "add",
    "Question",
    "Response",
    "calculate_topic_scores",
    "cluster_students",
    "recommend_courses",

    "load_question_bank",
    "load_student_responses",
    "strong_weak_topics_for_students",

]

__version__ = "0.1.0"
