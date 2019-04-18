class stack:

    def __init__(self):

        self.data=[]
        self.top=-1
        
    def isEmpty(self):

        if self.top==-1:
            return True
        else:
            return False

    def push(self,elt):
        self.data.append(elt)
        self.top=self.top+1

    def pop(self):
        if self.isEmpty():
            print('STACK IS EMPTY, UNDERFLOW CONDITION')
        else:
            self.data.pop(-1)
            self.top=self.top-1

    def length_of_stack(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
        
def check_string_balance(string_lst,obj):

    for i in range(len(string_lst)):
        if(string_lst[i]=='('):
            obj.push('(')
        elif(string_lst[i]==')'):
            if(obj.top==-1):
                obj.top=obj.top-1
            else:
                obj.pop()
        else:
            continue
            
    if obj.isEmpty():
        print('STRING IS BALANCED')
    else:
        print('STRING UNBALANCED')

def main():

    s=stack()
    print('DEMO OUTPUTS FOR STACK CLASS: ')
    print('----------------------------------------------')
    print('PUSHING 1 , 2 ,3 ON STACK')
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print('CHECKING IF STACK IS EMPTY: ')
    print(s.isEmpty())
    print(s.length_of_stack())
    s.pop()
    print('AFTER POPPING',s)
    print('---------------------------------------------- \n')

    print('STRING CHECKING IF BALANCED OR NOT, FOR EG:\n->( HE IS A BOY ) IS BALANCED \n->( SHE IS A GIRL ) ) IS UNBALLANCED \n')
    print('------------------------------------------------------ \n')

    while True:
        lstString=list(map(str,input('INPUT THE STRING WITH SPACES :  ').split()))
        check_string_balance(lstString,s)

        ext=int(input('press 1 for exit : '.upper()))
        if ext==1:
            print('EXITED')
            break
        else:
            continue
    print('------------------------------------------------------ \n')
    
if __name__=='__main__':
    main()
