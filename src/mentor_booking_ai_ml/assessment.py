"""Core assessment logic for analyzing student responses.

This module provides small utility functions to evaluate the strengths and
weaknesses of students based on their answers to comprehension questions. It
also includes simple clustering and course recommendation helpers implemented
with only the Python standard library so that it runs in minimal environments.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict
from typing import Dict, List


@dataclass
class Question:
    """Representation of a comprehension question."""

    question_id: str
    correct_answer: str
    topic: str


@dataclass
class Response:
    """Student response to a question."""

    question_id: str
    selected: str


def calculate_topic_scores(
    questions: List[Question], responses: List[Response]
) -> Dict[str, float]:
    """Calculate percentage scores per topic for a student's responses."""

    question_map = {q.question_id: q for q in questions}
    topic_totals: Dict[str, int] = {}
    topic_correct: Dict[str, int] = {}

    for resp in responses:
        q = question_map.get(resp.question_id)
        if q is None:
            continue
        topic_totals[q.topic] = topic_totals.get(q.topic, 0) + 1
        if resp.selected == q.correct_answer:
            topic_correct[q.topic] = topic_correct.get(q.topic, 0) + 1

    return {
        topic: (topic_correct.get(topic, 0) / total) * 100
        for topic, total in topic_totals.items()
    }


def _build_feature_vector(topic_scores: Dict[str, float], topics: List[str]) -> List[float]:
    return [topic_scores.get(t, 0.0) for t in topics]


def cluster_students(
    student_topic_scores: List[Dict[str, float]],
    n_clusters: int = 2,
    max_iter: int = 10,
) -> List[int]:
    """Cluster students by topic performance using a minimal k-means implementation."""

    if not student_topic_scores:
        return []

    all_topics = sorted({t for scores in student_topic_scores for t in scores})
    vectors = [_build_feature_vector(scores, all_topics) for scores in student_topic_scores]
    centroids = vectors[:n_clusters]

    for _ in range(max_iter):
        clusters: List[List[List[float]]] = [[] for _ in centroids]
        for vec in vectors:
            distances = [sum((a - b) ** 2 for a, b in zip(vec, c)) for c in centroids]
            idx = distances.index(min(distances))
            clusters[idx].append(vec)
        new_centroids = []
        for cluster, centroid in zip(clusters, centroids):
            if cluster:
                dim = len(cluster[0])
                mean_vec = [sum(point[d] for point in cluster) / len(cluster) for d in range(dim)]
                new_centroids.append(mean_vec)
            else:
                new_centroids.append(centroid)
        if new_centroids == centroids:
            break
        centroids = new_centroids

    labels = []
    for vec in vectors:
        distances = [sum((a - b) ** 2 for a, b in zip(vec, c)) for c in centroids]
        labels.append(distances.index(min(distances)))
    return labels


def recommend_courses(
    topic_scores: Dict[str, float], course_map: Dict[str, str], threshold: float = 60.0
) -> List[str]:
    """Recommend courses for topics where the student is weak."""

    return [
        course_map[topic]
        for topic, score in topic_scores.items()
        if score < threshold and topic in course_map
    ]



def load_question_bank(questions_csv: Path, metadata_csv: Path) -> List[Question]:
    """Load questions and merge with metadata to attach topics."""

    topic_map: Dict[str, str] = {}
    with metadata_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            topic_map[row["question_id"]] = row["sub_topics"]

    questions: List[Question] = []
    with questions_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = row["question_id"]
            questions.append(Question(qid, row["correct_answer"], topic_map.get(qid, "")))
    return questions


def load_student_responses(responses_csv: Path) -> Dict[str, List[Response]]:
    """Load student responses keyed by student id."""

    by_student: Dict[str, List[Response]] = defaultdict(list)
    with responses_csv.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            by_student[row["student_id"]].append(Response(row["question_id"], row["student_response"]))
    return by_student


def strong_weak_topics_for_students(
    questions: List[Question], responses: Dict[str, List[Response]]
) -> Dict[str, Dict[str, str]]:
    """Determine the strongest and weakest topic for each student."""

    results: Dict[str, Dict[str, str]] = {}
    for sid, resps in responses.items():
        scores = calculate_topic_scores(questions, resps)
        if not scores:
            continue
        strong = max(scores, key=scores.get)
        weak = min(scores, key=scores.get)
        results[sid] = {"strong": strong, "weak": weak}
    return results

