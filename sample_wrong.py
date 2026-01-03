# sample_wrong.py

def divide_numbers(a, b):
    return a / b

def main():
    # Intentional mistake: 'x' is not defined
    result = divide_numbers(x, 0)  # NameError first, then ZeroDivisionError if x existed
    print("Result:", result)

if __name__ == "__main__":
    main()
