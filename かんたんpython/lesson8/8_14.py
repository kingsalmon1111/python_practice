import codecs
import os

try:
    with codecs.open('/8-14.py', 'r', 'utf-8') as f:
        while True:
            n = input('input number:')
            if n == '':
                break
            try:
                num = int(n)
            except ValueError:
                num = 0
            f.seek(10 * num, os.SEEK_SET)
            try:
                res = int(f.read(9))
            except ValueError as err:
                print(err)
                res = 0
            print('data: ' + str(res))
except Exception as err2:
    print(err2)
