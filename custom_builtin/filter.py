from argparse import ArgumentParser

def predicate(item):
    return item % 3 == 0


def _filter(predicate, iterable):
    for i in iterable:
        if predicate(i):
            yield i


def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        for _ in _filter(predicate, iterable):
            pass

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
