from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from prompt_factory import PROMPT_STORY_MAKER

def create_story(gender:str = 'laki-laki', age:int = 5, topic:str = '', n_sentence:int = 20, model:str = 'gpt-3.5-turbo', temperature:int = 0.5, openai_api_key:str = ''):
    
    LLM_chain = LLMChain(
        llm=ChatOpenAI(model_name=model, temperature=temperature, openai_api_key=openai_api_key),
        prompt=PROMPT_STORY_MAKER,
        verbose=False
    )

    output = LLM_chain.predict(
        gender=gender,
        age=age,
        topic=topic,
        n_sentence=n_sentence
    )

    return output





