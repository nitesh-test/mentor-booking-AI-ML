import sys
import types

from mentor_booking_ai_ml import ocr_and_ask_openai


class DummyVisionClient:
    def text_detection(self, image):  # pragma: no cover - simple stub
        class Resp:
            error = type("Err", (), {"message": ""})
            text_annotations = [type("T", (), {"description": "2 + 2"})]

        return Resp()


class DummyOpenAI:
    class chat:  # pragma: no cover - simple stub
        class completions:
            @staticmethod
            def create(*, model, messages):
                assert messages[0]["content"] == "2 + 2"
                Choice = type("Choice", (), {"message": {"content": "4"}})
                return type("Resp", (), {"choices": [Choice()]})

    def __init__(self, api_key=None):
        pass


def test_ocr_and_ask_openai(monkeypatch, tmp_path):
    image_path = tmp_path / "img.png"
    image_path.write_bytes(b"fake")

    google_module = types.ModuleType("google")
    cloud_module = types.ModuleType("cloud")
    vision_module = types.ModuleType("vision")
    google_module.__path__ = []
    cloud_module.__path__ = []
    vision_module.ImageAnnotatorClient = lambda: DummyVisionClient()
    vision_module.Image = lambda content: types.SimpleNamespace(content=content)

    openai_module = types.ModuleType("openai")
    openai_module.OpenAI = lambda api_key=None: DummyOpenAI()

    sys.modules["google"] = google_module
    sys.modules["google.cloud"] = cloud_module
    sys.modules["google.cloud.vision"] = vision_module
    cloud_module.vision = vision_module
    sys.modules["openai"] = openai_module

    result = ocr_and_ask_openai(image_path)
    assert result == "4"

