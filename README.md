# Emoji Sentiment

A Python package for emoji sentiment analysis.

## Installation

```bash
pip install emoji-sentiment
```

## Usage

```python
from emoji_sentiment import EmojiSentiment

emoji_sentiment = EmojiSentiment()
smile_emoji = emoji_sentiment.get("smile")
print(smile_emoji.sentiment)
```

## Run demo local

```sh
streamlit run src/demo.py
```

## Run tests

```sh
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest --cov=./src/emoji_sentiment -v --cov-report=term ./tests
```
