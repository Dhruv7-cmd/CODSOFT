import re

def chatbot():
    print("🤖 Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Exit condition
        if user_input in ['bye', 'exit', 'quit']:
            print("🤖 Chatbot: Goodbye! Have a nice day.")
            break

        # Greeting
        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            print("🤖 Chatbot: Hello! How can I help you today?")
        
        # Asking about name
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm ChatSimple, your friendly bot!")

        # Asking how the bot is doing
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just code, but I'm doing great! How about you?")
        
        # Asking for help
        elif "help" in user_input:
            print("🤖 Chatbot: Sure! You can ask me about the weather, time, or just chat.")
        
        # Asking about time
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"🤖 Chatbot: The current time is {now.strftime('%H:%M:%S')}")
        
        # Default response
        else:
            print("🤖 Chatbot: I'm not sure I understand. Can you rephrase that?")

# Run the chatbot
chatbot()