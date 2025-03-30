from setuptools import setup, find_packages
from src.emoji_sentiment import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="emoji-sentiment",
    version=__version__,
    description="A Python package for emoji sentiment analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Wan, Jiun-Wei",
    author_email="wei840222@gmail.com",
    url="https://github.com/wei840222/emoji-sentiment",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "emoji-data-python",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
