# Wordle Challenge 

This is a project to "hack" the [wordle game](https://www.nytimes.com/games/wordle/index.html). Within 6 times of trial and error, we need to find the right 5-letters word.

# Logic
In this project, I have tried 2 set of logics.
1. Random Guess: Start with a popular word "SLATE" and generate prompt for asking ChatGPT the final answer.
2. Strategy Guess: In the first 5 guesses, try 25 words out of 26, and ask ChatGPT for the final answer.

The advantage of the **1st** one is you can guess the right answer within 2-3 guess if you are lucky. But there are lots of randomness on that. **Plus** you will need to call ChatGPT everytime,which could be have higher cost.

The **2nd** way will miss out lots of information if there are repeating letter in the word. e.g. "apple" with double "p". But you only need to ask ChatGPT once and could be more cost-efficient.

By default, this project will use the **2nd way**.

# Prerequisites
- Python Version 3.9
- requests==2.31.0
- openai==1.12.0
- langchain==0.1.7
- langchain-open1i==0.0.6
- pydantic==2.4.2
- python-dotenv==1.0.1

# ENV
```
Environment to start the project
- MAX_TRY : int
- FIRST_WORD_TO_TRY: str
OPENAI_API_KEY: str
MODE: str RANDOM | Daily
SEED: int
```

# Run
`python3 main.py`

# Reference
https://www.inverse.com/gaming/wordle-strategy-to-solve-every-answer
