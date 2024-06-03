from argparse import ArgumentParser

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        sum(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
