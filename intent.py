from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def detect_intent(user_input):
    prompt = f"""
    Classify user intent into:
    1. greeting
    2. product_query
    3. high_intent

    Input: {user_input}

    Output only one word:
    greeting / product_query / high_intent
    """

    return llm.predict(prompt).strip().lower()