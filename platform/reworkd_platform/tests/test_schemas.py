import pytest
from pydantic import ValidationError

from reworkd_platform.schemas import ModelSettings


@pytest.mark.parametrize(
    "settings",
    [
        {
            "model": "gpt-4-32k",
        },
        {
            "temperature": -1,
        },
        {
            "max_tokens": 8000,
        },
    ],
)
def test_model_settings_invalid(settings):
    with pytest.raises(ValidationError):
        ModelSettings(**settings)


def test_model_settings_default():
    settings = ModelSettings(**{})
    assert settings.model == "gpt-3.5-turbo"
    assert settings.temperature == 0.9
    assert settings.max_tokens == 500
    assert settings.language == "English"
