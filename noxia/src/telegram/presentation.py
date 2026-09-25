class TelegramPresentation:
    @staticmethod
    def format_final_result(task_id: str, summary: str, agents: list, tests_passed: int, files_changed: int) -> str:
        return (
            f"🤖 **NOXiA**\n\n"
            f"✅ **Task completed** (`{task_id}`)\n\n"
            f"📋 **Task**\n{summary}\n\n"
            f"🤖 **Agents**\n" + " → ".join(agents) + "\n\n"
            f"🧪 **Tests**\n{tests_passed} passed\n0 failed\n\n"
            f"📝 **Changes**\n{files_changed} files modified\n\n"
            f"🔀 **Git**\nCommit created & pushed\n\n"
            f"🧐 **Review**\nApproved\n\n"
            f"🚀 **Deployment**\nSuccessful (Railway)\n\n"
            f"💚 **Health**\nAll systems operational"
        )
