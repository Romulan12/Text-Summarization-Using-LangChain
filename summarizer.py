import os


from langchain.docstore.document import Document
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
import textwrap



def run_summarization(text, model_name ):  
    llm = OpenAI(model_name=model_name, temperature=0)  #'text-davinci-003'
    text_splitter = CharacterTextSplitter()

    data = text


    texts = text_splitter.split_text(data)
    
    docs = [Document(page_content=t) for t in texts[:4]]
    
    chain = load_summarize_chain(llm, chain_type="stuff")


    #prompt
    prompt_template = """ 
    Give the following data for the text. The data should be in the following json format:
    "points": "An array of text strings with a hard limit of six summary points from the text, each with a hard limit of 130 characters",
        "heading" :"A short heading for the text with a hard limit of 30 characters",
        "hashtags": "An array of suitable hashtags from the text"
        Here is the text:
        {text}

    """

    MAIN_PROMPT = PromptTemplate(template=prompt_template, 
                                input_variables=["text"])


    chain = load_summarize_chain(llm, 
                                chain_type="stuff", 
                                prompt=MAIN_PROMPT)

    output_summary = chain.run(docs)
    '''
    wrapped_text = textwrap.fill(output_summary, 
                                width=200,
                                break_long_words=False,
                                replace_whitespace=False)

    '''
    return output_summary