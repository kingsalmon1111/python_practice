from f5_calcdata import CalcData

obj = CalcData('f2.txt')
obj.read()

print(obj.data)
print(obj.calc())

obj.update(lambda x: int(x / 2), True)
print(obj.data)
print(obj.calc())

obj.write()
print('end.')
