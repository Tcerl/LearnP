def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        first_line += operand1.rjust(width) + "    "
        second_line += operator + operand2.rjust(width - 1) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if operator == "+":
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            answer_line += result.rjust(width) + "    "

    arranged_problems += first_line.rstrip() + "\n"
    arranged_problems += second_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip() + "\n"
    if show_answers:
        arranged_problems += answer_line.rstrip() + "\n"

    return arranged_problems.rstrip()
