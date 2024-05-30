from argparse import ArgumentParser

def main(x: int):
    n = 1000
    for _ in range(n):
        abs(x)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args.x)
