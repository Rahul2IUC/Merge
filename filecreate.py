import pickle,random
no_of_Records=100
blocksize=4
other=100
class Record:
    '''
    Objective: To create a class of record type.
    '''
    def __init__ (self,key,other):
        
        '''
        Objective: To initialize the constructor.
        '''
        self.key=key
        self.other=other
    def get_key(self):
        '''
             Objective: to generate the key of record
        '''
    def __str__ (self):
        '''
        Objective: To return the value of  key and other in string.
        '''
        return "Key : "+str(self.key)+"\n"+" Other : "+str(self.other)
def write():
    list=[]
    f = open('f','wb')
    for i in range(0,no_of_Records):
        #This will generate 100 random records between the range.
        key = random.randint(100,200)
        if key not in list:list.append(key)
        #this will copy key 100 times to the respective record.
        other = str(key)*5
        ob = Record(key,other)
        pickle.dump(ob,f)
    f.close()
    f=open('f','rb')
    for i in range(0,no_of_Records):
        print(pickle.load(f))


def sortRecord():
    '''
    Objective: To sort and write the records according to block size of file f into record1 and record2.
    '''
   
    f = open("f",'rb')
    f1 = open("record1",'wb')
    f2 = open("record2",'wb')
    y=0
    c=0
    while y!=101:
        try:
            
            lst1=[]
            for i in range(0,blocksize):
                x=pickle.load(f)
                lst1.append(x)
            lst1=sorted(lst1,key=lambda Record:Record.get_key())
            for i in lst1:
                (pickle.dump(i,f1))
        except:
            break
        try:
            lst2=[]
            for i in range(0,blocksize):
                x=pickle.load(f)
                lst2.append(x)
            lst2=sorted(lst2,key=lambda Record:Record.get_key())
            for i in lst2:
                (pickle.dump(i,f2))
        except:
            break
    
    f.close()
    f1.close()
    f2.close()

    f1 = open("record1",'rb')
    try :
        print("RECORD1")
        for i in range(0,52):
            x=pickle.load(f1)
            
            print(i)
            print(x)
    except:
        pass
    f1.close()


    f2 = open("record2",'rb')
    try:
        print("RECORD2")
        for i in range(0,48):
            x=pickle.load(f2)
            
            print(i)
            print(x)
    except:
        pass
    f2.close()

    
    choose=int(input("Choose the file:"))

    if choose==1:
        f=open("record1",'rb')
    else:
        f=open("record2",'rb')

    print("Enter the range of record in file")
    start=input("Start of range: ")
    end=input("End ofrange: ")
    c=0
    
    pickle.load(f)
    size=f.tell()
    f.seek(0)
    f.seek((start-1)*size)
    for i in range(start,end+1):
        try:
            x=pickle.load(f)
            print(i)
            print(x)
            c+=1
        except:
            print("Limit Exceed: No more Records")
            break
    print(c)
    f.close()

        
