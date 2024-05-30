from argparse import ArgumentParser

def _hex(x):
    if not isinstance(x, int):
        raise TypeError("an integer is required")
    hex_digits = "0123456789abcdef"
    result = ""
    while x > 0:
        x = x / 16
        remainder = x % 16
        result = hex_digits[remainder] + result
    return "0x" + result if result else "0x0"

def main(x: int):
    n = 1000
    for _ in range(n):
        _hex(x)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args.x)
