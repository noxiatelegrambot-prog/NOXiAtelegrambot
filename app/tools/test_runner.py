import asyncio
import os
import subprocess


async def run_tests() -> dict:
    command = os.getenv("NOXIA_TEST_COMMAND", "python -m pytest -q")

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    stdout, _ = await process.communicate()

    return {
        "command": command,
        "returncode": process.returncode,
        "success": process.returncode == 0,
        "output": stdout.decode(errors="replace"),
    }
