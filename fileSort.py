import os, random, pickle

class Node:
    '''
    Objective: To represent a node/record entity
    '''
    def __init__(self, key):
        
        '''
        Objective: To initialise a Node object
        Input Parameters:
                    self: (implicit) node object
                     key: key value of node/record
        '''
        self.key = key
        self.others = str(self.key)*100  # constant size records
        #self.others = str(self.key)*random.randint(50, 250)    

    def getKey(self):
        '''
        Objective: To return the key value of the object.
        Input Parameters:
                    self: (implicit) node object
        Output: Key of the object
        '''
        return self.key

    def getOthers(self):
        '''
        Objective: To return the othets value of the object.
        Input Parameters:
                    self: (implicit) node object
        Output: others of the object
        '''
        return self.others

    def __str__(self):
        return ("Key: " + str(self.getKey()) + "\nOthers: " + str(self.getOthers()))




def generateKey(keys, startRange, endRange):
        '''
        Objective: To generate a unused key in the list in the given range.
        '''
        if len(keys) >= endRange - startRange:
            print("Maximum keys generated already.")
            return

        while True:
            key = random.randint(startRange, endRange)
            if key not in keys:
                keys.append(key)
                return key



def saveRecords(filename, noOfNodes):
    '''
    Objective: To create a file and create and save noOfNodes records in given file . If
                file exists already, delete the file and create new again.
    Input Parameter:
           filename: Name of file in which records to be saved.
          noOfNodes: Number of records to be saved in the file.
    '''
    if os.path.isfile(filename):
        os.remove(filename)

    f = open(filename, 'wb')

    keys = []
    startRange = 100000000
    endRange = 200000000
    
    for i in range(noOfNodes):
        key = generateKey(keys, startRange, endRange)
        n = Node(key)
        pickle.dump(n, f)

    print(str(noOfNodes) + " records saved in " + filename)


def printRecords(filename, startRange, endRange):
    '''
    Objective: To retrieve and print records of the given file in given range.
               (including startRange and endRange)
    Input Parameter:
           filename: Name of file in which records to be saved.
           noOfRecords: Number of records to be retrieved from the file.
    '''
    try:    
        f = open(filename, 'rb')

        start = f.tell()       
        pickle.load(f)
        end = f.tell()
        diff = end - start
        
        f.seek(diff * (startRange - 1))
        
        for i in range(startRange, endRange + 1):
            n = pickle.load(f)
            print(str(i) + " key : " + str(n.getKey()))
            
    except EOFError:
        pass

def makeFilesF1F2(filename, blockSize = 4):
    '''
    Objective: To make files f1 and f2 which contain records sorted in blocks of blocksize.
    Input Parameter:
           filename: The name of the file which contains records initially.
          blocksize(default = 4): The size of block which contains records in sorted order.
    '''
    '''
    Approach: We read records one by one from given file and append them in a list till blocksize.
              Then we sort the list based on keys of records and add block of sorted records  one by one in f1.
              Then next sorted block of records in f2, then in f1 and so on till all the records of given file are handled.
    '''
    
    f = open(filename, "rb")
    f1 = open("f1.txt", "wb")
    f2 = open("f2.txt", "wb")

    
    endWhile = 0  #to control execution of while loop
    flag = 1  # to control in which file the records are written
    
    while endWhile == 0:
        lst = []

        # Add blockSize no. of records in a list one by one
        for i in range(blockSize):
            try:
                rec = pickle.load(f)
                lst.append(rec)
            except EOFError:
                endWhile = 1
                pass

        # Sort records in list
        lst.sort(key = lambda Node: Node.getKey())

        # Add sorted blockSize no. of records one by one, either in f1 or in f2 
        for i in range(len(lst)):
            if flag == 1:
                pickle.dump(lst[i], f1)
            else: 
                pickle.dump(lst[i], f2)
    
        if flag == 1:
            flag = 2
        else:
            flag = 1



'''
f = open('f.txt', 'rb')
f.seek(0)
start = f.tell()       
pickle.load(f)
end = f.tell()
diff = end - start
print('file 1 size = ' + str(os.stat('f1.txt').st_size))
print('no of objects in file 1 = ' + str((os.stat('f1.txt').st_size)//diff))
print('file 2 size = ' + str(os.stat('f2.txt').st_size))
print('no of objects in file 2 = ' + str((os.stat('f2.txt').st_size)//diff))
'''
