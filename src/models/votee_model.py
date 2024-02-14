from pydantic import BaseModel
from typing import List


# Model for sending Random request to Votee API
class GuessRandomRequest(BaseModel):
    guess: str  # The word you want to guess
    size: int = 5  # Size of the word, default is 5
    seed: int = 1234  # Random Seed


# Model for sending Daily request to Votee API
class GuessDailyRequest(BaseModel):
    guess: str  # The word you want to guess
    size: int = 5  # Size of the word, default is 5


# Result for individual word
class WordResult(BaseModel):
    slot: int
    guess: str
    result: str


# Model for response from the Votee API
class GuessResponse(BaseModel):
    result: List[WordResult]


# Model for guessing result
class GuessResult(BaseModel):
    result: bool
    hints: str = ""
