class CalcData:
    def __init__(self, fname = 'f2.txt'):
        self.data = []
        self.filename = fname
        self.func = lambda x: x

    def __str__(self):
        return '<CalcData filename=' + self.filename
        + 'data=' + str(self.data) + '>'

    def read(self, fname = None):
        if fname != None:
            self.filename = fname
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    try:
                        self.data += [int(line.strip())]
                    except ValueError:
                        self.data += [0]
        except Exception as f:
            print(f)
        print(self.data)

    def write(self, fname = None):
        if fname != None:
            fpath = fname
        else:
            fpath = self.filename
        try:
            with open(fpath, 'w') as f:
                for item in self.data:
                    f.write(str(item) + '\n')
        except Exception as f:
            print(f)

    def update(self, fn = None, save = False):
        if fn != None:
            self.func = fn
        data2 = []
        for item in self.data:
            data2 += [self.func(item)]
        if save:
            self.data = data2
        return data2

    def calc(self):
        total = 0
        for item in self.data:
            total += item
        try:
            return {'total': total, 'ave': total // len(self.data)}
        except ZeroDivisionError:
            return {'total': total, 'ave': 0}

import sys

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
    else:
        fname = 'f2.txt'
    ob = CalcData(fname)
    ob.read()
    print(ob.calc())
    print('end.')
