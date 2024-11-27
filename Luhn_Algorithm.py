def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]

    # Extract odd digits (every second digit starting from the start)
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Extract even digits (every second digit starting from index 1)
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    # Return True if total % 10 == 0, indicating a valid card number
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Check the result of verify_card_number and print the appropriate message
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
