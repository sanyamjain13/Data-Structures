'''
implementing queue using linked list
'''

class node:

    def __init__(self,e):

        self.element=e
        self.next=None

class LList_Queue:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def isEmpty(self):

        if self.size==0:
            return True

    def enq(self,e):

        elt=node(e)
        
        if self.isEmpty():
            self.head=elt
            self.tail=elt
            self.size+=1
        else:
            self.tail.next=elt
            self.tail=elt
            self.size+=1

    def deq(self):

        if self.isEmpty():
            print('QUEUE IS EMPTY')
        else:
            ans=self.head.element
            self.head=self.head.next
            self.size-=1
            
            if self.isEmpty():
                self.tail=None #removed head had been the tail
            
            return ans

    def first(self):
        return self.head.element

    def last(self):
        return self.tail.element

    def length(self):
        return self.size

    def search(self,e):

        head=self.head
        for i in range(self.size):
            if head.element==e:
                print('ELEMENT FOUND AT POSITION ',i+1)
                break
            else:
                head=head.next
        print('ELEMENT NOT FOUND')

    def __str__(self):

        lst="QUEUE : "
        temp=self.head
        size=self.size
        
        if size==0:
            print('YOUR QUEUE IS EMPTY')

        else:
            while(size!=0):

                if size==1:
                    lst+=str(temp.element)+" -> None "
                else:  
                    lst+=str(temp.element)+" -> "
                    temp=temp.next

                size=size-1

            return lst

def main():
    q=LList_Queue()
    lst=list(map(int,' '.join(input('ENTER ITEMS TO ADD : ')).split()))
    print('------------------------------------\n')
    for i in range(len(lst)):
        q.enq(lst[i])
        
    print(q)
    q.search(3)
    print('LENGTH : ',q.length())

    print('AFTER DELETING ELEMENT: ', q.first())
    q.deq()
    print(q)
    
    print('first elt: ',q.first())
    print('last elt: ',q.last())

main()
    
















            
    












    
