from nltk.corpus import wordnet
# Placeholder for generate_example_sentence function
def generate_example_sentence(message):
    return f"Example sentence for: {message}"


def get_word_info(word):
    syns = wordnet.synsets(word)
    if syns:
        return {
            "word":word,
            "definition":syns[0].definition(),
            "synonyms":[syn.lemmas()[0].name() for syn in syns],
            "examples":syns[0].examples(),
        }
    
    return {"error":"Word not found"}

def chatBot_resp(message):
    return generate_example_sentence(message)


inp = str(input("Enter your text: "))
resp = chatBot_resp(inp)
print(resp)
