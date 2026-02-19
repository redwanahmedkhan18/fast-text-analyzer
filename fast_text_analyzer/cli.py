import os
import requests
import click
from rich.console import Console
from fast_text_analyzer.analyzer import Analyzer

console = Console()

@click.group()
def cli():
    """Fast Text Analyzer CLI"""
    pass

@cli.command()
@click.argument("source")
@click.option("--file", is_flag=True, help="Read text from file")
@click.option("--url", is_flag=True, help="Read text from URL")
@click.option("--summary", is_flag=True, help="Get text summary")
@click.option("--lang", is_flag=True, help="Detect language")
@click.option("--unique", is_flag=True, help="Count unique words")
@click.option("--keywords", is_flag=True, help="Extract keywords")
@click.option("--readability", is_flag=True, help="Show readability score")
def analyze(source, file, url, summary, lang, unique, keywords, readability):
    """Analyze text from direct input, file, or URL"""

    # Fetch text
    if file:
        if not os.path.exists(source):
            console.print("[red]File does not exist![/red]")
            return
        with open(source, 'r', encoding='utf-8') as f:
            text = f.read()
    elif url:
        try:
            r = requests.get(source)
            r.raise_for_status()
            text = r.text
        except Exception as e:
            console.print(f"[red]Error fetching URL: {e}[/red]")
            return
    else:
        text = source

    analyzer = Analyzer(text)

    console.print(f"[bold green]Total Words:[/bold green] {analyzer.word_count()}")
    console.print(f"[bold cyan]Total Sentences:[/bold cyan] {analyzer.sentence_count()}")
    if unique:
        console.print(f"[yellow]Unique Words:[/yellow] {analyzer.unique_words()}")
    if lang:
        console.print(f"[magenta]Language:[/magenta] {analyzer.language()}")
    if summary:
        console.print(f"[blue]Summary:[/blue] {analyzer.summarize()}")
    if keywords:
        console.print(f"[bright_magenta]Keywords:[/bright_magenta] {', '.join(analyzer.keywords())}")
    if readability:
        console.print(f"[bold red]Readability Score:[/bold red] {analyzer.flesch_reading_score()}")
