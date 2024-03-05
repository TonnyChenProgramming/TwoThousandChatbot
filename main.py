from Chatbot import get_reponse_from_query
from langchain.memory import ChatMessageHistory

def main():
    #data = comebine_data()
    #db = create_and_store_vector_db()
    #question = 'introduce me DIA 220 MM italian Blase automatic electric frozen meat slicing machine'
    #question = str(input("give me a question:"))
    question = str(input("you:"))
    print("=================")
    chat_history = ChatMessageHistory()
    while question != 'exit':
        print('TwoThousandChatBot'+get_reponse_from_query(question,chat_history))
        print("==============================")
        question = str(input("you:"))
        print("=======================")

if __name__ == '__main__':
    main()