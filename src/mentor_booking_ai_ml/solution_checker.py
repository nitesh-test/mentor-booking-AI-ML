"""Utilities for validating step-by-step math solutions with OpenAI."""

from __future__ import annotations

import json
from typing import List, Optional, Dict, Any

from .ocr_openai import ask_openai


def check_solution_steps(
    problem: str,
    steps: List[str],
    *,
    model: str = "gpt-4o-mini",
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Use OpenAI to detect the first incorrect step in a math solution.

    Parameters
    ----------
    problem:
        The original math problem statement.
    steps:
        Ordered list of the student's solution steps.
    model:
        OpenAI model to query.
    api_key:
        Optional API key; falls back to environment configuration if ``None``.

    Returns
    -------
    dict
        Parsed JSON dictionary returned by the model containing at least
        ``error_step`` (1-based index of the first incorrect step or ``null``)
        and explanatory text fields.
    """

    step_lines = "\n".join(f"{i + 1}. {line}" for i, line in enumerate(steps))
    prompt = (
        "You are a math tutor. Given a problem and a student's solution steps, "
        "identify the first incorrect step and provide a correction. Respond in JSON "
        "with keys: error_step (null if none), message, correct_step, final_answer.\n"  # noqa: E501
        f"Problem: {problem}\nSteps:\n{step_lines}"
    )
    response = ask_openai(prompt, model=model, api_key=api_key)
    try:
        return json.loads(response)
    except json.JSONDecodeError as exc:  # pragma: no cover - defensive branch
        raise ValueError("OpenAI response was not valid JSON") from exc


__all__ = ["check_solution_steps"]
