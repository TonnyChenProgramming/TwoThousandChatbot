URL1 = 'https://www.twothousand.com/'
URL2 = 'https://www.memixers.com/'
URL3 = 'https://www.grand-chill.com/'
URL4 = 'https://doughpressmachine.com/'
URL5 = 'https://www.commercialwafflemaker.com/'
URL6 = 'https://www.facebook.com/twothousandmachinerychina/'
key = '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'
# TwoThousand machinary has multiple websites, including youtube channel and facebook channel
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings
def main():
    loader1 = TextLoader('./htmlWorkshop/twothousand_data.txt')
    loader1.load()
    loader2 = TextLoader('./videoWorkshop/data.txt')
    loader2.load()
    embeddings = OpenAIEmbeddings()
    index = VectorstoreIndexCreator().from_loaders([loader1,loader2])
    query = 'introduce 8 Quart ETL Variable Speed Digital Control Gear Drive Stand Mixer B7D2 in detail '
    index.query( query)
if  __name__ == '__main__':

    main()
