from setuptools import setup, find_packages

setup(
    name="fast-text-analyzer",
    version="0.1.0",
    description="Professional Python text analysis tool",
    author="Redwan Ahmed Khan",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "click",
        "langdetect",
        "requests",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "fast-text-analyzer=fast_text_analyzer.cli:cli",
        ],
    },
    python_requires='>=3.8',
)
