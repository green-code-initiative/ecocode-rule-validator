from argparse import ArgumentParser

def triple(item):
    return item * 3

def _map(function, iterable):
    for element in iterable:
        yield function(element)

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        for _ in _map(triple, iterable):
            pass

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
