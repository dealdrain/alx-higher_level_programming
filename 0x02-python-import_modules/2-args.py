#!/usr/bin/python3

if __name__ == "__main__":
    import sys

total = len(sys.argv)
if total <= 1:
    print("0 arguments.")
else:
    print(f"{total - 1} {'argument' if total == 2 else 'arguments'}:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
