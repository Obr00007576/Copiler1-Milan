import parser
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
                self.push(a//b)
                pass
            elif(de[0] == 'OUT'):
                print(self.pop())
                pass
            elif(de[0] == 'STOP'):
                break
            self.cp+=1
            


if __name__=='__main__':
    ma=PMachine()
    data = '''begin
        a:=3.5;
        int b := a+(int)(a+3.4);
    end
    '''
    p_code,mem = parser.parse(data)
    print(mem)

    for da in mem.keys():
        if type(da) is int:
            ma.push(da)
        elif type(da) is float:
            ma.push(0.)
        else:
            if mem[da][0]=='INT':
                ma.push(0)
            elif mem[da][0]=='FLOAT':
                ma.push(0.)
    ma.cp=len(ma.stack)
    for i in range(len(p_code)):
        print(f"{i}: {p_code[i]}")
        ma.push(p_code[i])
    ma.dp=len(ma.stack)

    
    