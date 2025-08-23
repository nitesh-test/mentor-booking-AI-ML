from pathlib import Path
from mentor_booking_ai_ml.comprehension_assessment import analyze_comprehension


def test_analyze_comprehension():
    report = analyze_comprehension(Path("data"))
    assert report["S1"]["strong"] == "Main Idea"
    assert report["S1"]["weak"] == "Vocabulary"
    assert report["S2"]["strong"] == "Vocabulary"
    assert report["S2"]["weak"] == "Main Idea"
