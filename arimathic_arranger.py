def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for each line of the output
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    # Process each problem
    for problem in problems:
        # Split the problem into components
        parts = problem.split()

        # Check if operator is valid
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width of the problem
        width = max(len(parts[0]), len(parts[2])) + 2

        # Format each line
        first_line.append(parts[0].rjust(width))
        second_line.append(parts[1] + parts[2].rjust(width - 1))
        dash_line.append('-' * width)

        # Calculate answer if required
        if show_answers:
            if parts[1] == '+':
                answer = str(int(parts[0]) + int(parts[2]))
            else:
                answer = str(int(parts[0]) - int(parts[2]))
            answer_line.append(answer.rjust(width))

    # Combine all lines with four spaces between problems
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dash_line)

    # Add answers if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
