import sys


def main():
    if len(sys.argv) > 1:
        print(f"Loaded file: {sys.argv[1]}")
    else:
        print("CSV Analyzer Toolkit started")


if __name__ == "__main__":
    main()