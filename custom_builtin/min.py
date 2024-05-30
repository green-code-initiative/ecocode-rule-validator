from argparse import ArgumentParser

def _min(iterable):
    lenght = len(iterable)
    if lenght == 0:
        raise  ValueError("Iterable is empty.")

    m = iterable[0]

    for i in range(1, lenght):
        if iterable[i] < m:
            m = iterable[i]
    return m

def main(size):
    n = 100
    for _ in range(n):
        iterable = range(size)
        _min(iterable)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    main(args.size)
