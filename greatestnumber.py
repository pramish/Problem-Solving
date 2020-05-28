# Main function
def main():
    take_input()
"""
Problem Name: The Greatest
Problem Number: 1013
Problem URI: https://www.urionlinejudge.com.br/judge/en/problems/view/1013
Question: Make a program that reads 3 integer values and present the greatest one
followed by the message "eh o maior". 
"""
def take_input():
    number1 = input("Please enter first number: ")
    number2 = input("Please enter second number: ")
    number3 = input("Please enter third number: ")

    if ((number1 > number2) and (number1 > number3)):
        print(number1, "eh o major")
    if ((number2 > number1) and (number2 > number3)):
        print(number2, "eh o major")
    else:
        print(number3, "eh o major")
take_input()

if __name__ == "__main__":
    main()
