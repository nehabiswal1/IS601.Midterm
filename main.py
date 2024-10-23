from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

# Command mapping
calculator_commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

def menu():
    print("Available commands: add, subtract, multiply, divide")
    print("Type 'exit' to quit")

def repl():
    while True:
        user_input = input("Enter command (or 'menu' for options): ").strip()
        if user_input == "menu":
            menu()
            continue
        elif user_input == "exit":
            break
        else:
            try:
                command_name, *args = user_input.split()
                args = list(map(float, args))
                command = calculator_commands[command_name]
                result = command.execute(*args)
                print(f"Result: {result}")
            except KeyError:
                print(f"Unknown command: {command_name}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl()

