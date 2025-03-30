# Emoji Sentiment

A Python package for emoji sentiment analysis.

<img width="531" alt="image" src="https://github.com/user-attachments/assets/5b53da6f-be97-4ec2-a2d5-dc09bd6f9917" />

## Installation

```bash
pip install emoji-sentiment
```

## Usage

```python
from emoji_sentiment import EmojiSentiment

emoji_sentiment = EmojiSentiment()
smile_emoji = emoji_sentiment.get("smile")
print(smile_emoji)
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
