from pathlib import Path
import subprocess

def process():
    for f in Path(".").glob("*.flac"):
        subprocess.run([
            "ffmpeg",
            "-i",
            f.name,
            "-ab",
            "320k",
            f"{f.stem}.mp3"
        ])