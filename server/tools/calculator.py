def execute_basic_math(operation: str, a: float, b: float) -> float:

    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Math error: Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Syntax error: {operation} is not supported.")