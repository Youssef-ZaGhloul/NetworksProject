# define the function to split the file into smaller chunks
def splitFile(inputFile,chunkSize):
    # read the contents of the file
    f = open(inputFile, 'rb')
    data = f.read()  # read the entire content of the file
    f.close()
    # get the length of data, ie size of the input file in bytes
    bytes = len(data)

    # calculate the number of chunks to be created
    noOfChunks = bytes / chunkSize
    if (bytes % chunkSize):
        noOfChunks += 1
        # create a info.txt file for writing metadata
        f = open('info.txt', 'w')
        f.write(inputFile + ',' + 'chunk,' + str(noOfChunks) + ',' + str(chunkSize))
        f.close()
        chunkNames = []

        for i in range(0, bytes + 1, chunkSize):
            fn1 = "chunk%s" % i
            chunkNames.append(fn1)
            f = open(fn1, 'wb')
            f.write(data[i:i + chunkSize])
            f.close()

    return noOfChunks

# define the function to join the chunks of files into a single file
def joinFiles(fileName, noOfChunks, chunkSize):
    dataList = []
    for i in range(0, noOfChunks, 1):
        chunkNum = i * chunkSize
        chunkName = fileName + '%s' % chunkNum
        f = open(chunkName, 'rb')
        dataList.append(f.read())
        f.close()
        f = open(fileName +'.jpeg', 'wb')
    for data in dataList:
        f.write(data)
    f.close()

