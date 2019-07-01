with open('sample.txt', 'r') as f:
    n = 1
    for line in f:
        print(str(n)+ ': ' + line.strip())
        n += 1
