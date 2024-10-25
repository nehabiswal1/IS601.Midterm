import logging
import  os
from dotenv import load_dotenv
import pandas as pd
from Midterm.commands.add_command import AddCommand
from Midterm.commands.subtract_command import SubtractCommand
from Midterm.commands.multiply_command import MultiplyCommand
from Midterm.commands.divide_command import DivideCommand
load_dotenv()

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Calculator Started")
logging.error("An Error Occurred")


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

# Function to save history to CSV
def save_history():
    try:
        history.to_csv('history.csv', index=False)
        logging.info("History saved to history.csv")
        print("History saved to history.csv")
    except Exception as e:
        logging.error(f"Failed to save history: {str(e)}")
        print(f"Error saving history: {e}")

# Function to load history from CSV
def load_history():
    global history
    try:
        history = pd.read_csv('history.csv')
        logging.info("History loaded from history.csv")
        print("History loaded from history.csv")
    except FileNotFoundError:
        logging.warning("No previous history found. Starting with an empty history.")
        print("No previous history found. Starting with an empty history.")
    except Exception as e:
        logging.error(f"Failed to load history: {str(e)}")
        print(f"Error loading history: {e}")

# Function to clear history
def clear_history():
    global history
    history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
    logging.info("History cleared")
    print("History cleared")

# Main REPL function
def repl():
    global history
    while True:
        user_input = input("Enter command (or 'menu' for options): ").strip()
        
        if user_input == "menu":
            menu()
            continue
        elif user_input == "exit":
            logging.info("Exiting calculator")
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
                # Split user input into command and arguments
                command_name, *args = user_input.split()
                args = list(map(float, args))  # Convert arguments to float
                command = calculator_commands[command_name]
                
                # Execute the command
                result = command.execute(*args)
                print(f"Result: {result}")
                
                # Append the result to history
                history = history.append(
                    {"Operation": command_name, "Operands": args, "Result": result}, 
                    ignore_index=True
                )
                
                # Automatically save history after each operation
                save_history()

                # Log the successful execution
                logging.info(f"Executed {command_name} with args {args}: {result}")
                
            except KeyError:
                print(f"Unknown command: {command_name}")
                logging.warning(f"Unknown command: {command_name}")
            except Exception as e:
                print(f"Error: {e}")
                logging.error(f"Error during {command_name}: {str(e)}")

if __name__ == "__main__":
    repl()
