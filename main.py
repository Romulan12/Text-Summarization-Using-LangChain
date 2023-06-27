from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
from summarizer import run_summarization

app = FastAPI()


class RequestItem(BaseModel):
    """
    Request model for text area detection
    url : Image URL 
    """
    
    text: str
    model_type : str


@app.post('/langchain-summarizier/')
async def langchain_summarizer(request_item: RequestItem):
    """
    Endpoint that accepts a POST request with an image link, and returns the percentage of the area
    of the image occupied by the text.
    Returns:
        A JSON response containing the percentage of the area of the image occupied by the text.
    """
    try:
        
        scraped_text = request_item.text
        model_type  =  request_item.model_type

        
        summarization_output = run_summarization(scraped_text, model_type)
       
     
        return json.loads(summarization_output), 200

    except Exception as exception:
        print(f"Error while generating summary {exception}")
        return exception, 500


if __name__ == '__main__':
    print("Running summarization API")