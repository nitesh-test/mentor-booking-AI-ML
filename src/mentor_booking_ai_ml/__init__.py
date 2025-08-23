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
from .ocr_openai import (
    extract_text_google_vision,
    ask_openai,
    ocr_and_ask_openai,
)
from .solution_checker import check_solution_steps

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
    "extract_text_google_vision",
    "ask_openai",
    "ocr_and_ask_openai",
    "check_solution_steps",
]

__version__ = "0.1.0"
