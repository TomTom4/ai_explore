import typer

from .recorder import play_wav, record_sound

app = typer.Typer()


@app.command()
def record():
    record_sound()


@app.command()
def play():
    play_wav()


@app.command()
def speech_to_text():
    raise NotImplementedError


if __name__ == "__main__":
    app()
