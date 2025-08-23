"""Utilities for running OCR with Google Vision and forwarding text to OpenAI."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

def extract_text_google_vision(image_path: str | Path) -> str:
    """Return text detected in *image_path* using Google Vision OCR.

    Parameters
    ----------
    image_path:
        Path to an image file readable by the Vision API.

    Returns
    -------
    str
        The detected text as a single string.  Empty string if nothing was
        detected.
    """

    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    with open(image_path, "rb") as img_file:
        content = img_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    if response.error.message:
        raise RuntimeError(response.error.message)
    texts = response.text_annotations
    return texts[0].description if texts else ""


def ask_openai(prompt: str, *, model: str = "gpt-4o-mini", api_key: Optional[str] = None) -> str:
    """Send *prompt* to OpenAI's chat completions API and return the reply."""

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]


def ocr_and_ask_openai(image_path: str | Path, *, model: str = "gpt-4o-mini", api_key: Optional[str] = None) -> str:
    """Run OCR on *image_path* then send the text to OpenAI and return its reply."""

    text = extract_text_google_vision(image_path)
    if not text.strip():
        raise ValueError("No text detected in image")
    return ask_openai(text, model=model, api_key=api_key)


__all__ = ["extract_text_google_vision", "ask_openai", "ocr_and_ask_openai"]

