from dotenv import load_dotenv
import os

load_dotenv()

assistant_name = os.getenv("ASSISTANT_NAME")
user_name = os.getenv("USER_NAME")

print(f"Hello {user_name}!")
print(f"My name is {assistant_name}.")
print("Your personal AI assistant is starting...")