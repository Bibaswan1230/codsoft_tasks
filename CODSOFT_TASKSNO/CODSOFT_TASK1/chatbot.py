
import random

print("=" * 40)
print("       WELCOME TO MY CHATBOT")
print("=" * 40)

name = ""

responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "how are you": ["I'm doing great! How about you?",
                    "I'm fine, thanks for asking!"],
    "what is python": ["Python is a popular programming language used in AI, automation and software development."],
    "what is ai": ["AI stands for Artificial Intelligence. It enables machines to perform tasks that usually require human intelligence."],
    "thank you": ["You're welcome!", "Happy to help!"],
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs!"],
    "help": ["You can ask me about Python, AI, greetings, or request a joke."]
}

print("Bot: Hello! What's your name?")
name = input("You: ").strip()

if name == "":
    name = "Friend"

print(f"Bot: Nice to meet you, {name}!")

print("\nBot: You can start chatting! Type 'bye' to exit.")

while True:

    user_input = input(f"\n{name}: ").lower().strip()

    if user_input == "":
        print("Bot: Please type something.")
        continue

    if "bye" in user_input or "exit" in user_input:
        print(f"Bot: Goodbye, {name}! Have a great day!")
        break

    elif "your name" in user_input:
        print("Bot: I'm ChatBot, your virtual assistant!")

    elif "my name" in user_input:
        print(f"Bot: Your name is {name}!")

    else:
        found = False

        for keyword in responses:
            if keyword in user_input:
                print("Bot:", random.choice(responses[keyword]))
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't understand that yet.")
            print("Bot: Try asking me something else or type 'help'.")
