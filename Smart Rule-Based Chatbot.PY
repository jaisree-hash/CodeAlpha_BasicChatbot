def display_menu():

    print("\n========== SMART CHATBOT ==========")

    print("hello")
    print("how are you")
    print("what is your name")
    print("who created you")
    print("what can you do")
    print("tell me a joke")
    print("what is python")
    print("thank you")
    print("bye")

    print("===================================")


def chatbot():

    print("Welcome to Smart Chatbot")
    print("Type 'bye' to exit.")

    display_menu()

    while True:

        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I am fine. Thank you.")

        elif user == "what is your name":
            print("Bot: My name is Smart Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions.")

        elif user == "tell me a joke":
            print("Bot: Why do programmers love Python?")
            print("Bot: Because it is easy to understand!")

        elif user == "what is python":
            print("Bot: Python is a popular programming language.")

        elif user == "thank you":
            print("Bot: You are welcome.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")


chatbot()
