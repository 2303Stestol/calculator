class Calculate:
    var_dict = {}

    def __init__(self, string):
        self.string = string
        self.strlist = self.string.split(' ')
        self.strlist_1 = []
        self.strlist_2 = []
        self.list_math = []
        self.string_ans = str()
        self.stack_math = []
        for i in self.strlist:
            if i != '':
                self.strlist_1.append(i)
        return

    def Check(self):
        check_list = []
        for i in self.strlist_1:
            if i == '(':
                check_list.append(i)
            elif i == ')' and len(check_list) > 0:
                check_list.pop(-1)
            elif i == ')' and len(check_list) == 0:
                return False
        if len(check_list) == 0:
            return True
        else:
            return False

    def operation(self, two, one, s):
        if s == '-':
            return one - two
        elif s == '+':
            return one + two
        elif s == '*':
            return one * two
        elif s == '/':
            return one / two

    def prior(self, f):
        if f == '*':
            return 2
        elif f == '/':
            return 2
        elif f == '+':
            return 1
        elif f == '-':
            return 1

    def stak(self):
        stack = []
        queue = []
        for f in self.strlist_1:
            if f.isalpha() is True or f.isdigit() is True:
                queue.append(f)
            elif f in {'+', '-', '*', '/'}:
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(f)
                elif self.prior(f) > self.prior(stack[-1]):
                    stack.append(f)
                elif self.prior(f) <= self.prior(stack[-1]):
                    while (len(stack) > 0) and (self.prior(f) <= self.prior(stack[-1])) and (stack[-1] != '('):
                        queue.append(stack.pop(-1))
                    stack.append(f)
            elif f == '(':
                stack.append(f)
            elif f == ')':
                while stack[-1] != '(':
                    queue.append(stack.pop(-1))
                stack.pop(-1)
        while len(stack) > 0:
            queue.append(stack.pop(-1))
        return queue


    def narezka(self, part_list):
        if part_list.isdigit() is True or part_list.isalpha() is True:
            self.list_math.append(part_list)
        else:
            for k in part_list:
                if k in {'+', '-', '*', '/', ')', '('}:
                    self.list_math.append(part_list[:part_list.index(k)])
                    self.list_math.append(k)
                    return self.narezka(part_list[part_list.index(k) + 1:])
        return

    def main(self):
        if self.string == '':
            return
        if self.string[0] == '/':
            self.menu()
            return
        if '=' in self.string and len(self.string) > 1:
            self.strlist_2.append(self.string[:self.string.index('=')].strip())
            self.strlist_2.append('=')
            self.strlist_2.append(self.string[self.string.index('=') + 1:].strip())
            self.give(self.strlist_2)
            return
        if len(self.strlist_1) == 1 and self.string.isalpha() is True:
            self.take()
            return

        for i in self.strlist_1:
            self.narezka(i)

        self.strlist_1.clear()
        for h in self.list_math:
            if h != '':
                self.strlist_1.append(h)
        if self.Check() is True:
            self.list_math.clear()
            self.list_math = self.stak()

            self.mamath()
            return
        else:
            print('Invalid expression')
            return

    def give(self, strlist):
        if strlist[1] == '=':
            if strlist[0].isalpha() is True:
                if strlist[2].isdigit() is True:
                    self.var_dict[strlist[0]] = strlist[2]
                    return
                elif strlist[2] in self.var_dict:
                    self.var_dict[strlist[0]] = self.var_dict.get(strlist[2])
                    return
                elif strlist[2].isalpha() is True:
                    print('Unknown variable')
                    return
                else:
                    print('Invalid assignment')
                    return
            else:
                print('Invalid identifier')
                return

    def mamath(self):
        try:
            for j in self.list_math:
                if j.isdigit() is True:
                    self.stack_math.append(j)
                elif j in self.var_dict:
                    self.stack_math.append(self.var_dict.get(j))
                elif j in {'+', '-', '*', '/'}:
                    self.stack_math.append(self.operation(int(self.stack_math.pop(-1)), int(self.stack_math.pop(-1)), j))
            print(self.stack_math[0])
        except Exception:
            print('Invalid expression')
        return

    def menu(self):
        if self.string[0] == '/':
            if self.string == '/exit':
                self._exit()
                return
            elif self.string == '/help':
                self.help()
                return
            else:
                print('Unknown command')
                return

    def take(self):
        for key in self.var_dict.keys():
            if self.strlist_1[0] == key:
                print(self.var_dict[key])
                return self.var_dict[key]
        print('Unknown variable')
        return

    def help(self):
        print('The program calculates expression with eval()')
        return

    def _exit(self):
        print('Bye!')
        exit()

while True:
    string = Calculate(str(input()).strip(' '))
    string.main()

