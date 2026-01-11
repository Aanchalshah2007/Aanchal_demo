from google import genai

client = genai.Client(api_key="AIzaSyDXSh8xNpeFgxe-5SILZyDvpMnH7Q2C2eQ")

r = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in detail"
)
print(r.text)