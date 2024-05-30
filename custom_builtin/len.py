from argparse import ArgumentParser

def _len(s):
    lenght = 0
    for _ in s:
        lenght = lenght + 1

    return lenght

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        _len(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
