msg = input('input text:')

with open('sample.txt', 'w') as f:
    f.write(msg)
    print('save message!')
