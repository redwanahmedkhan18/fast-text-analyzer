from collections import Counter
from langdetect import detect
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


class Analyzer:
    """
    Fast Text Analyzer

    Provides:
    - Word & sentence statistics
    - Language detection
    - Extractive summarization
    - Keyword extraction
    - Readability scoring
    """

    def __init__(self, text: str):
        self.text = text.strip()

        # Tokenize
        self.tokens = word_tokenize(self.text)
        self.words = [w.lower() for w in self.tokens if w.isalnum()]
        self.sentences = sent_tokenize(self.text)

    # ---------------- Basic Metrics ---------------- #

    def word_count(self) -> int:
        return len(self.words)

    def unique_words(self) -> int:
        return len(set(self.words))

    def sentence_count(self) -> int:
        return len(self.sentences)

    def language(self) -> str:
        try:
            return detect(self.text)
        except Exception:
            return "unknown"

    # ---------------- Summarization ---------------- #

    def summarize(self, top_n: int = 3) -> str:
        """
        Extractive summarization using frequency-based scoring.
        """
        if not self.sentences:
            return ""

        stop_words = set(stopwords.words("english"))
        filtered_words = [w for w in self.words if w not in stop_words]

        if not filtered_words:
            return " ".join(self.sentences[:top_n])

        freq = Counter(filtered_words)

        sentence_scores = {}
        for i, sent in enumerate(self.sentences):
            tokens = [w.lower() for w in word_tokenize(sent) if w.isalnum()]
            sentence_scores[i] = sum(freq.get(w, 0) for w in tokens)

        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]
        top_sentences = sorted(top_sentences)

        return " ".join([self.sentences[i] for i in top_sentences])

    # ---------------- Keyword Extraction ---------------- #

    def keywords(self, top_n: int = 5) -> list[str]:
        """
        Extracts top keywords using frequency filtering.
        """
        stop_words = set(stopwords.words("english"))
        words_filtered = [w for w in self.words if w not in stop_words]

        freq = Counter(words_filtered)
        return [word for word, _ in freq.most_common(top_n)]

    # ---------------- Readability ---------------- #

    def flesch_reading_score(self) -> float:
        """
        Computes Flesch Reading Ease Score.
        Higher score → easier to read.
        """
        total_words = self.word_count()
        total_sentences = self.sentence_count()

        if total_words == 0 or total_sentences == 0:
            return 0.0

        total_syllables = sum(self.count_syllables(word) for word in self.words)

        score = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)
        return round(score, 2)

    @staticmethod
    def count_syllables(word: str) -> int:
        """
        Approximate syllable counter.
        """
        word = word.lower()
        vowels = "aeiouy"
        count = 0

        if len(word) == 0:
            return 0

        if word[0] in vowels:
            count += 1

        for i in range(1, len(word)):
            if word[i] in vowels and word[i - 1] not in vowels:
                count += 1

        if word.endswith("e"):
            count = max(1, count - 1)

        return max(count, 1)
