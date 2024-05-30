from argparse import ArgumentParser

def predicate(item):
    return item % 3 == 0


def list_filter(predicate, iterable):
    output = []
    for i in iterable:
        if predicate(i):
            output.append(i)
    return output


def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        list_filter(predicate, iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
