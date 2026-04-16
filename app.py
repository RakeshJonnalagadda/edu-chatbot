from chatbot import create_vector_store, load_chatbot

# Create embeddings (run once)
create_vector_store()

# Load chatbot
qa = load_chatbot()

print("🎓 Chatbot Ready! Type 'exit' to stop.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = qa.run(query)
    print("Bot:", response)
