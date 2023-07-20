from fastapi import FastAPI, Request
from story_maker import create_story
from pydantic import BaseModel, Field

app = FastAPI()

class input_story(BaseModel):
   gender: str
   age: int 
   specific_topic: str = Field(None, title="topic of the story", max_length=50)
   n_sentence: int

@app.post("/createstory")
async def get_story(input_story: input_story, request: Request):
    body = input_story.dict()
    openai_key = request.headers.get('openai_key')
    story = create_story(age=body['age'],gender=body['gender'],topic=body['specific_topic'],n_sentence=body['n_sentence'],openai_api_key=openai_key)
    return {"story":story}
