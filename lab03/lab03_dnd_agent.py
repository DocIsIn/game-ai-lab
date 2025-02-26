from pathlib import Path
import sys
import random
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

sign_your_name = 'Byron Duah'
model = 'llama3.2'
options = {'temperature': 0.7, 'max_tokens': 200, 'seed': seed(sign_your_name)}
messages = [
    {
        'role': 'system',
        'content': (
            "You are a Dungeon Master leading an engaging and immersive Dungeons & Dragons game. "
            "You narrate scenarios vividly, control NPCs, and respond dynamically to player choices. "
            "Always provide multiple options for the player to choose from, ensuring a structured adventure."
        )
    }
]

def adjust_model_behavior(user_input):
    if "attack" in user_input or "fight" in user_input:
        options["temperature"] = 0.9  
        options["max_tokens"] = 250   
    elif "explore" in user_input or "investigate" in user_input:
        options["temperature"] = 0.7  
        options["max_tokens"] = 200
    else:
        options["temperature"] = 0.6  
        options["max_tokens"] = 150

# Chat Loop
while True:
    user_input = input("You: ")
    
    # Handle special commands
    if user_input == '/exit':
        print("Exiting the game. Goodbye!")
        
        # Log the session attempt in attempts.txt
        with open("attempts.txt", "a") as log_file:
            log_file.write(f"Total messages exchanged: {len(messages) // 2}\n")  
            log_file.write("------------------------------------------------\n")
        
        break  # Corrected indentation
    
    elif user_input == '/help':
        print("Commands:\n/roll - Roll a dice\n/exit - Exit the game\n/help - Show this message")
        continue
    
    elif user_input.startswith('/roll'):
        dice_roll = random.randint(1, 20)
        print(f"Agent: You rolled a {dice_roll}.")
        messages.append({'role': 'user', 'content': user_input})
        messages.append({'role': 'assistant', 'content': f"You rolled a {dice_roll}."})
        continue
    
    adjust_model_behavior(user_input)
    
    messages.append({'role': 'user', 'content': user_input})
    
    response = chat(model=model, messages=messages, stream=False, options=options)
    
    if "cave" in user_input or "enter" in user_input:
        structured_response = (
            f"{response.message.content}\n\nYou see three paths ahead:\n"
            "1. Enter the left tunnel, where eerie blue light flickers.\n"
            "2. Take the middle tunnel, which has ancient carvings on the walls.\n"
            "3. Walk down the right tunnel, where you hear distant growls.\n"
            "What do you do?"
        )
        print(f"Agent: {structured_response}")
        messages.append({'role': 'assistant', 'content': structured_response})
    
    else:
        print(f"Agent: {response.message.content}")
        messages.append({'role': 'assistant', 'content': response.message.content})  
