import typer
from recorder import play_wav, record_sound

from speech_to_text import process_sample

app = typer.Typer()


@app.command()
def record():
    record_sound()


@app.command()
def play():
    play_wav()


@app.command()
def speech_to_text():
    process_sample()


if __name__ == "__main__":
    app()
