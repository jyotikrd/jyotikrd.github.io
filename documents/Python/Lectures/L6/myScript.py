# A typical python script


def calculator(a, b, key):
    print("This is a calculator")

    if(key == '+'):   # perform addition
        print("Sum = ", a+b)
    elif(key == '-'):  # perform subtraction
        print("Difference = ", a-b)


def main():
    print('This is the main part of my script')
    calculator(20, 15, '+')


if __name__ == '__main__':
    main()

print('Value of built in variable:', __name__)
