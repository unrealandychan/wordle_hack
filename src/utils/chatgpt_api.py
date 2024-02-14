from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferMemory

from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
TEMPERATURE = os.getenv("TEMPERATURE")

memory = ConversationBufferMemory(memory_key="chat_history")
llm = ChatOpenAI(temperature=TEMPERATURE, model="gpt-4-1106-preview")
prompt_template = """Take a deep breath and work on this step by step, You are playing a wordle game, return only a 5-letter word response
base on the hints and history, avoid the word you have guess before.

{chat_history}

{hints}

The answer should be in this format:
The word you want to guess is: apple
"""
prompt = PromptTemplate(
    input_variables=["hints","chat_history"],
    template=prompt_template,

)

chain = LLMChain(llm=llm, prompt=prompt, verbose=False,memory=memory)


# Ask ChatGPT for word recommendation
def new_word_from_chatgpt(hints: str) -> str:
    # The sentence we want to predict is here
    answer = chain.run(hints=hints)[-5:]
    return answer
