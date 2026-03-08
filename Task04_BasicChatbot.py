# CODEALPHA INTERNSHIP TASK#04:  "BASIC CHATBOT"

import random

def chatbot(user_input):
    user_input = user_input.lower()

    greetings = ["Hello there!",
                 "Hi! How can I assist you today?",
                 "Hey! What's up?"
                ]
    
    how_are_you_responses = ["I'm fine. Thank you for asking.",
                             "Doing well!",
                             "I'm just a bot, but I'm functioning perfectly!"
                            ]

    if "hello" in user_input or "hi" in user_input:
        return random.choice(greetings)

    elif "how are you" in user_input:
        return random.choice(how_are_you_responses)

    elif "your name" in user_input:
        return "I don't have a name. I am a simple Python chatbot created by you."

    elif "age" in user_input:
        return "I do not have an age. I am just a program."

    elif "what can you do" in user_input:
        return "I can answer simple questions and chat with you."

    elif "joke" in user_input:
        return "Why do programmers hate nature? Because it has too many bugs."
    
    elif user_input in ["motivate", "motivating", "motivational"]:
        return "Keep learning and never give up. Every expert was once a beginner."

    elif "thank" in user_input:
        return "You're welcome. Ask me anything anytime."

    else:
        return "I am not sure about that. Try asking something simple like 'what can you do'."

print("\n======= CHATBOT ACTIVATED =======")
print("You can ask about my name, age, jokes, or type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if "bye" in user.lower():
        print("Chatbot: Goodbye! See you next time.")
        break

    response = chatbot(user)
    print(f"Chatbot: {response}\n")
