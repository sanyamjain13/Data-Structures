class deque:

    def __init__(self):

        self.data=[]
        self.front=0
        self.rear=0
    
    def add_first(self,e):

        self.data.insert(0,e)
        self.front=0

    def add_last(self,e):

        self.data.insert(len(self.data),e)
        self.rear=len(self.data)-1

    def is_Empty(self):

        if len(self.data)==0:
            return True

    def delete_first(self):

        if self.is_Empty():
            print('QUEUE IS EMPTY')
        else:
            print('DELETED FIRST ELEMENT : ',self.data.pop(0))
            self.front=0

    def delete_last(self):

        if self.is_Empty():
            print('QUEUE IS EMPTY')
        else:
            print('DELETED LAST ELEMENT : ',self.data.pop(-1))
            self.rear=len(self.data)-1
            
    def first(self):

        if self.is_Empty():
            print('QUEUE IS EMPTY')
        else:
            return(self.data[self.front])

    def last(self):

        if self.is_Empty():
            print('QUEUE IS EMPTY')
        else:
            return(self.data[self.rear])
        
    def __str__(self):
        return 'UPDATED LIST : '+str(self.data)
    
def main():

    d=deque()
    d.add_first(1)
    d.add_first(2)
    d.add_first(3)
    
    d.add_last(4)
    d.add_last(5)
    d.add_last(6)

    print(d)
    
    d.delete_first()
    print(d)
    d.delete_last()
    print(d)
    
    print('FIRST ELEMENT : ',d.first())
    print('LAST ELEMENT : ',d.last())

main()
    
    
