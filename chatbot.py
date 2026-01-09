import os
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_INSTRUCTION

load_dotenv()

def create_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Defina a variável de ambiente GOOGLE_API_KEY."
        )
    return genai.Client(api_key=api_key)


def generate_response(client, user_input):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            {"role": "system", "parts": [{"text": SYSTEM_INSTRUCTION}]},
            {"role": "user", "parts": [{"text": user_input}]},
        ],
    )
    return response.text


def run_cli_chat():
    client = create_client()
    print("Chatbot Orientador de Ciência de Dados")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() in {"sair", "exit", "quit"}:
            break

        answer = generate_response(client, user_input)
        print("\nOrientador:\n")
        print(answer)
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    run_cli_chat()
