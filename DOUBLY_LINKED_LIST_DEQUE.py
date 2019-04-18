'''
implementing DB-LL using header and trailer node
which is just an empty nodi with initially header pointing
to trailer & trailer pointing to header

node just after the header is the first node
node before the trailer is the last node

in DB-LL there are 2 reference pointers next and previous
'''

class node:

    def __init__(self,e):

        self.element=e
        self.prev=None
        self.next=None

class double_linked_list:

    def __init__(self):

        self.header=node(None)
        self.trailer=node(None)
        self.header.next=self.trailer
        self.trailer.prev=self.header
        self.size=0

    def isEmpty(self):

        if self.size==0:
            return True

    def length(self):

        return self.size

    def insert_between(self,e,predecessor,successor):

        x=node(e)
        predecessor.next=x
        successor.prev=x
        x.next=successor
        x.prev=predecessor
        self.size+=1
        return x

    def delete(self,Node):
        pre=Node.prev
        succ=Node.next
        pre.next=succ
        succ.prev=pre
        self.size-=1
        elt=Node.element
        Node.element=Node.prev=Node.next=None
        return elt

    def __str__(self):

        temp=self.header.next
        lst=" "
        size=self.size
        
        if self.isEmpty():
            print('EMPTY')
        else:

            while(size!=0):
                lst+=str(temp.element)+"->"
                temp=temp.next
                size=size-1

            return lst
        

'''
inheriting double_ll class to access its methods to implement double ended queues
we dont need to specify explicitly the init fn for this as it will inherit from base class
'''

#IMPLEMENTING DOUBLE ENDED QUEUES USING DOUBLY LINKED LIST CLASS

class db_ll_deque(double_linked_list):

    #if we dont write this it would automatically invoke parent class constructor

    def __init__(self):
        
        double_linked_list.__init__(self)
        
    def first(self):
        if self.isEmpty():
            print('QUEUE IS EMPTY')
        else:
            return self.header.next.element

    def last(self):
        if self.isEmpty():
            print('QUEUE IS EMPTY')
        else:
            return self.trailer.prev.element
    

    def insert_first(self,e):

        self.insert_between(e,self.header,self.header.next)

    def insert_last(self,e):

        self.insert_between(e,self.trailer.prev,self.trailer)

    def delete_first(self):
        
        if self.isEmpty():
            print('Empty :(')

        else:
            return self.delete(self.header.next)

    def delete_last(self):
    
        if self.isEmpty():
            print('Empty :(')

        else:
            return self.delete(self.trailer.prev)



def main():
    d=db_ll_deque()
    print('---------------------------------------------')
    print('\\\ DOUBLE ENDED QUEUES // \n')
    print('1. INSERT IN BEGINNING')
    print('2. INSERT IN LAST')
    print('3. DELETE FROM BEGINNING')
    print('4. DELETE FROM LAST')
    print('5. PRINT YOUR QUEUE')
    print('6. EXIT PROGRAM')
    print('---------------------------------------------')
    while True:
        #print('\n')
        ch=int(input('YOUR CHOICE : '))
        if ch==1:
            inp=int(input('ENTER ELEMENT: '))
            d.insert_first(inp)
        elif ch==2:
            inp=int(input('ENTER ELEMENT: '))
            d.insert_last(inp)
        elif ch==3:
            print('DELETED FIRST ELEMENT: ',d.delete_first())
        elif ch==4:
            print('DELETED LAST ELEMENT: ',d.delete_last())
        elif ch==5:
            print('QUEUE: ',d)
        else:
            print('EXITED SUCCESSFULLY')
            break

        print('--------------------------------------------')
            

main()




















    
