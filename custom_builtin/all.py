from argparse import ArgumentParser

def _all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def main(size):
    n = 100
    for _ in range(n):
        iterable = (True for _ in range(size))
        _all(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
