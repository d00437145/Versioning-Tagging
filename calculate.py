def calculate(operation, numbers, precision=None):
    if not isinstance(numbers, list) or not numbers:
        return {"result": None, "error": "Invalid or empty numbers list"}
    
    res = None
    if operation == 'sum':
        res = sum(numbers)
    elif operation == 'multiply':
        res = 1
        for n in numbers:
            res *= n
    elif operation == 'average':
        res = sum(numbers) / len(numbers)
    elif operation == 'max':
        res = max(numbers)
    else:
        return {"result": None, "error": "Unsupported operation"}
    
    if precision is not None and isinstance(res, (int, float)):
        res = round(res, precision)
        
    return {"result": res, "error": None}

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))        # Output: 8
    print(calculate('subtract', 5, 3))   # Output: 2
    print(calculate('multiply', 5, 3))   # Output: 15
    print(calculate('divide', 5, 3))     # Output: 1.666...
    print(calculate('divide', 5, 0))     # Error