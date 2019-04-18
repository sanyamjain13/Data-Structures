class node:

    def __init__(self,e):

        self.element=e
        self.next=None
        self.prev=None

class db_ll:

    def __init__(self):

        self.size=0
        self.header=node(None)
        self.trailer=node(None)
        self.header.next=self.trailer
        self.trailer.prev=self.header

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

    def add_first(self,e):

        return self.insert_between(e,self.header,self.header.next)

    def add_last(self,e):

        return self.insert_between(e,self.trailer.prev,self.trailer)
    
    def add_after(self,e,elt):

        #e = element after which need to add
        #elt- that element needed to be add
        
        temp=self.header.next
        while(temp.element!=e):
            temp=temp.next
            if temp==self.trailer:
                break

        if(temp==self.trailer):
            print('ELEMENT NOT FOUND')
        else:
            current=temp
            succ=temp.next
            self.insert_between(elt,current,succ)

    def add_before(self,e,elt):

        #e = element after which need to add
        #elt- that element needed to be add
        
        temp=self.header.next
        while(temp.element!=e):
            temp=temp.next
            if temp==self.trailer:
                break
        if(temp==self.trailer):
            print('ELEMENT NOT FOUND')        

        else:
            current=temp
            prev=temp.prev
            self.insert_between(elt,prev,current)

    def delete_first(self):

        if self.isEmpty():
            print('LIST IS EMPTY')
        else:
            self.delete(self.header.next)        

    def delete_last(self):

        if self.isEmpty():
            print('LIST IS EMPTY')
        else:
            self.delete(self.trailer.prev)        
    
    def delete_element(self,e):

        temp=self.header

        if (self.isEmpty()):
            print('UNDERFLOW')
        else:

            while(temp.element!=e):
                temp=temp.next
                if temp==self.trailer:
                    break

            if temp==self.trailer:
                print('ELEMENT NOT FOUND')
            else:
                self.delete(temp)

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

def main():
    
    d=db_ll()
    print('-----------------------------------------------')

    print('1.ADD ELEMENT AT STARTING')
    print('2.ADD ELEMENT AT LAST')
    print('3.ADD ELEMENT AFTER SOME ELEMENT')
    print('4.ADD ELEMENT BEFORE SOME ELEMENT')
    print('5.DELETE FIRST ELEMENT')
    print('6.DELETE LAST ELEMENT')
    print('7.DELETE A PARTICULAR ELEMENT')
    print('8.PRINT LIST')

    print('-----------------------------------------------')
    
    while(True):
        ch=int(input('ENTER YOUR CHOICE : '))

        if ch==1:
            e=int(input('ELEMENT TO ADD : '))
            d.add_first(e)

        elif ch==2:
            e=int(input('ELEMENT TO ADD : '))
            d.add_last(e)

        elif ch==3:
            elt=int(input('ELEMENT TO ADD : '))
            e=int(input('ELEMENT AFTER WHICH TO ADD : '))
            d.add_after(e,elt)

        elif ch==4:
            elt=int(input('ELEMENT TO ADD : '))
            e=int(input('ELEMENT BEFORE WHICH TO ADD : '))
            d.add_before(e,elt)
            
        elif ch==5:
            d.delete_first()

        elif ch==6:
            d.delete_last()

        elif ch==7:
            e=int(input('ELEMENT TO DELETE : '))
            d.delete_element(e)

        elif ch==8:
            print(d)

        else:
            exit()
        print('-------------------------')
            
main()
