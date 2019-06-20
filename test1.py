import os


def main():
    cwd = os.getcwd()
    cwd = cwd + "/newfolder"
    if not cwd is None:
        print(cwd)
    print(cwd)
    print("hello world")


if __name__ == '__main__':
    main()
