#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    all_dir = dir(hidden_4)
    filtered_names = [name for name in all_dir if "__" not in name]

    for name in filtered_names:
        print(name)
