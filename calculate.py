def calculate(operation, numbers):
    if not numbers:
        return {"result": None, "error": "No numbers provided"}
    
    if operation == 'sum':
        return {"result": sum(numbers), "error": None}
    elif operation == 'multiply':
        res = 1
        for n in numbers:
            res *= n
        return {"result": res, "error": None}
    return {"result": None, "error": "Unsupported operation"}

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))        # Output: 8
    print(calculate('subtract', 5, 3))   # Output: 2
    print(calculate('multiply', 5, 3))   # Output: 15
    print(calculate('divide', 5, 3))     # Output: 1.666...
    print(calculate('divide', 5, 0))     # Error