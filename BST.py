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
    objective: To create a bst
    '''
    def __init__(self,root):
        '''

        '''
        self.root=None

    def insertNodeWrapper(self,value):
        '''

        '''
        if self.root==None:
            self.root=Node(value)

        else:
            self.insertNode(self.root,value)

    def insertNode(self,current,value):
        '''

        '''
        if current.data<value:

            if current.right==None:
                current.right=Node(value)

            else:
                return self.insertNode(current.right,value)

        else:
            current.data>value:

                if current.left==None:
                    current.left=Node(value)
                else:
                    return self.insertNode(current.left,value)

    def inorder(self,current):
        '''
        
        '''
        self.inorder(current.left)
        print(current.data, ' - ')
        self.inorder(current.right)



if __name__=='__main__':
    t=BST()
    for i in range(3):
        value=int(input())
        t.insertNodeWrapper(value)
    
    t.inorder(current.root)    
