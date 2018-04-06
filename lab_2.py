
def gcd(a,b):
    if a == 0 and b == 0:
        raise ValueError()
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def acctBalance(deposit, interestRate, years):
    if years == 0:
        return deposit
    else:
        return acctBalance(deposit * interestRate, interestRate, years - 1)



def main():
    print("To exit program run command 'exit' when prompted for two values")
    while True:
        twovals = input("Enter two values to calculate GCD: ")
        if twovals == 'exit':
            break
        vals = twovals.split(",")
        val1 = int(vals[0])
        val2 = int(vals[1])

        try:
            print(gcd(val1,val2))
        except ValueError:
            print("enter two integers that are not 0s")


        deposit = int(input("Pleae enter a deposit $"))
        rate = int(input("Plese enter a rate %"))
        years = int(input("Enter number of years deposit will collect interest "))
        rate = (rate / 100) + 1
        result = acctBalance(deposit,rate,years)
        result = round(result, 2)
        print("After " + str(years) + " years the principal grows to $" + str(result))

if __name__ == '__main__':
    main()
