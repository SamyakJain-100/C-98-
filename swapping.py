
#CREATE A FUNCTION FOR EXCHANGING FILE DATA
def swapFileData():
    #CREATE THE INPUT BOX FOR FILE PATH
    inp1 = input("ENTER THE NAME OF FILE 1.")
    inp2 = input("ENTER THE NAME OF FILE 2.")

    #OPEN FILE 1 READ ITS DATA AND SAVE IT IN VARIABLE
    data_a = open(inp1,'r')
    data_a.readline()

    #OPEN FILE 2 READ ITS DATA AND SAVE IT IN VARIABLE
    data_b = open(inp2,'r')
    data_b.readline()

    #PRINT TEXT
    print("WORK IN PROGRESS...")
    print("FILE SWAPPING COMPLETED")

    #PRINT THE VARIABLES
    print(data_a)
    print(data_b)

    #DO SWAPPING OF FILE DATA
    file1 = open(inp2,'w')
    file1.writelines(data_a)
    file2 = open(inp1,'w')
    file2.writelines(data_b)


    print(file2)

    print(file1)

    
    
    

    


swapFileData()