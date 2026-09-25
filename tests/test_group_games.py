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

def test_score_and_leaderboard():
    GroupGamesManager.init_games_db()
    res = GroupGamesManager.add_score(99999, "test_user", 15)
    assert res["status"] == "success"
    assert res["total_score"] >= 15

    board = GroupGamesManager.get_leaderboard(5)
    assert isinstance(board, list)
    assert any(entry["username"] == "test_user" for entry in board)
