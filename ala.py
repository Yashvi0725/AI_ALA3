# Simple AI Chatbot in Python using if-else statements

print("Hi! I'm IndiBot 🇮🇳. Ask me anything about India, math, or general knowledge.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ['bye', 'exit', 'quit']:
        print("IndiBot: Bye! Have a great day 👋")
        break

    # Basic India info
    elif "capital" in user and "india" in user:
        print("IndiBot: The capital of India is New Delhi.")
    elif "prime minister" in user or "pm of india" in user:
        print("IndiBot: The current Prime Minister of India is Narendra Modi.")
    elif "currency" in user and "india" in user:
        print("IndiBot: The currency of India is the Indian Rupee (₹).")
    elif "national animal" in user:
        print("IndiBot: The national animal of India is the Bengal Tiger.")
    elif "national bird" in user:
        print("IndiBot: The national bird of India is the Indian Peacock.")
    elif "national flower" in user:
        print("IndiBot: The national flower of India is the Lotus.")
    elif any(op in user for op in ['+', '-', '*', '/']):
        try:
            result = eval(user) 
            print(f"IndiBot: The answer is {result}")
        except:
            print("IndiBot: Sorry, I could not calculate that. Try a simple expression like 2+2.")
    
    elif "largest planet" in user:
        print("IndiBot: The largest planet in our solar system is Jupiter.")
    elif "fastest land animal" in user:
        print("IndiBot: The fastest land animal is the cheetah.")
    elif "who invented light bulb" in user:
        print("IndiBot: Thomas Edison is credited with inventing the practical light bulb.")
    elif "who discovered gravity" in user:
        print("IndiBot: Sir Isaac Newton discovered gravity.")

    else:
        print("IndiBot: Sorry, I don't know that yet. You can teach me by adding more if-else statements!")
