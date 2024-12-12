def leaky_bucket():
    size = int(input("Enter the bucket size: "))
    nop = int(input("Enter the number of packets: "))
    
    datarate = []
    print("Enter the data rate for each packet:")
    for i in range(nop):
        datarate.append(int(input()))
    
    opr = int(input("Enter the output rate: "))
    
    for rate in datarate:
        if rate > size:
            print("Bucket overflow")
        else:
            temp = rate
            while temp > opr:
                print("Packet transmission:", opr)
                temp -= opr
            print("Packet transmission:", temp)

# Call the function to execute the program
leaky_bucket()