#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build(source: Path, output: Path, package_name: str) -> Path:
    skill_md = source / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"Missing entrypoint: {skill_md}")
    text = skill_md.read_text(encoding="utf-8")
    if not text.lstrip().startswith("---"):
        raise SystemExit("SKILL.md must start with YAML frontmatter")

    output.mkdir(parents=True, exist_ok=True)
    artifact = output / f"{package_name}.skill"

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / package_name
        shutil.copytree(source, root)
        zip_path = Path(tmp) / f"{package_name}.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in root.rglob("*"):
                if p.is_file():
                    zf.write(p, p.relative_to(root.parent))
        shutil.copy2(zip_path, artifact)

    checksum = sha256(artifact)
    (output / f"{artifact.name}.sha256").write_text(
        f"{checksum}  {artifact.name}\n", encoding="utf-8"
    )
    return artifact


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", default=Path("dist"), type=Path)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    artifact = build(args.source, args.output, args.name)
    print(artifact)


if __name__ == "__main__":
    main()
