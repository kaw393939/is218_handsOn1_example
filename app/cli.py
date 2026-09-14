"""
Command-line interface for the calculator REPL (Read-Eval-Print-Loop).

Provides an interactive calculator where users can perform arithmetic operations.

This is the presentation/orchestration layer: read text, select an operation,
convert operands, display a result, and manage session history. Arithmetic lives
in app.operations so it can be reused without a terminal. See tests/test_cli.py
for examples of testing this layer without a human typing at the keyboard.
"""

# Explicit imports make the available arithmetic dependencies easy to find.
from app.operations import (
    add, subtract, multiply, divide, modulo, power, square_root
)


class Calculator:
    """Interactive calculator REPL with state owned by one session.

    A class groups behavior (methods) with related state (operations/history).
    ``self`` refers to the particular Calculator instance receiving the call.
    Creating a Calculator does not start input; call run() explicitly to do so.
    """

    def __init__(self):
        """Initialize calculator with available operations."""
        # A dispatch table maps text to (callable, operand count, help text).
        # Store add rather than add(): the function is selected now, called later.
        # Unary means one operand; binary means two. This table is reused for
        # parsing and help, reducing repeated lists of supported operations.
        self.operations = {
            '+': (add, 2, 'Add two numbers'),
            '-': (subtract, 2, 'Subtract two numbers'),
            '*': (multiply, 2, 'Multiply two numbers'),
            '/': (divide, 2, 'Divide two numbers'),
            '%': (modulo, 2, 'Modulo (remainder)'),
            '**': (power, 2, 'Power (exponentiation)'),
            'sqrt': (square_root, 1, 'Square root'),
        }
        # An instance attribute gives each session its own mutable list. A list
        # defined at class level would be shared by instances unless overridden.
        # History is in memory only; it is not saved when the process exits.
        self.history = []

    def display_welcome(self):
        """Display welcome message and help."""
        print("\n" + "="*50)
        print("Welcome to the Python Calculator!")
        print("="*50)
        print("\nAvailable operations:")
        print("-" * 50)
        # items() yields key/value pairs; tuple unpacking names the metadata.
        # func and args are unpacked here for readability but are not used by help.
        for op, (func, args, description) in self.operations.items():
            # In this f-string, :<6 left-aligns the symbol in a six-character field.
            print(f"  {op:<6} : {description}")
        print("\nSpecial commands:")
        print("  'history' : Show calculation history")
        print("  'clear'   : Clear history")
        print("  'help'    : Show this message")
        print("  'exit'    : Exit calculator")
        print("-" * 50 + "\n")

    def show_history(self):
        """Display calculation history."""
        # Empty containers are false in a condition. Return early for this case
        # so the normal path below needs no extra indentation.
        if not self.history:
            print("\nNo calculations yet.\n")
            return
        print("\nCalculation History:")
        print("-" * 50)
        # enumerate(..., 1) supplies student-friendly numbering starting at 1.
        for i, entry in enumerate(self.history, 1):
            print(f"  {i}. {entry}")
        print("-" * 50 + "\n")

    def parse_input(self, user_input: str):
        """Parse and execute user input.

        Args:
            user_input: Raw user input string

        Returns:
            True to continue, False to exit. This is a loop-control signal,
            not a calculation result or a flag indicating arithmetic success.
        """
        # Normalize outer whitespace once; blank input simply prompts again.
        user_input = user_input.strip()

        if not user_input:
            return True

        # Handle commands before arithmetic. lower() makes commands insensitive
        # to case without altering the original expression used by the parser.
        if user_input.lower() == 'exit':
            print("\nGoodbye!\n")
            return False
        elif user_input.lower() == 'history':
            self.show_history()
            return True
        elif user_input.lower() == 'clear':
            # Replace this session's history with a new empty list.
            self.history = []
            print("\nHistory cleared.\n")
            return True
        elif user_input.lower() == 'help':
            self.display_welcome()
            return True

        # At the UI boundary, turn calculation exceptions into readable output.
        # execute_calculation itself raises, so direct callers/tests can inspect
        # errors. Catching Exception keeps this teaching REPL alive, but can also
        # hide programming bugs. A production refinement is to catch expected
        # user-input errors specifically and log unexpected failures.
        try:
            self.execute_calculation(user_input)
        except Exception as e:
            print(f"\nError: {e}\n")

        return True

    def execute_calculation(self, expression: str):
        """Execute a calculation expression.

        Args:
            expression: Calculation expression (e.g., "5 + 3")

        Raises:
            ValueError: If no operation is found, splitting/conversion fails,
                or an arithmetic function rejects the input.
            ArithmeticError: For arithmetic failures not explicitly converted
                by an operation, such as zero raised to a negative power.

        Prints and records a successful result; returns None. This is a small
        single-operation parser, not a Python expression evaluator. It does not
        implement precedence, parentheses, or reliable signed/scientific input.
        Some malformed input can be misinterpreted; see the guide's limitations.
        """
        # Try to find operation in expression
        # Check multi-char operators first (e.g., ** before *)
        # key=len sorts by symbol length; reverse=True puts longer symbols first.
        # Substring matching is deliberately simple and has limits: a minus sign
        # in an operand can be mistaken for subtraction. Do not replace this
        # with eval(user_input), which would allow arbitrary Python execution.
        found_op = None
        sorted_ops = sorted(self.operations.keys(), key=len, reverse=True)
        for op in sorted_ops:
            if op in expression:
                found_op = op
                break

        # A missing operator is a domain-specific input error, not a KeyError.
        if not found_op:
            raise ValueError(
                f"No valid operation found. Use: {', '.join(self.operations.keys())}"
            )

        # _ conventionally names a value we intentionally do not use (help text).
        func, args_needed, _ = self.operations[found_op]

        # Parse operands
        if args_needed == 1:
            # Unary operation (sqrt)
            parts = expression.split(found_op)
            if len(parts) != 2:
                raise ValueError(f"Invalid format for {found_op}")
            # input arrives as text. float() handles decimals and raises
            # ValueError for nonnumeric text. This parser currently ignores
            # parts[0] for sqrt, so it does not validate the entire expression.
            operand = float(parts[1].strip())
            result = func(operand)
            calculation = f"{found_op}({operand}) = {result}"
        else:
            # Binary operation
            parts = expression.split(found_op)
            if len(parts) != 2:
                raise ValueError(f"Invalid format: {expression}")

            # split must yield exactly two pieces for one binary operation.
            # Neither full arithmetic expressions nor repeated operators work.
            operand1 = float(parts[0].strip())
            operand2 = float(parts[1].strip())
            result = func(operand1, operand2)
            calculation = f"{operand1} {found_op} {operand2} = {result}"

        # Build the history entry only after parsing and calculation succeed.
        # Consequently, rejected calculations do not leave partial history.
        print(f"\n{calculation}\n")
        self.history.append(calculation)

    def run(self):
        """Read–Evaluate–Print–Loop until exit, an interrupt, or end of input.

        Evaluation here means calling our selected arithmetic function; it does
        not mean Python's eval(). A user error is reported by parse_input and
        returns control to the next prompt instead of terminating the session.
        """
        self.display_welcome()

        try:
            while True:
                try:
                    # READ: input() waits for a line and returns it as a string.
                    user_input = input("calc> ")
                    # EVALUATE and PRINT happen in parse_input and its helpers.
                    # LOOP repeats unless parse_input explicitly returns False.
                    if not self.parse_input(user_input):
                        break
                except KeyboardInterrupt:
                    # Ctrl+C signals KeyboardInterrupt, not an ordinary Exception.
                    print("\n\nCalculator interrupted. Goodbye!\n")
                    break
        except EOFError:
            # input() raises EOFError when a pipe ends or the terminal sends EOF
            # (usually Ctrl+D on Unix or Ctrl+Z then Enter on Windows).
            print("\n\nEnd of input. Goodbye!\n")


def main():
    """Construct one fresh session, then start its input loop.

    A small entry-point function can be called by calculator.py or by running
    this module with ``python -m app.cli`` from the project root.
    """
    calc = Calculator()
    calc.run()


# Keep importing this module safe for tests: start only on direct execution.
if __name__ == '__main__':
    main()
