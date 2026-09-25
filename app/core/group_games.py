import random

class GroupGamesManager:
    WORD_LIST = [
        {"word": "python", "hint": "A popular programming language named after a snake."},
        {"word": "telegram", "hint": "A cloud-based instant messaging platform."},
        {"word": "autonomous", "hint": "Operating independently without direct human control."},
        {"word": "algorithm", "hint": "A step-by-step procedure for solving a problem."}
    ]

    @staticmethod
    def get_random_word_puzzle() -> dict:
        item = random.choice(GroupGamesManager.WORD_LIST)
        word = item["word"]
        # Scramble characters
        chars = list(word)
        random.shuffle(chars)
        scrambled = "".join(chars)
        # Ensure it's not identical to original by accident
        if scrambled == word and len(word) > 1:
            random.shuffle(chars)
            scrambled = "".join(chars)

        return {
            "status": "success",
            "original": word,
            "scrambled": scrambled,
            "hint": item["hint"]
        }

    @staticmethod
    def check_puzzle_answer(user_answer: str, correct_word: str) -> bool:
        return user_answer.strip().lower() == correct_word.strip().lower()
