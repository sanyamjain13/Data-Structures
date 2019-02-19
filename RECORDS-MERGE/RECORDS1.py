import pickle,random,os,sys
class record:
    '''
    Objective: To represent a record entity
    '''
    def __init__(self,key):
        '''
        objective: To initialse object of record class
        input parameters:
                        self:Implicit parameter
                        key: The key of the value
        '''
        self.key=key+100000000
        self.nonkey=str(self.key)*10
        
    def getkey(self):
        '''
        objective: To get the key of a record
        input parameters:
                        self:Implicit parameter
        returns the key of the record
        '''
        return self.key

    def __str__(self):
        '''
        objective: To print the object of record class
        input parameters:
                        self:Implicit parameter
        '''

        return str(self.key)+" :"+str(self.nonkey)+"\n"

def printRecords(lower,upper):

    f=open('file1.txt','rb')
    obj=pickle.load(f)
    size=f.tell()
    f.seek(0)
    f.seek(size*(lower-1))
    for i in range(lower,upper+1):
        print("RECORD NO "+str(i),pickle.load(f),"\n")
        
    f.close()
    
def main():
    global n
    n=int(input('ENTER NUMBER OF RECORDS TO BE STORED IN FILE : '))
    keysList=[]
    f=open('file1.txt','wb')
    No_rec=open('record.txt','wb')
    pickle.dump(n,No_rec)
    No_rec.close()

    #HERE ENTERING THE RECORDS INTO FILE-1 AND ALSO THE RECORDS ARE NOT DUPLICATE, ONLY UNIQUE
    for i in range(1,n+1):
        key=random.randint(10,10000000)
        while key in keysList:
            key=random.randint(10,10000000)
        keysList.append(key)
        pickle.dump(record(key),f)
    f.close()
    print("----------------------------------")
    print("\n1. PRINT ALL THE RECORDS IN A FILE")
    print("2. PRINT ACCORDING TO USER \n")
    print("----------------------------------")
    ch=int(input("   ENTER CHOICE : "))

    f=open('file1.txt','rb')
    if ch==1:
        pickle.load(f)
        len_f=os.stat('file1.txt')
        while f.tell()!=len_f.st_size:
            print(pickle.load(f))
    f.close()

    if ch==2:
        lower=int(input("ENTER THE LOWER LIMIT : "))
        upper=int(input("ENTER THE UPPER LIMIT : "))
        printRecords(lower,upper)

    if ch<=0 or ch>2:
        print("***WRONG CHOICE***")
        
if __name__=="__main__":
    
    main()
