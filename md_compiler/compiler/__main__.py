import logging
import argparse
from pathlib import Path

from compiler import MDCompiler, Config
from compiler.extensions import StrikeExtension, CalloutExtension, HSpacerExtension

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, default=Path.cwd())
    parser.add_argument("--docs", type=Path, default=Path.cwd() / "docs")
    parser.add_argument("--build", type=Path, default=Path.cwd() / "build")
    parser.add_argument("--templates", type=Path, default=Path.cwd() / "templates")
    parser.add_argument("--watch", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()

    config = Config(
        base=args.base,
        build=args.build,
        docs=args.docs,
        templates=args.templates,
    )
    
    extensions = [
        "meta",
        "toc",
        "tables",
        "fenced_code",
        "codehilite",
        StrikeExtension(),
        CalloutExtension(),
        HSpacerExtension()
    ]

    compiler = MDCompiler(config, extensions=extensions)

    compiler.compile()

    if args.watch:
        compiler.watch()


if __name__ == "__main__":
    main()