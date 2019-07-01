import codecs

try:
    with codecs.open('sample.txt', 'w', 'utf-8') as f:
        msg = input('input text:')
        f.write(msg + '\n')
        print('save message')
except Exception as err:
    print('[ERROR] ' + str(err))
