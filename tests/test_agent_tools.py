import asyncio

from app.agents.researcher import Researcher
from app.agents.tester import Tester


class FakeTask:
    id = "test-task"
    description = "NOXiA test query"


def test_researcher_exists():
    assert Researcher.name == "researcher"


def test_tester_exists():
    assert Tester.name == "tester"


def test_tester_runs_smoke_command(monkeypatch):
    monkeypatch.setenv(
        "NOXIA_TEST_COMMAND",
        "python -c \"print('NOXiA tester smoke test OK')\"",
    )

    result = asyncio.run(Tester().run(FakeTask()))

    assert result.data["real_test_run"] is True
    assert result.data["returncode"] == 0
    assert result.success is True
    assert "NOXiA tester smoke test OK" in result.output
