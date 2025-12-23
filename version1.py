print("简易计算器")
print("选择运算：")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")
while True:
    opertion = input('输入你的选择: 1/2/3/4:')
    if opertion in ('1','2','3','4'):
        break
while True:
    num1 = input('输入第一个数字:') 
    if num1.isdigit():
        num1 = float(num1)
        break
while True:
    num2 = input('输入第二个数字:')
    if num2.isdigit():
        num2 = float(num2)
        break
if opertion == '1':
    print(f'{num1+num2}')
elif opertion == '2':
    print(f'{num1-num2}') 
elif opertion == '3':
    print(f'{num1*num2}')
elif opertion == '4':
    try:
        print(f'{num1/num2}')
    except ZeroDivisionError:
        print("错误：除数不能为零")
        num2 = float(input('请输入一个非零数字作为你的第二个数字:'))
        print(f'{num1/num2}')
