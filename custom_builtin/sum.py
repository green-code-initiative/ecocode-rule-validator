from argparse import ArgumentParser

def _sum(iterable):
    s = 0
    for v in iterable:
        s = s + v

    return s

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        _sum(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
