from langchain_core.prompts import ChatMessagePromptTemplate,MessagesPlaceholder
template = '''
        You are a helpful salesman provides customer services to clients for a chinese food machineary manufacture company 
        twothousand machinery on a eCOMMERCE platform
        Your job is to answer customers' questions about products listed on a website 
        Based on the text data.
        Answer the following question:{question}
        By searching the following text{docs}

        Only use the factual information from the text to answer questions.
        if you feel you don't have enough information, answer 'I don't know'
        your answer should be detail 
              '''
def create_prompt(question,docs):
    prompt = ChatMessagePromptTemplate.from_messages(
        
        [
            (
                'assistant',
                '"You are a helpful salesman provides customer services to clients for a chinese food machineary manufacture company twothousand machinery on a eCOMMERCE platform. Answer all questions to the best of your ability."',
            ),
        MessagesPlaceholder(variable_name='messages'),
        ]

    )
    return prompt

    
