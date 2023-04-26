#!/usr/bin/env python3
import os
import sys

def get_buffer_len(file_name: str) -> int:
    for i in range(1, 2048, 4):
        if os.system(f'{file_name} {"A" * i}'):
            return i
    raise RuntimeError('Couldnt determine buffer length')

if __name__ == '__main__':
    print(f'Buffer length is: {get_buffer_len(sys.argv[1])}')