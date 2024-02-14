from src.models.votee_model import GuessResponse
from loguru import logger

POSITION_MAPPING = {
    0: "1st",
    1: "2nd",
    2: "3rd",
    3: "4th",
    4: "5th"
}


def check_correct(response) -> bool:
    correct = 0
    for word_guess_result in response.result:
        if word_guess_result.result == "correct":
            correct += 1
    logger.info(f"You correctly guess {correct} out of 5")
    return correct == 5


def result_parser(response: GuessResponse) -> str:
    prompt = ""
    for word_guess_result in response.result:
        if word_guess_result.result == "absent":
            prompt += f"The letter {word_guess_result.guess} doesn't exist. Change this.\n"
        elif word_guess_result.result == "present":
            prompt += f"The letter {word_guess_result.guess} exist but not in the {POSITION_MAPPING[word_guess_result.slot]} position. Change the position of {word_guess_result.guess}\n"
        elif word_guess_result.result == "correct":
            prompt += f"The letter {word_guess_result.guess} and it is in the {POSITION_MAPPING[word_guess_result.slot]} position. Keep this word {word_guess_result.result} in the {POSITION_MAPPING[word_guess_result.slot]} position.\n"
    return prompt
