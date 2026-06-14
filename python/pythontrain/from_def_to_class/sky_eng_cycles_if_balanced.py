def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[': # Открывающая скобка
            stack.append(char)
        elif char in ')}]': # Закрывающая скобка
            if not stack or stack.pop() != brackets[char]:
                return False

# Если стек пуст, все скобки сбалансированы
    return len(stack) == 0

# Примеры тестирования
expressions = [
    "{[()]}",
    "{[(])}",
    "{{[[(())]]}}",
    "((()))",
    "((())"
]

for expr in expressions:
    result = "сбалансировано" if is_balanced(expr) else "несбалансировано"
    print(f"'{expr}' – {result}")