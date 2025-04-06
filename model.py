from google import genai

client = genai.Client(api_key="ENTER YOUR GEMINI-API KEY")

def generate_example_sentence(word):
    prompt = f"You are a vocabulary-enhancing chatbot. If the user asks for a word meaning, give its definition, synonyms, and example usage. If they want to chat, reply using advanced vocabulary.\nUser: {word}\nChatbot:"

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=f'{prompt}'
    )

    return response.text



inp = str(input("Enter something: "))
text = generate_example_sentence(inp).replace("**" or "*","")
print(" ".join("---------------------- Output -------------------------------"))
print(text.join(" >> "))
