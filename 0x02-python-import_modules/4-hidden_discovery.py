#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    module_names = dir(hidden_4)
    for item in module_names:
        if item[:2] != "__":
            print(item)
