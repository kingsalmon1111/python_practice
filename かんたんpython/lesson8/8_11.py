import codecs

try:
    with codecs.open('sample.txt', 'w+', 'utf-8') as f:
        while True:
            msg = input('input text:')
            if msg == '':
                break
            f.write(msg + '\n')
        print('*save all message*')
        n = 1
        for line in f:
            print(str(n) + ': ' + line.strip())
            n += 1
except Exception as err:
    print('[ERROR] ' + str(err))
