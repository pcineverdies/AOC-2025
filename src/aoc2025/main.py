import importlib
import re
from pathlib import Path
import argparse
from typing import Type

from .utils.day import Day

def get_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("action", type=str, choices=["run", "init", "test"])
        parser.add_argument("day", type=int)
        return parser.parse_args()


def get_input(dir: str, day_number: int, prefix: str) -> list[str]:

    day_string = str(day_number) if day_number > 9 else f"0{day_number}"
    pattern = re.compile(fr"{prefix}_{day_string}.*")

    test_inputs: list[str] = []

    for file in Path(dir).iterdir():
        if file.is_file() and pattern.match(file.name):
            with open(file, "r", encoding="utf-8") as f:
                test_inputs.append(f.read().strip())

    return test_inputs


def get_day_class(day_number: int) -> Type[Day]:

    day_string = str(day_number) if day_number > 9 else f"0{day_number}"
    day_module_name = f"day_{day_string}"

    try:
        day_module = importlib.import_module(f".{day_module_name}", package=__package__)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Error: Module '{day_module_name}' not found.")

    try:
        day_class = getattr(day_module, f"Day{day_string}")
    except AttributeError:
        raise ModuleNotFoundError(f"Error: Class 'Day{day_string}' not found in '{day_module_name}'.")

    return day_class


def test(args: argparse.Namespace) -> None:
    day_class = get_day_class(args.day)
    inputs = get_input("./tests", args.day, "test")

    if len(inputs) == 0:
        raise ValueError("No tests found; run `init` first? Are they all empty?")

    inputs = [f for f in inputs if len(f) > 0]
    if len(inputs) == 0:
        raise ValueError("All the files are empty")

    day_instance: Day = day_class(args.day, inputs, None)
    day_instance.run()


def init(args: argparse.Namespace) -> None:

    day_string = str(args.day) if args.day > 9 else f"0{args.day}"

    files = [
        Path(f"input/test_{day_string}.txt"),
        Path(f"tests/test_{day_string}_1.txt"),
        Path(f"tests/test_{day_string}_2.txt"),
    ]

    for file in files:
        file.parent.mkdir(parents=True, exist_ok=True)
        if not file.exists():
            file.touch()
            print(f"+ -- Created {file}")

    file = Path(f"src/aoc2025/day_{day_string}.py")

    file.parent.mkdir(parents=True, exist_ok=True)
    if not file.exists():
        file.touch()
        template = Path("src/aoc2025/__template.py")
        content = template.read_text(encoding="utf-8")
        content = content.replace("XX", day_string)
        file.write_text(content, encoding="utf-8")
        print(f"+ -- Created {file} from template")


def run(args: argparse.Namespace) -> None:
    day_class = get_day_class(args.day)

    inputs = get_input("./input", args.day, "test")

    if len(inputs) != 1:
        raise ValueError("Expected one input file; run `init` first?")
    input = inputs[0]
    if len(input) == 0:
        raise ValueError("Empty input file")

    day_instance: Day = day_class(args.day, None, input)
    day_instance.run()


def main(args: argparse.Namespace) -> None:

    if args.action == "run":
        run(args)
    if args.action == "init":
        init(args)
    if args.action == "test":
        test(args)


if __name__ == "__main__":
    main(get_args())
