class heapSort:
    '''
    objective: This class represents maximum heap sort
    '''
    def __init__(self,lst):
        '''
        objective: To initialise list which need to be sorted and the length
        input parameters:
                        self:implicit parameter
                        lst:list of numbers
                        length:length of the list
        '''
        self.lst=lst
        self.length=len(lst)

    def left(self,n):
        '''
        objective:returns the index of left child
        inpur parameters:
                        self:implicit parameter
                        n=index of parent
        return: index of left child
        '''

        return 2*n+1

    def right(self,n):
        '''
        objective:returns the index of right child
        inpur parameters:
                        self:implicit parameter
                        n=index of parent
        return: index of right child
        '''

        return 2*n+2

    def parent(self,n):
        '''
        objective:returns the index of left child
        inpur parameters:
                        self:implicit parameter
                        n=index of child
        return: index of parent
        '''

        if n%2==0:
            return n//2-1
        return n//2

    def max_heapify(self,i):
        '''
        objective:to heapify subtree rooted at i
        input parameters:
                        self:implicit parameters
                        i:index of root
                    return:none
        '''
        if i<0:
            return
        l=self.left(i)
        r=self.right(i)
        largest=i

        if l<self.length and self.lst[l]>self.lst[largest]:
            largest=l

        if r<self.length and self.lst[r]>self.lst[largest]:
            largest=r

        if i!=largest:
            self.lst[i],self.lst[largest]=self.lst[largest],self.lst[i]
            self.max_heapify(self.parent(i))
            self.max_heapify(largest)

    def buildheap(self):
        for i in range(0,self.length//2):
            self.max_heapify(i)
        print('After Heapify (max heap) ->',self.lst,'\n')

    
    
    def delete(self):
        print('Before Deletion ->',self.lst)
        self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
        self.lst.pop()
        for i in range(0,len(self.lst)//2):
            self.max_heapify(i)
        print('After Deletion ->',self.lst,'\n')


    def insert(self,element):
        print('Before Insertion ->',self.lst)
        self.lst.append(element)
        for i in range(0,len(self.lst)//2):
            self.max_heapify(i)
        print('After Insertion ->',self.lst)
        
        
if __name__ =='__main__':
    h=heapSort([1,16,20,30,50,2])
    h.buildheap()
    h.delete()
    h.insert(999)
