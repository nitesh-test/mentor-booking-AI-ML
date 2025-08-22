"""Mentor Booking AI/ML project package."""

from .example import add
from .assessment import (
    Question,
    Response,
    calculate_topic_scores,
    cluster_students,
    recommend_courses,
)

__all__ = [
    "add",
    "Question",
    "Response",
    "calculate_topic_scores",
    "cluster_students",
    "recommend_courses",
]

__version__ = "0.1.0"
