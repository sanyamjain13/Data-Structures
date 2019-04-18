class queue:

    default_size=10
    def __init__(self):
        self.data=[None]*queue.default_size
        self.front=0
        self.rear=0
        self.size=0

    def is_Empty(self):
        if(self.size==0):
            return True

    def front_index(self):
        return self.front

    def last_index(self):
        return self.rear

    def enq(self,elt):
        if (self.rear==len(self.data)):
            print('QUEUE IS FULL, RESIZING QUEUE')
            self.resize(5)

        self.data[self.rear]=elt
        self.rear=self.rear+1
        self.size+=1
            
    def deq(self):

        if self.is_Empty():
            print('QUEUE IS EMPTY')
        else:
            print('REMOVED ELEMENT: ',self.data.pop(self.front))
            self.data.insert(self.front,None)
            self.front=(self.front+1)%len(self.data)
            self.size-=1

    def resize(self,size):

        lst=[None]*(size)
        self.data.extend(lst)

    def __str__(self):

        return 'UPDATED LIST: '+str(self.data)

def main():
    q=queue()
    for i in range(10):
        q.enq(i+1)
    print(q)
    
    for i in range(5):
        q.deq()      

    print(q)
              
    print('front: ',q.front_index())
    print('rear: ',q.last_index())
if __name__=='__main__':
    main()



    
