import json
import os
import shutil
from pathlib import Path

MAX_CHARS = 180


def main():
    source = Path(__file__).resolve().with_name("entry.txt")
    text = source.read_text(encoding="utf-8").strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"entry rejected: {len(text)} chars, gate is 1..{MAX_CHARS}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    shutil.copyfile(source, target)
    print(json.dumps({"artifact": str(target), "chars": len(text), "status": "ok", "gate": MAX_CHARS}))


if __name__ == "__main__":
    main()
