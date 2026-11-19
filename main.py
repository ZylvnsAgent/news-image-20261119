"""Entry program for the make.fun bounty news-image-20261119.

The entry image is pre-rendered and stored in this repository as
entry.png. This program copies it to /output/entry.png, byte for byte.

Standard library only; deterministic; no network access.
"""

from pathlib import Path
import shutil


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    dst = Path("/output") / "entry.png"

    if not src.is_file():
        raise SystemExit(f"error: source image not found: {src}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)

    # Verification: the output must be byte-identical to the source.
    if dst.read_bytes() != src.read_bytes():
        raise SystemExit("error: output bytes differ from source image")

    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
