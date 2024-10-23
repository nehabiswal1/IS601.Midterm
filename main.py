import pandas as pd
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

history = pd.DataFrame(columns=["Operation", "Operands", "Result"])

calculator_commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

def menu():
    print("Available commands: add, subtract, multiply, divide")
    print("Type 'history' to view history")
    print("Type 'save_history' to save history to CSV")
    print("Type 'load_history' to load history from CSV")
    print("Type 'clear_history' to clear history")
    print("Type 'exit' to quit")

def save_history():
    history.to_csv('history.csv', index=False)
    print("History saved to history.csv")

def load_history():
    global history
    history = pd.read_csv('history.csv')
    print("History loaded from history.csv")

def clear_history():
    global history
    history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
    print("History cleared")

def repl():
    global history
    while True:
        user_input = input("Enter command (or 'menu' for options): ").strip()
        if user_input == "menu":
            menu()
            continue
        elif user_input == "exit":
            break
        elif user_input == "history":
            print(history)
        elif user_input == "save_history":
            save_history()
        elif user_input == "load_history":
            load_history()
        elif user_input == "clear_history":
            clear_history()
        else:
            try:
                command_name, *args = user_input.split()
                args = list(map(float, args))
                command = calculator_commands[command_name]
                result = command.execute(*args)
                print(f"Result: {result}")
                history = history.append(
                    {"Operation": command_name, "Operands": args, "Result": result}, 
                    ignore_index=True
                )
            except KeyError:
                print(f"Unknown command: {command_name}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl()
