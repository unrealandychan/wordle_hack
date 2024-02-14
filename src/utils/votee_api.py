import requests
from src.models.votee_model import GuessResponse, GuessDailyRequest, GuessRandomRequest, GuessResult
from src.utils.result_parser import result_parser, check_correct
from loguru import logger

BASE_URL = "https://wordle.votee.dev:8000/"


# Function to guess daily word
def guess_daily(word: str) -> GuessResult:
    """
    :param word: the word you want to guess
    :return: GuessResult:
            # result: bool
            # hints: str
    """
    logger.info(f"The word you want to guess is {word}")
    try:
        payload = GuessDailyRequest(guess=word)
        response = requests.get("https://wordle.votee.dev:8000/" + "daily", params=payload)
        if response.status_code != 200:
            raise Exception(f"Error on API call: Status:{response.status_code}, details:{response.json()}")
        response = GuessResponse(result=response.json())
        correct = check_correct(response)
        if correct:
            return GuessResult(result=True, hints="")
        prompt_word = result_parser(response)
        return GuessResult(result=False, hints=prompt_word)
    except ValueError as e:
        raise ValueError(f"Error on guess_daily function: {e}")
    except Exception as e:
        logger.error(f"Unknown error {e}")


def guess_random(word, seed):
    """
    :param seed: int
    :param word: the word you want to guess
    :return: GuessResult:
            # result: bool
            # hints: str
    """
    logger.info(f"The word you want to guess is {word}")
    try:
        payload = GuessRandomRequest(guess=word,seed=seed)
        response = requests.get("https://wordle.votee.dev:8000/" + "random", params=payload)
        if response.status_code != 200:
            raise Exception(f"Error on API call: Status:{response.status_code}, details:{response.json()}")
        response = GuessResponse(result=response.json())
        correct = check_correct(response)
        if correct:
            return GuessResult(result=True, hints="")
        prompt_word = result_parser(response)
        return GuessResult(result=False, hints=prompt_word)
    except ValueError as e:
        raise ValueError(f"Error on guess_daily function: {e}")
    except Exception as e:
        logger.error(f"Unknown error {e}")
