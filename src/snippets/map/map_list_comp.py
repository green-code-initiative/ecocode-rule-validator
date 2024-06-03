from argparse import ArgumentParser

def triple(item):
    return item * 3

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        [triple(i) for i in iterable]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
