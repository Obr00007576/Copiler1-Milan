import parser
import sys
class PMachine:
    stack=[]
    cp=0
    dp=0
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        t=self.stack[-1]
        del self.stack[-1]
        return t
    def run(self):
        print("\n-----------CODE BEGIN-----------")
        while True:
            pc=self.stack[self.cp]
            de=pc.split()
            if(de[0] == 'LOAD'):
                self.push(self.stack[int(de[1])])
                pass
            elif(de[0] == 'STORE'):
                self.stack[int(de[1])] = self.pop()
                pass
            elif(de[0] == 'CMP'):
                b=self.pop()
                a=self.pop()
                if de[1] == '0':
                    if a == b:
                        self.push(1)
                    else:
                        self.push(0)
                elif de[1] == '1':
                    if a < b:
                        self.push(1)
                    else:
                        self.push(0)
                elif de[1] == '2':
                    if a <= b:
                        self.push(1)
                    else:
                        self.push(0)
                elif de[1] == '3':
                    if a > b:
                        self.push(1)
                    else:
                        self.push(0)
                elif de[1] == '4':
                    if a >= b:
                        self.push(1)
                    else:
                        self.push(0)
                elif de[1] == '5':
                    if a != b:
                        self.push(1)
                    else:
                        self.push(0)
            elif(de[0] == 'JMP_NO'):
                b=self.pop()
                if b==0:
                    self.cp+=int(de[1])
                    continue
                pass
            elif(de[0] == 'JMP'):
                self.cp+=int(de[1])
                continue
                pass
            elif(de[0] == 'ADD'):
                b=self.pop()
                a=self.pop()
                self.push(a+b)
                pass
            elif(de[0] == 'SUB'):
                b=self.pop()
                a=self.pop()
                self.push(a-b)
                pass
            elif(de[0] == 'MULT'):
                b=self.pop()
                a=self.pop()
                self.push(a*b)
                pass
            elif(de[0] == 'DIV'):
                b=self.pop()
                a=self.pop()
                if type(a) is int:
                    self.push(a//b)
                elif type(a) is float:
                    self.push(a/b)
                pass
            elif(de[0] == 'OUT'):
                print(self.pop())
                pass
            elif(de[0] == 'ITOF'):
                self.stack[-1]=float(self.stack[-1])
            elif(de[0] == 'FTOI'):
                self.stack[-1]=int(self.stack[-1])
            elif(de[0] == 'STOP'):
                break
            self.cp+=1
        print("-----------CODE END-----------\n")
    def pre_compile(self, code):
        p_code,mem = parser.parse(code)
        print('-----------MEMORY TABLE-----------')
        for k in mem.keys():
            if type(k) is int or type(k) is float:
                print(f"{mem[k][1]}: \tCONST_VAL: {k}, TYPE: {mem[k][0]}")
            else:
                print(f"{mem[k][1]}: \tVAR_NAME: {k}, TYPE: {mem[k][0]}")
        for da in mem.keys():
            if type(da) is int:
                self.push(da)
            elif type(da) is float:
                self.push(da)
            else:
                if mem[da][0]=='INT':
                    self.push(0)
                elif mem[da][0]=='FLOAT':
                    self.push(0.)
        self.cp=len(self.stack)
        print('\n-----------P_CODE-----------')
        for i in range(len(p_code)):
            print(f"{i}: \t{p_code[i]}")
            self.push(p_code[i])
        self.dp=len(self.stack)
            


if __name__=='__main__':
    ma = PMachine()
    code = open(sys.argv[1], 'r').read()
    ma.pre_compile(code)
    ma.run()
