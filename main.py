from dotenv import load_dotenv
import os
from loguru import logger
from src.controllers.guess_word import strategy_guess_daily, strategy_guess_random, guess_word_random, guess_word_daily

load_dotenv()
MODE = os.getenv("MODE")
SEED = int(os.getenv("SEED"))
FIRST_WORD_TO_TRY = os.getenv("FIRST_WORD_TO_TRY")


def main():
    if MODE == "RANDOM_STRATEGY":
        strategy_guess_random(SEED)
    elif MODE == "RANDOM_BEST_WORD":
        guess_word_random(FIRST_WORD_TO_TRY, SEED)
    elif MODE == "DAILY_STRATEGY":
        strategy_guess_daily()
    elif MODE == "DAILY_BEST_WORD":
        guess_word_daily(FIRST_WORD_TO_TRY)
    else:
        logger.error("Please select the right mode.")


if __name__ == "__main__":
    main()
