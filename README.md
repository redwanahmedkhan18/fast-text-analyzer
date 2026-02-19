
# Fast Text Analyzer

A lightweight, fast, and production-ready **Python text analysis toolkit** with CLI support.

---

## Features

- Word & sentence statistics  
- Automatic language detection  
- Extractive summarization  
- Keyword extraction  
- Readability scoring (Flesch Reading Ease)  
- Analyze text from **files, URLs, or direct input**  
- Rich colored CLI output  

---

##  Installation

```bash
pip install fast-text-analyzer
````

---

## CLI Usage

### Analyze Direct Text

```bash
fast-text-analyzer analyze "This is a simple example." --summary --lang --keywords
```

---

### Analyze File

```bash
fast-text-analyzer analyze sample.txt --file --summary --readability
```

---

### Analyze URL

```bash
fast-text-analyzer analyze https://example.com --url --summary --lang
```

---

##  Python API Usage

```python
from fast_text_analyzer import Analyzer

text = "Fast Text Analyzer is a professional Python module."
a = Analyzer(text)

print(a.word_count())
print(a.keywords())
print(a.summarize())
```

---

##  Tech Stack

* Python 3.8+
* NLTK
* Click
* Rich
* LangDetect
* Requests

---

##  License

MIT License

---

## Author

**Redwan Ahmed**
Machine Learning Engineer | Researcher | Instructor | Software Engineer

---

##  Commit

```bash
git add README.md
git commit -m "Add professional README"
git push
```

```
```
