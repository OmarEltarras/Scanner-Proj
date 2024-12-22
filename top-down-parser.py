class TopDownParser:
    def __init__(self):
        self.grammar = {}

    def is_simple_grammar(self):
        """
        Checks if the grammar is a simple grammar.
        A simple grammar has non-terminals with rules in the form:
        - Non-Terminal -> Terminal Non-Terminal | Terminal
        """
        for non_terminal, rules in self.grammar.items():
            for rule in rules:
                if len(rule) > 2 or (len(rule) == 2 and not rule[1].isupper()):
                    return False
        return True

    def parse_sequence(self, sequence, start_symbol):
        """
        Parses the sequence using the grammar and checks if it is accepted or rejected.
        """
        def parse_recursive(current_sequence, current_symbol):
            if not current_symbol:
                return not current_sequence

            if current_symbol[0].islower():
                # Terminal
                return current_sequence.startswith(current_symbol[0]) and parse_recursive(current_sequence[1:], current_symbol[1:])
            elif current_symbol[0].isupper():
                # Non-Terminal
                for rule in self.grammar.get(current_symbol[0], []):
                    if parse_recursive(current_sequence, rule + current_symbol[1:]):
                        return True

            return False

        return parse_recursive(sequence, start_symbol)

    def run(self):
        while True:
            print("\n--- Top Down Parser ---")
            print("1. Enter Grammar")
            print("2. Check if Grammar is Simple")
            print("3. Test Sequence")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.grammar = {}
                print("Enter Grammar Rules (e.g., S -> aA | b)")
                print("Type 'done' when finished.")
                while True:
                    rule = input("Enter rule: ")
                    if rule.lower() == "done":
                        break
                    try:
                        left, right = rule.split("->")
                        left = left.strip()
                        right_rules = [r.strip() for r in right.split("|")]
                        self.grammar[left] = self.grammar.get(left, []) + right_rules
                    except ValueError:
                        print("Invalid rule format. Use the format: Non-Terminal -> Rule(s)")

            elif choice == "2":
                if self.is_simple_grammar():
                    print("The grammar is SIMPLE.")
                else:
                    print("The grammar is NOT SIMPLE.")

            elif choice == "3":
                if not self.grammar:
                    print("Please enter a grammar first.")
                    continue

                start_symbol = input("Enter the start symbol: ").strip()
                sequence = input("Enter the sequence to test: ").strip()
                if self.parse_sequence(sequence, start_symbol):
                    print(f"The sequence '{sequence}' is ACCEPTED.")
                else:
                    print(f"The sequence '{sequence}' is REJECTED.")

            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    parser = TopDownParser()
    parser.run()
