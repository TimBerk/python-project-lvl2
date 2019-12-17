# -*- coding:utf-8 -*-
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', type=str, dest='format')
    args = parser.parse_args()
    print(args.indir)


if __name__ == '__main__':
    main()