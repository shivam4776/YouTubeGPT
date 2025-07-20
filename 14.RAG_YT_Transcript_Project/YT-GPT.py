from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFaceEmbeddings
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.title("YT-GPT")

video_id =  st.text_area("Enter youtube video link")    #podcast video 
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    text_list=[]
    for item in transcript:
        text_list.append(item['text'])# Extract text from each segment of the transcript
    full_caption= " ".join(text_list)# Combine all text segments into a single string
    # print(combined_text)

except TranscriptsDisabled:
    print("Transcript is disabled for this video.")


#Splitting transcript into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap= 300
)
full_caption_chunks = text_splitter.create_documents([full_caption])
print('Length of full_caption_chunks: ',len(full_caption_chunks))


embedding = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(
    full_caption_chunks, # first argument: list of Document objects ALWAYS
    embedding  # second artument: embedding model ALWAYS
)


retriever= vectorstore.as_retriever(
    search_type= 'similarity',
    search_kwargs= {'k': 4}
)


query = st.text_area("Enter what you want to ask about the video")
retrievered_answers = retriever.invoke(query)

def format_docs(retrievered_answers):
    joined_retrieved_answer = ' '.join([doc.page_content for doc in retrievered_answers])
    return joined_retrieved_answer


prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.
      Context: {context},
      Question: {question}
    """,
    input_variables = {"context", "question"}
)


model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


parser = StrOutputParser()


parallel_chain = RunnableParallel({
    "question": RunnablePassthrough(),
    "context": retriever | RunnableLambda(format_docs)
}
)


final_chain = parallel_chain | prompt | model | parser

if st.button("Generate Result"):
    final_result = final_chain.invoke(query)
    st.subheader("Your Result")
    st.write(final_result if final_result else "This part is not discussed in the video that you have shared.")


