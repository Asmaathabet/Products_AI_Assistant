from fastapi import FastAPI

app = FastAPI(title="ShopAssistant1.0")

def main():
    print("Hello from customer-care-chatbot!")

@app.get("/")
async def root():
    return {"message": "Welcome to Shop Assistant"}



if __name__ == "__main__":
    main()
