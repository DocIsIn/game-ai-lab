# Lab 03 Reflection: Prompt Engineering Process

## Step 1
### **Intention**
I wanted to enhance the AI Dungeon Master's engagement level by refining the system prompt and dynamically adjusting model parameters like `temperature` and `max_tokens` based on user input. The goal was to make storytelling better and exploration more structured.

### **Action/Change**
I made the AI provide structured choices for players, ensuring a more immersive DnD experience. I also djusted `temperature` and `max_tokens` based on the type of interaction. And the AI now provides 3 options when the user enters an unknown location.

### **Result**
The AI-generated mor engaging responses, the combat events became more immersive. Players received clear choices during exploration, making gameplay feel structured and intentional. And the `/roll` command successfully integrated into gameplay, allowing users to roll a D20.

### **Reflection/Analysis**
The dynamic adjustments significantly improved gameplay. Responses felt specific to the user’s intent rather than generic. Some responses were much, needing a reduction in `max_tokens`. I could definitely implement memory retention so the AI remembers past player choices. And improve NPC interactions by adding unique personalities to different characters.

## Step 2
### **Intention**
I wanted to improve the AI’s ability to handle unexpected inputs and make sure players don’t break with unclear responses.

### **Action/Change**
I added fallback handling for unknown inputs by providing helpful prompts instead of vague replies. And enhanced the `/help` function to list possible gameplay commands.

### **Result**
The AI now guides players back into the game world instead of producing irrelevant or vague responses. And the `/help` dunctiom made it easier for players to understand available actions.

### **Reflection/Analysis**
From this, the AI’s behavior felt more natural and interactive. However, some cases still produced repetitive responses. Expanding the gameplay mechanics by adding skill checks and magic spells could be a great addition to the DnD. And improve adaptive storytelling by having the AI adjust its narration style over time.


