def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1), len(num2)) + 2
        arranged_problems.append((num1, operator, num2, width))
    
    top_line = ""
    bottom_line = ""
    separator_line = ""
    answer_line = ""
    
    for num1, operator, num2, width in arranged_problems:
        top_line += num1.rjust(width) + "    "
        bottom_line += operator + num2.rjust(width - 1) + "    "
        separator_line += '-' * width + "    "
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line += answer.rjust(width) + "    "
    
    arranged_problems_output = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + separator_line.rstrip()
    if show_answers:
        arranged_problems_output += "\n" + answer_line.rstrip()
    
    return arranged_problems_output