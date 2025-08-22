from mentor_booking_ai_ml import check_solution_steps


def test_check_solution_steps(monkeypatch):
    fake_json = '{"error_step": 2, "message": "addition error", "correct_step": "4 + 5 = 9", "final_answer": "x=2"}'
    monkeypatch.setattr(
        "mentor_booking_ai_ml.solution_checker.ask_openai", lambda prompt, model="gpt-4o-mini", api_key=None: fake_json
    )
    result = check_solution_steps("2x+3=7", ["2x+3=7", "2x=5", "x=2.5"])
    assert result["error_step"] == 2
    assert "addition" in result["message"]
