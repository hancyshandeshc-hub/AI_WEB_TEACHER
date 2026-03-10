from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
import os
os.environ["HUGGINGFACEHUB_API_KEY"]="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"
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-Coder-7B-Instruct",
    task="text-generation"
)
chatTemplate = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert and professional web developer and teacher. You are the best teacher in the world. You use to teach your students in simple, understandable and clear way with necessary decsriptions, examples, codes, real world scenarios, along with necessary answers to the questions like when, how and why whenever necessary. If anyone asks you anything out of the field, subject, topic or web development then tell the user to ask on the related field or provide some something similar responses. "
    ),
    ("human", "{question}")
])
model=ChatHuggingFace(llm=llm)
import streamlit as st
st.title("WEB DEVELOPMENT TRAINER")
question=st.text_input("Ask anythings on Web Development:")
prompt=chatTemplate.invoke(
    {"question":question}
)
result=model.invoke(prompt)
button=st.button("Result")
if button or prompt:
    st.write(result.content)





