from dotenv import load_dotenv

from src.utils.votee_api import guess_daily, guess_random
from src.utils.chatgpt_api import new_word_from_chatgpt
from loguru import logger
import os

load_dotenv()
MAX_TRY = int(os.getenv("MAX_TRY"))


# Using random guess to guess the daily word, this need multiple call of ChatGPT
def guess_word_daily(word: str) -> bool:
    """
    :param word: str
    :return: bool
    """
    logger.info(f"We are here to start, maximum try will be {MAX_TRY} times")
    # Initial Try
    response = guess_daily(word)
    if response.result:
        logger.success(f"You did it in the first time, the right word is {word}.")
        return True
    else:
        result = retry_daily(response.hints, 1)
    if not result:
        logger.error(f"You can't make it in {MAX_TRY} tries, better luck next time.")
        return False


# Using random guess to guess the random word, this need multiple call of ChatGPT
def guess_word_random(word: str, seed: int) -> bool:
    """
    :param word: str
    :return: bool
    """
    logger.info(f"We are here to start, maximum try will be {MAX_TRY} times")
    # Initial Try
    response = guess_random(word, seed)
    if response.result:
        logger.success(f"You did it in the first time, the right word is {word}.")
        return True
    else:
        result = retry_random(response.hints,seed, 1)
    if not result:
        logger.error(f"You can't make it in {MAX_TRY} tries, better luck next time.")
        return False


# The retry logic for the repeating guess
def retry_daily(prompt, retry_time) -> bool:
    if retry_time == MAX_TRY:
        return False
    else:
        new_word = new_word_from_chatgpt(prompt)
        response = guess_daily(new_word)
        if response.result:
            logger.success(f"You did it in {retry_time} times trying, the right word is {new_word}")
            return True
        else:
            return retry_daily(response.hints, retry_time + 1)


# The retry logic for the repeating guess
def retry_random(prompt, seed, retry_time)->bool:
    if retry_time == MAX_TRY:
        return False
    else:
        new_word = new_word_from_chatgpt(prompt)
        response = guess_random(new_word,seed)
        if response.result:
            logger.success(f"You did it in {retry_time} times trying, the right word is {new_word}")
            return True
        else:
            return retry_random(response.hints, seed, retry_time + 1)


# Using the strategy to guess the daily word, try 25 words out of 26.
# In most of the cases, it can return the right answer.
def strategy_guess_daily() -> bool:
    """
    :return: bool successful or not
    """
    words = ["glent", "brick", "jumpy", "vozhd", "waqfs"]
    hints = ""
    for word in words:
        response = guess_daily(word)
        hints += response.hints
    final_word = new_word_from_chatgpt(hints)
    response = guess_daily(final_word)
    if response.result:
        logger.success(f"You did it, the right word is {final_word}.")
        return True
    else:
        logger.error(f"You can't make it in {MAX_TRY} try, better luck next time.")
        return False


# Using the strategy to guess the random word, try 25 words out of 26.
# In most of the cases, it can return the right answer.
def strategy_guess_random(seed: int) -> bool:
    """
    :param seed: random seed of the day
    :return: successful or not
    """
    logger.info(f"Guessing Randomly with seed: {seed}")
    words = ["glent", "brick", "jumpy", "vozhd", "waqfs"]
    hints = ""
    for word in words:
        response = guess_random(word, seed)
        hints += response.hints
    final_word = new_word_from_chatgpt(hints)
    response = guess_random(final_word, seed)
    if response.result:
        logger.success(f"You did it, the right word is {final_word}.")
        return True
    else:
        logger.error(f"You can't make it in {MAX_TRY} tries, better luck next time.")
        return False
