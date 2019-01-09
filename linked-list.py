class Node:
    '''
    objective: To create a node in linked list
    '''

    def __init__(self,data):

        '''
        objective: To initialise a class object
        input parameters:
                        self:implicit parameter
                        data: The data we need to add in linked list
        return: None
        '''

        self.data=data
        self.next=None

class Linkedlist:
    '''
    objective: To represent linked list
    '''
    def __init__(self):
        '''
        objective: To initialise a class object
        input parameter:
                        self:implicit parameter
                        head:
        '''
        self.head=None

    def insertNode(self,value):
        '''
        objective: To insert node in the beginning
        input parameters:
                        self:implicit parameter
                        value:value to insert at the beginning
                        
        '''

        temp=Node(value)
        temp.next=self.head #putting the current head in the new nodes next
        self.head=temp  #and now making head pointing to the new element head

    def insertAtEnd(self,temp,value):
        '''
        Objective: To add a node at the end of a linked list
        Input:
            self: Implicit object of class LinkedList
            value: Value to be inserted
            temp : Current node
        Return Value: None
        '''
        #Approach: Recurssively
        if temp == None:
            self.head = Node(value)
        elif temp.next == None:
            temp.next = Node(value)
        else:
            return self.insertAtEnd(temp.next,value)

    def deleteNodeIterative(self,value):
        '''
        objective: To delete node from the list iteratively
        input parameters:
           self:implicit parameter
           value: The value that to be deleted
        return: the node that is deleted
        '''
        if self.head==None:
            print("List is empty")
        elif self.head.data==value:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            return 
        else:
            previous=self.head
            current=previous.next
            while current!=None:
                if current.data==value:
                    previous.next=current.next
                    current.next=None
                    return
                previous=current
                current=current.next
            print(value+' not found')

    def deleteNodeRecursive(self,previous,current,value):
        '''
        objective: To delete node from the list recursively
        input parameters:

           self:implicit parameter
           previous: element that is head in beginning
           current: it is the element the head element is pointing to
           value: the value that to be deleted
        

        '''
        if previous==None:
            print('empty')

        elif previous.data==value:
            self.head=current

        elif previous.next==None:
            print('empty')

        elif previous.next.data==value:
            previous.next=current.next
            
        else:
            return self.deleteNode(previous.next,current.next,value)      
            
            
    def __str__(self):

        '''
        objective: to print the list
        input parameters:
                        self:implicit parameter
        '''
        
        if self.head==None:
            print("list is empty")

        else:
            temp=self.head
            lst=" "
            while temp!=None:
                lst+=str(temp.data)+"->"
                temp=temp.next
            return lst

if __name__=='__main__':
    l=Linkedlist()

    while True:

        print("1. INSERT NODE IN THE BEGINNING \n")
        print("2. DELETE NODE FROM THE BEGINNING \n")
        print("3. DISPLAY YOUR LIST \n")
        print("4. INSERT NODE AT THE END \n")
        print("ENTER YOUR CHOICE :",end=" ")
        ch=int(input())            

        if ch==1:
            print('ENTER NUMBER OF VALUES TO INSERT :',end=" ")
            number=int(input())
            for i in range(number): 
                value=int(input())
                l.insertNode(value)
        elif ch==2:
            print("2.1 ITERATIVELY \n")
            print("2.2 RECURSIVELY\n")
            ch1=float(input('ENTER CHOICE HOW TO DELETE :'))

            if ch1==2.1:

                print('ENTER THE VALUE TO DELETE :', end=" ")
                value=int(input())
                l.deleteNodeIterative(value)

            if ch==2.2:

                print('ENTER THE VALUE TO DELETE :', end=" ")
                value=int(input())
                l.deleteNodeRecursive(l.head,l.head.next,valuue)
                
        elif ch==3:
            print(l)

        elif ch==4:
            print('ENTER NUMBER OF VALUES TO INSERT :',end=" ")
            number=int(input())
            for i in range(number): 
                value=int(input())
                l.insertAtEnd(l.head,value)

        else:
            print("Invalid choice")

    
class Node:
    '''
    objective: To create a node in linked list
    '''

    def __init__(self,data):

        '''
        objective: To initialise a class object
        input parameters:
                        self:implicit parameter
                        data: The data we need to add in linked list
        return: None
        '''

        self.data=data
        self.next=None

class Linkedlist:
    '''
    objective: To represent linked list
    '''
    def __init__(self):
        '''
        objective: To initialise a class object
        input parameter:
                        self:implicit parameter
                        head:
        '''
        self.head=None

    def insertNode(self,value):
        '''
        objective: To insert node in the beginning
        input parameters:
                        self:implicit parameter
                        value:value to insert at the beginning
                        
        '''

        temp=Node(value)
        temp.next=self.head #putting the current head in the new nodes next
        self.head=temp  #and now making head pointing to the new element head

    def insertAtEnd(self,temp,value):
        '''
        Objective: To add a node at the end of a linked list
        Input:
            self: Implicit object of class LinkedList
            value: Value to be inserted
            temp : Current node
        Return Value: None
        '''
        #Approach: Recurssively
        if temp == None:
            self.head = Node(value)
        elif temp.next == None:
            temp.next = Node(value)
        else:
            return self.insertAtEnd(temp.next,value)

    def deleteNodeIterative(self,value):
        '''
        objective: To delete node from the list iteratively
        input parameters:
           self:implicit parameter
           value: The value that to be deleted
        return: the node that is deleted
        '''
        if self.head==None:
            print("List is empty")
        elif self.head.data==value:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            return 
        else:
            previous=self.head
            current=previous.next
            while current!=None:
                if current.data==value:
                    previous.next=current.next
                    current.next=None
                    return
                previous=current
                current=current.next
            print(value+' not found')

    def deleteNodeRecursive(self,previous,current,value):
        '''
        objective: To delete node from the list recursively
        input parameters:

           self:implicit parameter
           previous: element that is head in beginning
           current: it is the element the head element is pointing to
           value: the value that to be deleted
        

        '''
        if previous==None:
            print('empty')

        elif previous.data==value:
            self.head=current

        elif previous.next==None:
            print('empty')

        elif previous.next.data==value:
            previous.next=current.next
            
        else:
            return self.deleteNode(previous.next,current.next,value)      
            
            
    def __str__(self):

        '''
        objective: to print the list
        input parameters:
                        self:implicit parameter
        '''
        
        if self.head==None:
            print("list is empty")

        else:
            temp=self.head
            lst=" "
            while temp!=None:
                lst+=str(temp.data)+"->"
                temp=temp.next
            return lst

if __name__=='__main__':
    l=Linkedlist()

    while True:

        print("1. INSERT NODE IN THE BEGINNING \n")
        print("2. DELETE NODE FROM THE BEGINNING \n")
        print("3. DISPLAY YOUR LIST \n")
        print("4. INSERT NODE AT THE END \n")
        print("ENTER YOUR CHOICE :",end=" ")
        ch=int(input())            

        if ch==1:
            print('ENTER NUMBER OF VALUES TO INSERT :',end=" ")
            number=int(input())
            for i in range(number): 
                value=int(input())
                l.insertNode(value)
        elif ch==2:
            print("2.1 ITERATIVELY \n")
            print("2.2 RECURSIVELY\n")
            ch1=float(input('ENTER CHOICE HOW TO DELETE :'))

            if ch1==2.1:

                print('ENTER THE VALUE TO DELETE :', end=" ")
                value=int(input())
                l.deleteNodeIterative(value)

            if ch==2.2:

                print('ENTER THE VALUE TO DELETE :', end=" ")
                value=int(input())
                l.deleteNodeRecursive(l.head,l.head.next,valuue)
                
        elif ch==3:
            print(l)

        elif ch==4:
            print('ENTER NUMBER OF VALUES TO INSERT :',end=" ")
            number=int(input())
            for i in range(number): 
                value=int(input())
                l.insertAtEnd(l.head,value)

        else:
            print("Invalid choice")

    
