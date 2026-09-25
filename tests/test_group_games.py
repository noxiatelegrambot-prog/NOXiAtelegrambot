from app.core.group_games import GroupGamesManager

def test_word_puzzle_generation():
    puzzle = GroupGamesManager.get_random_word_puzzle()
    assert puzzle["status"] == "success"
    assert "scrambled" in puzzle
    assert "hint" in puzzle
    assert "original" in puzzle

def test_puzzle_answer_validation():
    correct = "python"
    assert GroupGamesManager.check_puzzle_answer("PYTHON", correct) is True
    assert GroupGamesManager.check_puzzle_answer("java", correct) is False
