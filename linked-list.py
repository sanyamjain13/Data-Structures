import sys

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
        temp.next=self.head
        self.head=temp


    def deleteNode(self):
        '''
        objective: To delete node from the beginning
        input parameters:
                        self:implicit parameter
        return: the node that is deleted
                        
        '''
        if self.head==None:
            print("List is empty")

        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data

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
                lst+=" "+str(temp.data)
                temp=temp.next
            return lst

if __name__=='__main__':
    l=Linkedlist()

    while True:

        print("1. INSERT NODE IN THE BEGINNING \n")
        print("2. DELETE NODE FROM THE BEGINNING \n")
        print("3. DISPLAY YOUR LIST \n")
        print("4. ENTER 0 TO EXIT \n")
        print("   ENTER YOUR CHOICE :",end=" ")
        ch=int(input())            
        if ch==1:
            print('   ENTER NUMBER OF VALUES TO INSERT : ',end=" ")
            number=int(input())
            for i in range(number):
                value=int(input())
                l.insertNode(value)
        elif ch==2:
            l.deleteNode()
        elif ch==3:
            print(l)
        else:
            exit()

    
