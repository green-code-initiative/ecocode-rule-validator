import os
import sys
import re
import time

vjoule_cmd = os.environ.get("VJOULE_CMD", "vjoule")
python_cmd = os.environ.get("PYTHON_CMD", "python3")


def parse_results(input: str) -> dict:
    pattern = r'(CPU|RAM)\s+([\d.]+)\s+J'
    matches = re.findall(pattern, input)
    # Create a dictionary from the matches
    results = {key: float(value) for key, value in matches}
    results['total'] = sum(results.values())
    return results


def eval_command(cmd: str, *args) -> dict:
    args_as_str = " ".join(args)
    command = f"{vjoule_cmd} {cmd} {args_as_str}"
    print("### - " + str(time.time()) + " - Start of command - " + command )
    stream = os.popen(command)
    print("### - " + str(time.time()) + " - End of command - " + command)
    return parse_results(stream.read())


def eval_python(filepath: str, *args) -> dict:
    args_as_str = " ".join([str(a) for a  in args])
    return eval_command(f"{python_cmd} {filepath} {args_as_str}")


def main() -> int:
    eval_python(sys.argv[1], *sys.argv[2:]) 
    return 0


if __name__ == '__main__':
    sys.exit(main())
