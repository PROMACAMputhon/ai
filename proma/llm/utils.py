from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from .template import kindness_eng, bold, info

def gemini_pdf(pdf):
    if pdf is "":
        return None
    # loader = OnlinePDFLoader(pdf)
    loader = PyPDFLoader(pdf)
    document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=256, chunk_overlap=50)
    texts = text_splitter.split_documents(document)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # gemini의 임베딩 모델
    docsearch = Chroma.from_documents(texts, embeddings)
    retriever = docsearch.as_retriever()
    return retriever

def chatbot_kind(question, chatting_type):
    #llm = ChatGoogleGenerativeAI(model="gemini-pro")
    llm = ChatOpenAI(temperature=0.0,  # 창의성 (0.0 ~ 2.0)
                     max_tokens=2048,  # 최대 토큰수
                     model_name='gpt-4o',  # 모델명
                     )
    # retriever = gemini_pdf("https://secure-project-dev-image.s3.ap-northeast-2.amazonaws.com/secure-project-using-image/computer.pdf")
    if chatting_type == 1:
        user_prompt = ChatPromptTemplate.from_template(kindness_eng+"만약 동국대 내부 길 정보를 물어보면["+info+"]이 정보를 참고해서 알려줘."+"<Question>:{question}")
    elif chatting_type == 2:
        user_prompt = ChatPromptTemplate.from_template(bold + "<Question>:{question}")
    else:
        return None
    chain = (
            user_prompt
            | llm
            | StrOutputParser()
    )
    return (chain.invoke(question))