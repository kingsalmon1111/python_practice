with open('sample.txt', 'w') as f:
    while True:
        msg = input('input text:')
        if msg == '':
            break
        f.write(msg + '\n')
    print('save all messages!')
