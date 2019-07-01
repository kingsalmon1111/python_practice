calcdata = __import__('f3_calcdata_')

calcdata.read()

print(calcdata.data)
print(calcdata.calc())

calcdata.update(lambda x: int(x * 2), True)
print(calcdata.data)
print(calcdata.calc())

calcdata.write()
print('end')
