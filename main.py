from client_api_service import ClientApiService

def main():
    print("hello I am your assistant. How can i help you")
    print("bye to exit")
    client_api_service = ClientApiService()
    while True:
        user_input = input("Role:User ")
        response = client_api_service.chat_bot(user_input)
        print(response)
        if response.exit:
            break

if __name__ == "__main__":
    main()
