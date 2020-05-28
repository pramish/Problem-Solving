def main():
    take_input()

"""
Problem URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2057
Problem Number: 2057
"""
def take_input():
    sum = 0
    print("Please Enter your input followed by the space:")
    number1 = raw_input(
        "Enter the time you left, Enter the time required for the journey and Enter the time zone in whole number: ")
    input_number = number1.split()
    # print(input_number)
    for i in range(len(input_number)):
        sum = sum + int(input_number[i])
        # print(input_number[i])

    if (sum < 24):
        print(sum)
    if (sum == 24):
        sum = 0
        print(sum)
    if (sum > 24):
        sum = sum - 24
        print(sum)




if __name__ == "__main__":
    main()