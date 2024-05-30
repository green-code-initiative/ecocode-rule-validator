from argparse import ArgumentParser

def _any(iterable):
    for element in iterable:
        if element:
            return True
    return False

def main(size):
    n = 100
    for _ in range(n):
        iterable = (False for _ in range(size))
        _any(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
