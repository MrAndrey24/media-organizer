# PIL: python3 -m pip install Pillow on MAC, Windows python -m pip install Pillow
from PIL import Image
from pathlib import Path

DOWNLOADS_FOLDER = Path("/your path folder")
PICTURES_FOLDER = Path("/your path folder")
MUSIC_FOLDER = Path("/your path folder")


def compress_images():
    """Compresses image files in the downloads folder and moves them to the pictures folder."""
    for file_path in DOWNLOADS_FOLDER.glob("*"):
        name, extension = file_path.stem, file_path.suffix.lower()

        if extension in (".jpg", ".jpeg", ".png"):
            try:
                with Image.open(file_path) as img:
                    img.save(PICTURES_FOLDER / f"compressed_{file_path.name}",
                             optimize=True, quality=60)
            except:
                print(f"Failed to open {file_path}")
            else:
                file_path.unlink()  # remove original file
                print(
                    f"{name}{extension} was compressed and moved to {PICTURES_FOLDER}")


def move_music():
    """Moves music files in the downloads folder to the music folder."""
    for file_path in DOWNLOADS_FOLDER.glob("*.mp3"):
        file_path.rename(MUSIC_FOLDER / file_path.name)
        print(f"{file_path.name} was moved to {MUSIC_FOLDER}")


if __name__ == "__main__":
    compress_images()
    move_music()
