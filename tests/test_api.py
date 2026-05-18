import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.api_service import get_motivational_quote


def test_get_motivational_quote():
    quote = get_motivational_quote()

    assert "content" in quote
    assert "author" in quote
    assert isinstance(quote["content"], str)
    assert isinstance(quote["author"], str)