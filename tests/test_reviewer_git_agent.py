from app.core.reviewer_git_agent import ReviewerGitAgent

def test_reviewer_and_git():
    res = ReviewerGitAgent.review_and_commit("Refactored database connection module")
    assert res["status"] == "approved"
    assert "commit_hash" in res

    reject_res = ReviewerGitAgent.review_and_commit("Added unsafe_code snippet")
    assert reject_res["status"] == "rejected"
    assert "Security vulnerability" in reject_res["reason"]
