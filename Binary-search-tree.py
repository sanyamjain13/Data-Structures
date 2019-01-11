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
        self.left=None
        self.right=None

class BST:
    '''
    objective: To create a binary search tree
    '''
    def __init__(self):
        '''
        objective: To initialise a class object
        input parameters:
                        self:implicit parameter
                        root: it is the root element of the BST
        '''
        self.root=None

    def insertNodeWrapper(self,value):
        '''
        objective: To insert a node using wrapper function which calls another function to perform desired task
        input parameters:
                        self: implicit parameter
                        vale: the value that need to be inserted in a tree
        '''
        if self.root==None:
            self.root=Node(value) #if emplty then insert a node at root

        else:
            self.insertNode(self.root,value) # if not empty call function insertNode

    def insertNode(self,current,value):
        '''
        objective: To insert a node in the left or right of the root node if tree is not empty
        input parameter:
                        self: Implicit parameter
                        current: It is the current root node of a tree or a subtree
                        value: Va;ue to be insrted on left or right of a root node of a tree or a subtree
        '''
        if current.data<value: #if value is greater than root node then approach to RHS of root

            if current.right==None:
                current.right=Node(value)

            else:
                return self.insertNode(current.right,value)

        else: #if value is greater than root node then approach to RHS of root
            if current.left==None:
                current.left=Node(value)
            else:
                return self.insertNode(current.left,value)

    def inorder(self,current,Tstring=""):
        '''
        Objective: To traverse a binary tree in inorder traversal which is LEFT->PARENT->RIGHT
        input parameters:
                        self:implicit parameter
                        current: It is the current node from where the traversing is happening
        '''
        if current.left!=None:
            Tstring = self.inorder(current.left,Tstring)
        Tstring+="->"+str(current.data)
        if current.right!=None:
            Tstring = self.inorder(current.right,Tstring)
        return Tstring


    def __str__(self):

        if self.root==None:
            print("Tree is empty")

        else:
            return self.inorder(self.root,"")    


if __name__=='__main__':

    t=BST()
    while True:
        print("--------------------------------------------\n")
        print("1.INSERT A NODE IN A BINARY TREE \n")
        print("2.TRAVERSE A BINARY TREE IN INORDER \n ")
        print("3.EXIT PROGRAM \n")
        print("--------------------------------------------")
        ch=int(input("ENTER YOUR CHOICE : "))

        if ch==1:
            
            num=int(input('\nENTER NUMBER OF VALUES TO ENTER : '))
            for i in range(num):
                value=int(input("VALUE-"+ str(i+1)+' : '))
                t.insertNodeWrapper(value)
        if ch==2:
            print("INORDER TRAVERSAL :",t)

        if ch==3:
            exit()
            



