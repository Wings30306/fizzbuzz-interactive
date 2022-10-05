"""Interactive FizzBuzz game"""


def fizzbuzz(num):
    """
    FIZZBUZZ functionality:
    - if a number is divisible by 3 but not 5, return Fizz
    - if a number is divisible by 5 but not 3, return Buzz
    - if a number is divisible by both, return FizzBuzz
    - if a number is not divisible by either, return the number
    """
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = num
    return result


def play():
    """Main function to play the game"""
    print("Hello, welcome to FizzBuzz, "
          "the division game that tells you whether a number is divisible by 3"
          " (Fizz), 5 (Buzz) or both (FizzBuzz).")
    play_status = True
    while play_status:
        try:
            user_num = int(input("Enter a number: "))
            print(f"FizzBuzz result for {user_num} is {fizzbuzz(user_num)}")
            print()
            play_again = input("Choose another number? y/n ")
            if play_again.lower() == "y":
                play_status = True
            elif play_again.lower() == "n":
                play_status = False
            else:
                print("Not a recognised answer.")
                print("Ending game")
                play_status = False

        except BaseException:
            print("Not a number, try again!")


play()
