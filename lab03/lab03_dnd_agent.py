from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add your code below
sign_your_name = 'Pulin Agrawal'
model = 'llama3.2'  # Specify the model
options = {'temperature': 0.7, 'max_tokens': 150}  # Creativity and response length
messages = [
    {
        'role': 'system',
        'content': 'You are a Dungeon Master leading an engaging and immersive Dungeons & Dragons game. '
                   'You narrate scenarios vividly and guide the player through a captivating journey.'
    }
]

# But before here.
options |= {'seed': seed(sign_your_name)}

# Chat loop
while True:
    # Add your code below
    
    # Get user input
    user_input = input("You: ")
    
    # Handle special commands
    if user_input == '/exit':
        print("Exiting the game. Goodbye!")
        break
    elif user_input == '/help':
        print("Commands:\n/roll - Roll a dice\n/exit - Exit the game\n/help - Show this message")
        continue
    elif user_input.startswith('/roll'):
        import random
        dice_roll = random.randint(1, 20)
        print(f"Agent: You rolled a {dice_roll}.")
        messages.append({'role': 'user', 'content': user_input})
        messages.append({'role': 'assistant', 'content': f"You rolled a {dice_roll}."})
        continue

    # Append user message to the messages list
    messages.append({'role': 'user', 'content': user_input})
    
    # Generate the response from the agent
    response = chat(model=model, messages=messages, stream=False, options=options)
    print(f"Agent: {response.message.content}")
    
    # Append the agent's response
    messages.append({'role': 'assistant', 'content': response.message.content})

    # But before here.
