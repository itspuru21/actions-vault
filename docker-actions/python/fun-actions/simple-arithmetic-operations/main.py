import sys
import os

def main():
    # 1. Read the two inputs from sys.argv safely
    try:
        num1 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
        num2 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    except ValueError as e:
        print(f"❌ Error: Invalid number provided. Details: {e}")
        sys.exit(1)

    # 2. Perform all basic arithmetic operations
    total_sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    # Handle division by zero edge-case
    if num2 == 0:
        quotient = "Undefined (Division by zero)"
        print("⚠️ Warning: Division by zero attempted.")
    else:
        quotient = num1 / num2

    # 3. Print clean logs to the GitHub terminal
    print("🧮 --- Arithmetic Calculator Results ---")
    print(f"➕ Addition ({num1} + {num2}) = {total_sum}")
    print(f"➖ Subtraction ({num1} - {num2}) = {difference}")
    print(f"✖️ Multiplication ({num1} * {num2}) = {product}")
    print(f"➗ Division ({num1} / {num2}) = {quotient}")

    # 4. Write all outputs back to GitHub Actions via GITHUB_OUTPUT
    github_output_path = os.getenv('GITHUB_OUTPUT')
    if github_output_path:
        with open(github_output_path, 'a') as f:
            f.write(f"sum={total_sum}\n")
            f.write(f"difference={difference}\n")
            f.write(f"product={product}\n")
            f.write(f"quotient={quotient}\n")

if __name__ == "__main__":
    main()