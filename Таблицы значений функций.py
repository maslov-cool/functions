class Function:
    def __init__(self, arg1, action, arg2):
        if arg1.replace('-', '').isdigit():
            self.arg1 = int(arg1)
        elif arg1.replace('.', '').isdigit():
            self.arg1 = float(arg1)
        else:
            self.arg1 = arg1
        self.action = action
        if arg2.isdigit():
            self.arg2 = int(arg2)
        elif arg2.replace('.', '').isdigit():
            self.arg2 = float(arg2)
        else:
            self.arg2 = arg2

    def calculate(self, x):
        a, b = (self.arg1 if isinstance(self.arg1, int) or isinstance(self.arg1, float) else 0,
                self.arg2 if isinstance(self.arg2, int) or isinstance(self.arg2, float) else 0)

        # 'x' или нет
        if self.arg1 == 'x':
            a = x
        if self.arg2 == 'x':
            b = x

        # если функции в аргументах
        if self.arg1 in functions.keys() and self.arg1 != 'x':
            a = functions[self.arg1].calculate(x)
        if self.arg2 in functions.keys() and self.arg2 != 'x':
            b = functions[self.arg2].calculate(x)

        if self.action == '+':
            return a + b
        elif self.action == '-':
            return a - b
        elif self.action == '*':
            return a * b
        elif self.action == '/':
            return a / b
        return a ** b


functions = {
    'x': Function('x', '*', '1'),
    'sqrt_fun': Function('x', '**', '0.5')
}


for _ in range(int(input())):
    s = input().split()
    if s[0] == 'define':
        functions[s[1]] = Function(s[2], s[3], s[4])
    else:
        print(' '.join(str(functions[s[1]].calculate(int(i))) for i in s[2:]))


