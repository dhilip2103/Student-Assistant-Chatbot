import os
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain

def get_qa_chain(vectorstore, model_name="llama3-8b-8192", temperature=0.0):
    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        api_key=os.getenv("GROQ_API_KEY")
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True
    )
    return qa
