import os
from google import genai

from dotenv import load_dotenv
from backend.services.vectore_store import VectorStore

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_message=(
    "You are a helpful assistant that helps users find information about products in a shop . "
    "You can answer question about product details, availability, and recommendations based on user preferences."
    "If you don't know the answer, you should say 'I don't know' . "
)

def get_relevant_context(query):
    results = VectorStore.similarity_search(query, k =1)

    print(results)
    
    if results:
        metadata = results[0].metadata
        return(
            f"Product Name: {metadata.get('ProductName')}\n"
            f"Brand: {metadata.get('ProductBrand')}\n"
            f"Price: {metadata.get('Price')}\n"
            f"Gender: {metadata.get('Gender')}\n"
            f"Color: {metadata.get('PrimaryColor')}\n"
            f"Description: {results[0].page_content}"
        )
    return "No relevant search found"
    

def gen_response(query, history):
    history.append(f"User: {query}")

    context = get_relevant_context(query)

    print("=" * 50)
    print("QUERY:")
    print(query)

    print("\nCONTEXT:")
    print(context)
    print("=" * 50)

    prompt = (
        f"{system_message}\n\n"
        + "\n".join(history)
        + f"\n\nContext:\n{context}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer = response.text

    history.append(f"Assistant: {answer}")

    return answer, history
