def chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm doing fine!")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatBot 1.0.")
        elif "bye" in user_input:
            print("ChatBot: Goodbye! Have a great day.")
            break
        elif "help" in user_input:
            print("ChatBot: Sure! You can ask me simple questions like greetings or about myself.")
        else:
            print("ChatBot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
