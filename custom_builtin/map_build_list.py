from argparse import ArgumentParser

def triple(item):
    return item * 3

def list_map(function, iterable):
    output = []
    for element in iterable:
        output.append(function(element))
    return output

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        list_map(triple, iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
