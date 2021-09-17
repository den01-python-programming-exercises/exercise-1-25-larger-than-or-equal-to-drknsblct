def main():
    #write your code below this line
    num1 = int(input('Give the first number:'))
    num2 = int(input('Give the second number:'))
    
    if num1 > num2:
        print(str(num1) + ' is bigger than ' + str(num2))
    elif num1 < num2:
        print(str(num2) + ' is bigger than ' + str(num1))
    else:
        print('The numbers are equal!')

if __name__ == '__main__':
    main()
