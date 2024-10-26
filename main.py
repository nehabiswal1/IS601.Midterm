import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import logging
import pandas as pd
from dotenv import load_dotenv

from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand



# Load environment variables
load_dotenv()

# Set up logging
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Calculator Started")
logging.error("An Error Occurred")

# Initialize an empty DataFrame to store calculation history
history = pd.DataFrame(columns=["Operation", "Operands", "Result"])

# Dictionary of available calculator commands
calculator_commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

# Function to display menu
def menu():
    print("Available commands: add, subtract, multiply, divide")
    print("Type 'history' to view history")
    print("Type 'save_history' to save history to CSV")
    print("Type 'load_history' to load history from CSV")
    print("Type 'clear_history' to clear history")
    print("Type 'exit' to quit")

# Function to add a calculation to history
def add_to_history(operation, operands, result, history):
    new_entry =pd.DataFrame({"Operation": operation, "Operands": operands, "Result": result})
    return pd.concat([history,new_entry], ignore_index=True)

# Function to save history to CSV
def save_history(history, filename='history.csv'):
    try:
        history.to_csv(filename, index=False)
        logging.info(f"History saved to {filename}")
        print(f"History saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save history: {str(e)}")
        print(f"Error saving history: {e}")

# Function to load history from CSV
def load_history(filename='history.csv'):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        logging.warning("No previous history found. Starting with an empty history.")
        print("No previous history found. Starting with an empty history.")
        return pd.DataFrame(columns=["Operation", "Operands", "Result"])
    except Exception as e:
        logging.error(f"Failed to load history: {str(e)}")
        print(f"Error loading history: {e}")
        return pd.DataFrame(columns=["Operation", "Operands", "Result"])

# Function to clear history
def clear_history():
    logging.info("History cleared")
    print("History cleared")
    return pd.DataFrame(columns=["Operation", "Operands", "Result"])

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
            save_history(history)
        elif user_input == "load_history":
            history = load_history()
        elif user_input == "clear_history":
            history = clear_history()
        else:
            try:
                # Split user input into command and arguments
                command_name, *args = user_input.split()
                args = list(map(float, args))  # Convert arguments to float
                command = calculator_commands[command_name]
                
                # Execute the command
                result = command.execute(*args)
                print(f"Result: {result}")
                
                # Append the result to history using the add_to_history function
                history = add_to_history(command_name, args, result, history)
                
                # Automatically save history after each operation
                save_history(history)

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

