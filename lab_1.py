
def toBinary(n):
    binaryList = [0,0,0,0,0,0,0,0]
    valuseList = [128,64,32,16,8,4,2,1]
    if n > 255:
        print("Please enter a valid integer beetween 0 and 255.")
    else:
        for i in range(8):
            if n != 0 and n >= valuseList[i]:
                binaryList[i] = 1
                n = n - valuseList[i]
        return binaryList



def toDecimal(binaryList):

    final_val = int()
    valuseList = [128,64,32,16,8,4,2,1]
    if  8 < len(binaryList):
        print("enter a valid bit string")
    else:
        for i in range(8):
            if int(binaryList[i]) == 1:
                final_val += valuseList[i]
    return(final_val)

def sumit(n,m):

    if n > 127 or m > 127:
        print("Please enter two valid numbers under 127")
    else:
        carry_byte = [0,0,0,0,0,0,0,0]
        byte_1 = toBinary(n)
        byte_2 = toBinary(m)
        byte_3 = [0,0,0,0,0,0,0,0]
        for i in range(7,-1,-1):
            if byte_1[i] == 1 and byte_2[i] == 0 and carry_byte[i] == 0:
                byte_3[i] = 1
            if byte_1[i] == 0 and byte_2[i] == 1 and carry_byte[i] == 0:
                byte_3[i] = 1
            if byte_1[i] == 0 and byte_2[i] == 0 and carry_byte[i] == 1:
                byte_3[i] = 1
            if byte_1[i] == 1 and byte_2[i] == 1:
                carry_byte[i - 1] = 1
            if byte_1[i] == 1 and carry_byte[i] == 1:
                carry_byte[i - 1] = 1

            if byte_2[i] == 1 and carry_byte[i] == 1:
                carry_byte[i - 1] = 1

            if byte_1[i] == 1 and byte_2[i] == 1 and carry_byte[i] == 1:
                byte_3[i] = 1
                carry_byte[i - 1] = 1
        printsum(byte_1,byte_2,byte_3,carry_byte)
def doubleIt(n):
    n = toBinary(n)
    n.append(0)
    n.pop(0)
    deci = toDecimal(n)
    print(deci)
def printsum(byte_1,byte_2,byte_3,carry_byte):
    print("     Carry over byte")
    print("     ---------------")
    print(carry_byte)
    print("         Byte 1")
    print("         ------")
    print(byte_1)
    print("         Byte 2")
    print("         ------")
    print(byte_2)
    print("     Sum of the bytes")
    print("     ----------------")
    print(byte_3)
    decimal_hold = toDecimal(byte_3)
    print("Sum converted to a decimal")
    print("--------------------------")
    print("           " + str(decimal_hold))


def main():
    myint = int(input("enter an int: "))
    binaryList = toBinary(myint)
    print("       Bit String")
    print("========================")
    print(binaryList)

    mybitstring = list(input("enter an byte: "))
    decimal_hold = toDecimal(mybitstring)
    print("         " + str(decimal_hold))

    ints_to_be_summed = input("enter two integers to be summed seperated by a + : ")
    ints_to_be_summed = ints_to_be_summed.split('+')
    one = int(ints_to_be_summed[0])
    two = int(ints_to_be_summed[1])
    sumit(one,two)

    dub = int(input("Enter a number to be doubled: "))
    doubleIt(dub)

if __name__ == '__main__':
    main()
