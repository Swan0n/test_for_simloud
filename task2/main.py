import argparse


def swap(first: str, second: str):
    read_file = 'input.txt'
    write_file = 'output.txt'
    with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
        for line in fr:
            line = line.replace(first, second)
            line = line.lower()
            fw.write(line)
    with open(read_file, 'r') as fr:
        for line in fr:
            print(line, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("first", type=str)
    parser.add_argument("second", type=str)

    args = parser.parse_args()
    swap(args.first, args.second)





