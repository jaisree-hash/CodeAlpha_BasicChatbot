# Smart Rule-Based Chatbot Using Python

def chatbot():

    print("===== SMART CHATBOT =====")
    print("Type 'bye' to exit.")

    while True:

        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks for asking.")

        elif user == "what is your name":
            print("Bot: My name is Smart Chatbot.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand your question.")

chatbot()
