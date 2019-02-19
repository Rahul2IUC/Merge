from fileSort import *
import time

def mergeSort():
    '''
    Objective: To sort and merge records in files f1 and f2.
               Final sorted records are stored in file1.
               *** This function changes the contents of file1 and file2. ***
    '''
    fRecords = noOfRecords('f.txt')
    f = open('f.txt', 'rb')
    start = f.tell()
    pickle.load(f)
    end = f.tell()
    diff = end - start
    

    mergeSortHelper(blockSize = 4, recSize = diff, totalRecords = fRecords)

def mergeSortHelper(blockSize, recSize, totalRecords):

    if blockSize >= totalRecords:
        # printRecords('f1.txt',1,1000000)
        return


    f1 = open("f1.txt", 'rb')
    f2 = open("f2.txt", 'rb')
    f3 = open("f3.txt", 'wb')
    f4 = open("f4.txt", 'wb')
    
    f1Records =  noOfRecords('f1.txt')               # no. of records in f1
    f1Blocks = f1Records // blockSize                # no. of blocks in f1
    f2Records = noOfRecords('f2.txt')                # no. of records in f2
    f2Blocks = f2Records // blockSize                # no. of blocks in f2

    CompleteBlocks = min(f1Blocks, f2Blocks)
    i,j = 1,1
    dumpFile = f3
    
    for a in range(CompleteBlocks):
        mergeSortedBlocks(f1, i, f2, j, recSize, blockSize, dumpFile)
        i += blockSize
        j += blockSize
        if dumpFile == f3:
            dumpFile = f4
        else:
            dumpFile = f3

    # handle remaining records

    f1End = 0
    f2End = 0
    nextRecord = (blockSize * CompleteBlocks) + 1
    try:
        f1.seek(recSize * (nextRecord - 1))
        rec1 = pickle.load(f1)
    except EOFError:
        f1End = 1
        pass
    try:
        f2.seek(recSize * (nextRecord - 1))
        rec2 = pickle.load(f2)
    except EOFError:
        f2End = 1
        pass


    while f1End == 0 and f2End == 0:
        if rec1.getKey() < rec2.getKey():
            pickle.dump(rec1, dumpFile)
            try:
                rec1 = pickle.load(f1)
            except EOFError:
                f1End = 1
                break
        else:
            pickle.dump(rec2, dumpFile)
            try:
                rec2 = pickle.load(f2)
            except EOFError:
                f2End = 1
                break
            
    while f1End == 0:
        pickle.dump(rec1, dumpFile)
        try:
            rec1 = pickle.load(f1)
        except EOFError:
            f1End = 1
            break
            
    while f2End == 0:
         pickle.dump(rec2, dumpFile)
         try:
            rec2 = pickle.load(f2)
         except EOFError:
            f2End = 1
            break
        
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    
    os.remove('f1.txt')
    os.remove('f2.txt')
    os.rename('f3.txt', 'f1.txt')
    os.rename('f4.txt', 'f2.txt')

    mergeSortHelper(blockSize = blockSize * 2, recSize = recSize, totalRecords = totalRecords)
    
def mergeSortedBlocks(f1, i, f2, j, recSize, blockSize, dumpFile):
    '''
    Objective: This function merges two blocks of sorted records into a single
               block of twice the size and dumps it into the given file.
    Input parameter:
                 f1: file object to read records from file1
                  i: starting record no to be read from file1
                 f2: file object to read records from file1
                  j: starting record no to be read from file2
            recSize: size of each record in file1 and file2     
          blockSize: current block size in f1 and f2
           dumpFile: file object to dump merged sorted records in given dump file
    '''

    
    f1.seek(recSize * (i-1))
    f2.seek(recSize * (j-1))

    p = 1
    q = 1

    
    rec1 = pickle.load(f1)
    # print('inside mergeSortedBlocks, rec1 = ', rec1.getKey())
    rec2 = pickle.load(f2)
    # print('inside mergeSortedBlocks, rec2 = ', rec2.getKey())

    while p <= blockSize and q <= blockSize:
        
        if rec1.getKey() < rec2.getKey():
            pickle.dump(rec1, dumpFile)
            # print('record dumped = ', rec1.getKey())
            if p < blockSize:
                rec1 = pickle.load(f1)
            p += 1
        else:
            pickle.dump(rec2, dumpFile)
            # print('record dumped = ', rec2.getKey())
            if q < blockSize:
                rec2 = pickle.load(f2)
            q += 1

    while p <= blockSize:
        pickle.dump(rec1, dumpFile)
        # print('record dumped = ', rec1.getKey())
        if p < blockSize:
                rec1 = pickle.load(f1)
        p += 1

    while q <= blockSize:
        pickle.dump(rec2, dumpFile)
        # print('record dumped = ', rec2.getKey())
        if q < blockSize:
                rec2 = pickle.load(f2)
        q += 1
    

def noOfRecords(filename):
    '''
    Objective: To count and return the number of records in a given file
    Input Parameter:
           filename: Name of the file in which records are to be counted
    Output: Number of records in given file
    '''

    f = open(filename, 'rb')
    start = f.tell()
    pickle.load(f)
    end = f.tell()
    recordSize = end - start
    fileSize = os.stat(filename).st_size
    
    return fileSize // recordSize

res = open('results.txt', 'w')

i = 100
dic = {}
while i <= 1000000:
    saveRecords("f.txt", i)
    # print("---------Records in f---------")
    # printRecords("f.txt", 1, i)

    makeFilesF1F2("f.txt")
    # print("---------Records in f1---------")
    # printRecords("f1.txt",1, i)

    # print("---------Records in f2---------")
    # printRecords("f2.txt",1, i)

    startTime = time.time()
    mergeSort()
    endTime = time.time()
    dic[str(i)] = endTime - startTime
    print('time taken = ', endTime - startTime, 'for ', i, 'records')
    i = i * 10

res.write(str(dic))
res.close()
