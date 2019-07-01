import codecs

with codecs.open('sample.txt', 'w', 'utf-8') as f:
    while True:
        msg = input('input text:')
        if msg == '':
            break
        f.write(msg + '\n')
    print('save all messages!')
