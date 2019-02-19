import pickle, os
import random
blocksize=4
no_of_records=100
others = 100

class Record:
    '''
    Objective : To create an object of type 'Record'
    '''

    def __init__(self):
        '''
        Objective : To initialize an Record object
        Input     : self   : (Implicit) Record object
                    key    : key value of the object Record
                    others : value corresponding to that key
        Output    : None
        '''
        
        # This will generate keys between the value given in below line
        self.key= random.randint(1000000,2000000)
        #this will copy the key into the record(x othersSize)
        self.others= str(self.key)*others
    
    def get_key(self):
        '''Objective: to generate the key of record
        '''
        return self.key
    
    def __str__(self):
        '''
        Objective : To return a string of the values of the object Record
        Input     : self : (Implicit) Record object 
        OUTPUT    : a string representing the Record object
        '''

        return "Key: "+str(self.key) + "\nData: " +self.others


def writeToFile():

    '''
    Objective : To write records in file1
    Input     : Start= Starting range of record
                    End= Ending range of record
    Output    : None 
    '''
     
    f = open("f",'wb')
    for i in range(0,no_of_records):
        ob=Record()
        #This will write n numbers of record into the file f.
        pickle.dump(ob,f)
    f.close()

    f = open("f",'rb')
    Start=int(input("Starting range:="))
    End= int(input("Ending point:="))
    x=pickle.load(f)
    size=f.tell()
    f.seek(0)
    f.seek((Start-1)*size)
    
    for i in range(Start,End+1):
        try:
            x=pickle.load(f)
            print(i)
            print(x)
        except:
            break
    f.close()

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
        for i in range(0,52):
            x=pickle.load(f1)
            print("RECORD1")
            print(i)
            print(x)
    except:
        pass
    f1.close()


    f2 = open("record2",'rb')
    try:
        for i in range(0,48):
            x=pickle.load(f2)
            print("RECORD2")
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
    start=int(input("Start of range: "))
    end=int(input("End ofrange: "))
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


       
                    
                
            
                    
                    
                
    


        
    

    
        
    

 
                  
    

    

