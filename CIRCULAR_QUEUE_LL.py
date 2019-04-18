'''
implementing circular queue where last element refrences to the first element

make refrence to head element by pointing the tails next to first element
no need to explicitly maintain head pointer

'''

class node:

    def __init__(self,e):
        self.element=e
        self.next=None

class circular_Q:

    def __init__(self):

        self.tail=None
        self.size=0

    def isEmpty(self):

        if self.size==0:
            return True

    #adding elements
    def enq(self,e):

        elt=node(e)
        
        #single element pointing itself
        if self.isEmpty():
            self.tail=elt
            self.tail.next=elt

        else:

            #new element at tail which points to previous head, and old tail points to new element
            #finally new element becomes the tail
            
            elt.next=self.tail.next
            self.tail.next=elt
            self.tail=elt

        self.size+=1

    def deq(self):

        if self.isEmpty():
            print('circular queue is empty')
        
        if self.size==1:
            #when only one element present make tail=none
            
            ans=self.tail.element
            self.tail=None
            self.size-=1
            return ans

        else:
            '''
            otherwise make present heads next element,the new head by
            refrencing the tails next to oldhead's next element
            '''
            
            oldhead=self.tail.next
            ans=oldhead.element
            self.tail.next=oldhead.next
            self.size-=1
            return ans
    

    def rotate(self):

        #shifting element 1 at last (make head the tail)
        
        if self.size>0:
            self.tail=self.tail.next

    def length(self):
        return self.size

    def search(self,e):

        head=self.tail.next
        for i in range(self.size):
            if head.element==e:
                print('ELEMENT FOUND AT POSITION ',i+1)
                break
            else:
                head=head.next
        print('ELEMENT NOT FOUND')
        
    def head(self):
        return self.tail.next.element

    def last(self):
        return self.tail.element
    
    def __str__(self):

        lst="CIRCULAR QUEUE :  "
        head=self.tail.next
        size=self.size
        
        if self.isEmpty():
            print('THE QUEUE IS EMPTY')
            
        else:
            while(size!=0):
                lst+=str(head.element)+"->"
                head=head.next
                size=size-1

            return lst

def main():
    c=circular_Q()
    
    lst=list(map(int,' '.join(input('ENTER ITEMS TO ADD : ')).split()))

    print('------------------------------------\n')

    for i in range(len(lst)):
        c.enq(lst[i])
    print(c)

    e=int(input('Element to search in Queue : '))
    c.search(e)
    
    print('\nDeleted element',c.deq())
    print(c)

    print('\nLength :',c.length())
    print('\nHead :',c.head())
    print('\nTail: ',c.last())

    print('\nAfter rotating')
    c.rotate()
    print(c)
    
main()
    
            
            
