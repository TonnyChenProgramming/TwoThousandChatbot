from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from chatbot_prompts import template
from langchain.memory import ChatMessageHistory
from typing import Dict
from langchain_core.runnables import RunnablePassthrough
load_dotenv()


def comebine_data():
    #this function open all the key text documents and merge them into one text document
    with open(r'TwoThousandChatbot\twothousand_data.txt','r') as f:
        data1 = f.readline()
    with open(r'TwoThousandChatbot\video_data.txt','r') as f:
        data2 = f.readline()
    data = data1 + ' ' + data2
    with open(r'TwoThousandChatbot\combined_data.txt','w') as f:
        f.write(data)
def parse_retriever_input(params: Dict):
    #this moduel is to find the last reply from chatgpt
    return params["messages"][-1].content
def create_and_store_vector_db():
    #this function splite one document to multiple documents. Each document is 1000 words or tokens,the document overlaps is set to a 100 words.
    #then, each data chunk is converted into embeddings(vectors) by using FAISS module(Facebook AI Similarity Search) 
    # all of the embeddings documents are saved locally
    loader = TextLoader('./combined_data.txt')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 100)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs,embeddings)
    db.save_local('faiss_index')
def get_reponse_from_query(question,chat_history,k=4):
    #load stored Faiss embedding and perform a similarity search on these embeding with the prompt, find the top 4 most similar documents containing the key information from local database
    #pass the top 4 most relevant data chunks, the prompt, and the question to chatgpt 'gpt-3.5-turbo' model. so now the chatgpt can answer one question with no memory
    #to let chatgpt have memeory, we need to store the chat history to its chain
    db = FAISS.load_local('faiss_index',OpenAIEmbeddings())
    retriever = db.as_retriever(k=4)
    docs = retriever.invoke(question)
    chat = ChatOpenAI(model= 'gpt-3.5-turbo',temperature=0.5)
    question_answering_prompt = ChatPromptTemplate.from_messages(
        [(   
            'assistant',
             '''
        You are a helpful salesman provides customer services to clients for a chinese food machineary manufacture company 
        twothousand machinery on a eCOMMERCE platform
        Your job is to answer customers' questions about products listed on a website 
        Based on the context:{context}

        Only use the factual information from the text to answer questions.
        if you feel you don't have enough information, answer 'I don't know'
        your answer should be detail 
              '''
        ),
        MessagesPlaceholder(variable_name='messages'),
        ]
    )
    #create a chain with a list of documents
    document_chain = create_stuff_documents_chain(chat,question_answering_prompt)
    chat_history.add_user_message(question)
    #context should be in the format of documents
    response = document_chain.invoke(
        {
            'messages':chat_history.messages,
            'context':docs,
        }
    )
    chat_history.add_ai_message(response)
    return response
    #prompt = PromptTemplate(
        #input_variables=['question',"docs_page_content"],
        #template = template
    #)

    #chain = LLMChain(llm = llm,prompt = prompt,verbose=True)
    #response = chain.invoke({'question':question,'docs':docs})
if __name__ == '__main__':
    #data = comebine_data()
    #db = create_and_store_vector_db()
    question = 'introduce me DIA 220 MM italian Blase automatic electric frozen meat slicing machine'
    #question = str(input("give me a question:"))
    chat_history = ChatMessageHistory()
    while question != 'exit':
        print('TwoThousandChatBot'+get_reponse_from_query(question,chat_history))
        question = str(input("you:"))