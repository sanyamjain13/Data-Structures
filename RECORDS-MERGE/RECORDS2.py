import pickle,random,os
from RECORDS1 import *

def main():
    f=open("record.txt",'rb')
    n=pickle.load(f)
    print("NO OF RECORDS IN FILE1 is: ",n)
    print("*****************************\n")
    f.close()
    
    blocksize=int(input('ENTER THE BLOCKSIZE : '))

    f=open('file1.txt','rb')
    f1=open('file2.txt','wb')
    f2=open('file3.txt','wb')

    f3=open("blocksize.txt","wb")
    pickle.dump(blocksize,f3)
    f3.close()
    #BLOCKS WILL TELL THAT HOW MANY BLOCKS OF ELEMENT WITH BLOCKSIZE IS THERE.IF 12 RECORDS THEN THERE ARE 3 BLOCKS OF SIZE 4(4 ELEMENTS)

    blocks=n//blocksize
    left=n%blocksize

    '''
    HERE WE ARE MAKING TWO FILES AND DISTRIBUTING 4 RECORDS IN FIRST FILE AND THEN
    OTHER 4 IN OTHER FILE. IT WILL GO ALTERNATIVELY. INITIALLY THE BLOCKSIZE=4 THATS WHY 4
    '''
    k=0
    for i in range(blocks):
        lst=[]
        for j in range(blocksize):
            lst.append(pickle.load(f))
        t=sorted(lst,key=lambda x:x.getkey())
        k=i
        
        for elt in t:
            if i%2==0:
                pickle.dump(elt,f1)
            else:
                pickle.dump(elt,f2)

    '''
    IF THERE IS ODD NUMBER OF RECORDS THEN THERE WILL BE SOME RECORDS WHICH WILL BE LEFT
    FOR EG- IF 13 RECORDS THEN ALTERNATIVELY 4 4 CAN BE ADDED, BUT ONE WILL BE LEFT. FOR THAT
    THIS LOOP WORKS
    '''
    if left>0:
        lst=[]

        for i in range(left):
            lst.append(pickle.load(f))
        t=sorted(lst,key=lambda x:x.getkey())

        for elt in t:
            if (k+1)%2==0:
                pickle.dump(elt,f1)
            else:
                pickle.dump(elt,f2)
    f.close()
    f1.close()
    f2.close()

def printRecordsFile2():
    '''
    printing the records in FILE2.txt
    '''
    
    f2=open('file2.txt','rb')
    len_f2=os.stat("file2.txt")

    print("\n**********RECORDS IN FILE2*********\n")
    while f2.tell()!=len_f2.st_size:
        print(pickle.load(f2))
    
    f2.close()
    
def printRecordsFile3():
    '''
    printing the records in FILE3.txt
    '''
    f3=open('file2.txt','rb')
    len_f3=os.stat("file3.txt")
    
    print("\n**********RECORDS IN FILE3*********\n")
    while f3.tell()!=len_f3.st_size:
        print(pickle.load(f3))
    f3.close()
    
if __name__=="__main__":
    
    main()
    print("\n----------------------------------")
    print("1. PRINT RECORDS OF FILE 2")
    print("2. PRINT RECORDS OF FILE 3")
    print("----------------------------------\n")
    ch=int(input("ENTER CHOICE : "))

    if ch==1:
        printRecordsFile2()
    if ch==2:
        printRecordsFile3()
    


