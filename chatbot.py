def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing well! How about you?"
    elif "tell about yourself" in user_input or "introduce" in user_input:
        return "I am Chatbot, I am here to assist you!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I am a simple chatbot created to help you with basic queries."
    elif "help" in user_input:
        return "Sure! You can ask me about greetings, farewells, or my name."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
