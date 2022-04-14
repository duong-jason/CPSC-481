#!/usr/bin/env python3


import sys


def save_to_file(stream):
    '''saves a stream of text to a .csv file'''
    file_handle = open('sentence_list.csv', 'w')
    file_handle.write(stream)
    file_handle.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        save_to_file(sys.argv[1])
    else:
        sys.exit('Only 1 argument must be specified.')
