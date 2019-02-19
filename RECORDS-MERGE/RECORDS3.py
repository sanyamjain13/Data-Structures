import pickle,os,sys
from RECORDS3 import *

def merge(blocksize):
    '''
    objective: It is to merge the elements according to the blocksize
               of elements in the files 2 and 3 and sort them and load
               them in file 4 and 5.
    input parameters:
                    blocksize: It tells how many elements can be inside a block
    '''
    file1='file2.txt'
    file2='file3.txt'
    file3='file4.txt'
    file4='file5.txt'

    f1=open(file1,'rb')
    f2=open(file2,'rb')
    f3=open(file3,'wb')
    f4=open(file4,'wb')
    
    
    x=True
    flag=True
    
    while x:
        '''
        this if is deciding whether to load the elements inide file 4 or file5
        '''
        if flag==True:
            fileS=f3
            flag=False

        else:
            fileS=f4
            flag=True

        i,j=0,0

        rec1=None
        rec2=None
        pointer1=f1.tell()
        pointer2=f2.tell()
        '''
        This is merging and sorting the elements in two list
        '''
        while i<blocksize and j<blocksize:

            pointer1=f1.tell()
            pointer2=f2.tell()

            try:
                rec1=pickle.load(f1)
            except EOFError:
                i=blocksize
                x=False
                break

            try:
                rec2=pickle.load(f2)
            except EOFError:
                f1.seek(pointer1)
                x=False
                j=blocksize
                break;

            if rec1.getkey()<rec2.getkey():
                pickle.dump(rec1,fileS)
                f2.seek(pointer2)
                i=i+1

            else:
                pickle.dump(rec2,fileS)
                f1.seek(pointer1)
                j=j+1

        while i<blocksize:
            try:
                rec1=pickle.load(f1)
            except EOFError:
                break
            pickle.dump(rec1,fileS)
            i=i+1

        while j<blocksize:
            try:
                rec2=pickle.load(f2)
            except EOFError:
                break
            pickle.dump(rec1,fileS)
            j=j+1
        

    f1.close()
    f2.close()
    f3.close()
    f4.close()

    os.remove('file2.txt')
    os.remove('file3.txt')
    os.rename('file4.txt','file2.txt')
    os.rename('file5.txt','file3.txt')

def records_Up_Low(lower,upper):
    '''
    objective: To give the records according to the user limit
    input parameters:
                    lower:Lower limit of the record
                    upper:upper limit of the record
    '''
    f2=open('file2.txt','rb')
    obj=pickle.load(f2)
    size=f2.tell()
    f2.seek(0)
    f2.seek(size*(lower-1))
    for i in range(lower,upper+1):
        print("RECORD NO- "+str(i),"->",pickle.load(f2),"\n")

def printRecordsFile():
    '''
    printing all the records in a file
    '''
    f2=open('file2.txt','rb')
    len_f2=os.stat("file2.txt")
    
    
    while f2.tell()!=len_f2.st_size:
        print(pickle.load(f2))
    f2.close()    

def main():
    f2=open('blocksize.txt','rb')
    blocksize=pickle.load(f2)
    f2.close()
    #os.remove("blocksize.txt")
    while True:

        merge(blocksize)
        #WHEN FILE-3 BECOMES EMPTY
        if os.path.getsize("file3.txt")==0:
            break
        blocksize=blocksize*2

if __name__=="__main__":

    main()
    print("\n----------------------------------")
    print("1. PRINT ALL RECORDS OF FILE ")
    print("2. PRINT RECORDS ACCORDING TO USER")
    print("----------------------------------\n")
    ch=int(input("ENTER CHOICE : "))
    print("\n---------------------------------------\n")
    if ch==1:
        printRecordsFile()
    
    if ch==2:
        print("TO FIND THE RECORD ACCORDING TO YOUR WISH :- ")
        print("-------------------------------------\n")
        lower=int(input("ENTER LOWER LIMIT : "))
        upper=int(input("ENTER UPPER LIMIT : "))
        if upper>lower:
            records_Up_Low(lower,upper)
        else:
            print("YOU ENTERED THE LIMITS WRONG :(")
