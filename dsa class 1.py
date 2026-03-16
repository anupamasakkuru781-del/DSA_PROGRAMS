# Print Numbers from 1 to N

#def print_numbers(n):
    #for i in range(1, n+1):
        #print(i)

#def main():
    #n = int(input("enter Number:"))
    #print_numbers(n)

#if __name__ == "__main__":
    #main()

# sum of first N numbers

def calculate_sum(n):
    total = 0 # total is a.variable
    for i in range(1, n+1):
        total+=i
    return total
def main():
    n = int(input("Enter a Number:"))
    print("sum: ",calculate_sum(n)) 
if __name__ =="__main__":
    main()
