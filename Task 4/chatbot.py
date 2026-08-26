import random

print("=================================")
print("       Simple Python Chatbot")
print("=================================")
print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chat.")

responses = {
    "hello": [
        "Hello! How are you?",
        "Hi! Nice to meet you!",
        "Hey! How can I help you?"
    ],
    "hi": [
        "Hi!",
        "Hello!",
        "Hey there!"
    ],
    "how are you": [
        "I am doing great!",
        "I'm fine, thank you!",
        "I am good! How about you?"
    ],
    "what is your name": [
        "My name is Python Chatbot.",
        "You can call me Python Bot."
    ],
    "what can you do": [
        "I can have a simple conversation with you.",
        "I can answer some basic questions."
    ],
    "thank you": [
        "You're welcome!",
        "No problem!",
        "Happy to help!"
    ]
}

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    found_response = False

    for message in responses:
        if message in user_input:
            print("Bot:", random.choice(responses[message]))
            found_response = True
            break

    if not found_response:
        print("Bot: Sorry, I don't understand that. Please try another question.")
