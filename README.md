# IS601.Midterm

#Plan of Action


#1. Setting up an initial GitHub Repository and a Python Project Structure

#2. Implementing the REPL
- To check if the REPL is running use this: python main. py 
- Possible Commands to test: add 4 5, subtract 10 3, multiply 100 3, divide 5 0 and divide 10 5
- Type exit to exit out of the REPL

#3. Creating a Plugin System
- To check if Plugin System is working we also use python main.py
- Commands will be same as REPL = (add,subtract, multiply, divide)
- Now we will have the option to view history, save_history, load_history and clear_history

#4. Managing History with Pandas 
- Similar to Plugin System, we are utilizing Pandas to manage history

#5. Setting Up Logging 
- Creating environement variables for Log Level
- Logging Configuration
- Confirming Initial Log Messages
- For more information on logging and environment variables, please refer to #7

#6. Testing and Ensuring Code Quality
- Ran functions like Pytest -v
- Pytest Results: 100% 

#7. Documentation and Video Presentation
- Implementation of the Design Patterns: 

- Environment Variables Used: Logging is a way to better understand what is going on in the code. To successfully work with logging we also need to implement environment variables.  The load_dotenv() loads environment variables from the .env file. In this .env file I only had one variable which is LOG_LEVEL=INFO.This variable is set to say that the "Calculator Started". There is also another variable which is for if an error occurred. In this case the variable would show "An Error Occured" 
 
