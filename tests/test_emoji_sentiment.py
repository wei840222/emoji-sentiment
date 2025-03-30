from src.emoji_sentiment.emoji import EmojiSentiment
import pytest


def test_emoji_sentiment_get():
    emoji_sentiment = EmojiSentiment()

    # test valid emoji name
    smile_emoji = emoji_sentiment.get("smile")
    assert smile_emoji is not None
    assert hasattr(smile_emoji, 'name')
    assert len(smile_emoji.name) > 0
    assert hasattr(smile_emoji, 'short_names')
    assert len(smile_emoji.short_names) > 0
    assert hasattr(smile_emoji, 'char')
    assert len(smile_emoji.char) == 1
    assert hasattr(smile_emoji, 'samples')
    assert smile_emoji.samples > 0
    assert hasattr(smile_emoji, 'score')
    assert smile_emoji.score >= -1 and smile_emoji.score <= 1

    # test different case of emoji name
    assert emoji_sentiment.get("SMILE") is not None
    assert emoji_sentiment.get("Smile") is not None

    # test invalid emoji name
    assert emoji_sentiment.get("not_exist_emoji") is None
    assert emoji_sentiment.get("") is None

    # test special characters
    assert emoji_sentiment.get("@#$%") is None


def test_emoji_sentiment_initialization():
    emoji_sentiment = EmojiSentiment()
    assert len(emoji_sentiment.all) > 0


@pytest.mark.parametrize("short_names", ["smile", "eyes", "thumbsup", "joy", "sunglasses"])
def test_common_emojis(short_names):
    emoji_sentiment = EmojiSentiment()
    emoji = emoji_sentiment.get(short_names)
    assert emoji is not None
