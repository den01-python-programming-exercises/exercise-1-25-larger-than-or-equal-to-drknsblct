def main():
    #write your code below this line
    num1 = int(input('Give the first number:'))
    num2 = int(input('Give the second number:'))
    
    if num1 > num2:
        print('Greater number is: ' + str(num1))
    elif num1 < num2:
        print('Greater number is: ' + str(num2))
    else:
        print('The numbers are equal!')

if __name__ == '__main__':
    main()
