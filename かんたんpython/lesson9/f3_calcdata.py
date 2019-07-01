data = []
filename = 'f2.txt'
func = lambda x: x

def read(fname = filename):
    global data
    global filename
    filename = fname
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    data += [int(line.strip())]
                except ValueError:
                    data += [0]
    except Exception as f:
        print(f)

def write(fname = filename):
    global data
    try:
        with open(fname, 'w') as f:
            for item in data:
                f.write(str(item) + '\n')
    except Exception as f:
        print(f)

def update(fn = func, save = False):
    global data
    global func
    func = fn
    data2 = []
    for item in data:
        data2 += [func(item)]
    if save:
        data = data2
    return data2

def calc():
    global data
    total = 0
    for item in data:
        total += item
    return {'total': total, 'ave': total // len(data)}
