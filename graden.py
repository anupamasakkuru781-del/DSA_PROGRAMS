# if/elif/else
def check_graden(n):
    if n>90:
        print("O")
    elif n>80:
        print("A+")
    elif n>70:
        print("A")
    elif n>60:
        print("B+")
    elif n>50:
        print("B")
    elif n>40:
        print("C")
    else:
        print("Fail")
def main():
    n = int(input("Enter marks:"))
    check_grade(n)

    
