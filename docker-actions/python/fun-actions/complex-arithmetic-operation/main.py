import sys
import os
import math

def main():
    # 1. Read inputs from action.yml args
    operation = sys.argv[1].lower().strip() if len(sys.argv) > 1 else "sqrt"
    
    try:
        val = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
        extra_val = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    except ValueError as e:
        print(f"❌ Error: Invalid number format provided. Details: {e}")
        sys.exit(1)

    result = None
    print(f"🔬 Running Scientific Operation: '{operation}' on value {val} (extra: {extra_val})")

    # 2. Perform math operations safely
    try:
        if operation == "sqrt":
            if val < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            result = math.sqrt(val)

        elif operation == "power":
            result = math.pow(val, extra_val)

        elif operation == "factorial":
            if not val.is_integer() or val < 0:
                raise ValueError("Factorial requires a non-negative integer.")
            result = math.factorial(int(val))

        elif operation == "log":
            if val <= 0:
                raise ValueError("Logarithm argument must be greater than zero.")
            result = math.log(val) # Natural log (ln)
        
        else:
            print(f"❌ Error: Unknown operation '{operation}'")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Mathematical Error: {e}")
        sys.exit(1)

    print(f"✨ Calculation Result: {result}")

    # 3. Pass output back to GitHub Actions via GITHUB_OUTPUT
    github_output_path = os.getenv('GITHUB_OUTPUT')
    if github_output_path:
        with open(github_output_path, 'a') as f:
            f.write(f"result={result}\n")

if __name__ == "__main__":
    main()