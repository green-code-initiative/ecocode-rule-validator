from argparse import ArgumentParser

def _enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        _enumerate(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
