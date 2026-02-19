from fast_text_analyzer.analyzer import Analyzer

def test_basic_metrics():
    text = "Hello world. Hello again!"
    analyzer = Analyzer(text)
    assert analyzer.word_count() == 4
    assert analyzer.sentence_count() == 2
    assert analyzer.unique_words() == 3
