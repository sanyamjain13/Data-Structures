'''
implementing stack using LINKED LIST
'''
class node:

    def __init__(self,e):
        self.element=e
        self.next=None

    def __str__(self):
        return str(self.element)
    
class linked_list:

    def __init__(self):

        self.head=None
        self.size=0

    def isEmpty(self):

        if self.size==0:
            return True
        
    def push(self,e):

        x=node(e)
        x.next=self.head
        self.head=x
        self.size+=1

    def pop(self):

        if self.isEmpty():
            print('stack is empty')
        else:
            answer=self.head.element
            self.head=self.head.next
            self.size-=1
            return answer
        
    def search(self,e):
        
        temp=self.head

        for i in range(self.size):
            if temp.element==e:
                res='ELEMENT '+str(e)+' FOUND AT POSITION '+str(i+1)
                print(res)
                break
            else:
                temp=temp.next
                
        print('ELEMENT NOT FOUND')        
        
    def length(self):
        return self.size

    def top(self):
        if self.size==0:
            print('stack is empty')
        else: 
            return self.head.element

    def __str__(self):

        x=self.size
        
        if self.size==0:
            print('STACK IS EMPTY')
        lst="STACK: "
        temp=self.head
        while(x!=0):
            lst+=str(temp.element)+"->"
            temp=temp.next
            x-=1
        return lst
        
        
def main():
    print('iIMPLEMENTING STACK USING LINKED LIST')
    print('-------------------------------------- \n')
    l=linked_list()

    lst=list(map(int,' '.join(input('ENTER ELEMENTS TO PUSH ON STACK: ')).split()))

    for i in range(len(lst)):
        l.push(lst[i])

    print(l)
    
    l.search(3)
    
    print('ELEMENT POPPED : ',l.pop())

    print(l)

    print('LENGTH: ',l.length())

    print('TOP: ',l.top())

main()

        
        
    
    
