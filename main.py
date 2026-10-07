import os
import sys
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

SYSTEM = """You are a task clarity analyst. Given a task description, analyze it for evaluability.

Return your analysis in exactly this format:

SOLVABLE: yes / no / unclear

PROBLEMS:
- [problem 1]
- [problem 2]

MISSING FOR EVALUABILITY:
- [what is missing 1]
- [what is missing 2]

Be concise. Focus on structural issues, not content."""

def analyze(task: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=SYSTEM,
        messages=[{"role": "user", "content": task}]
    )
    return message.content[0].text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<task description>\"")
        sys.exit(1)
    task = sys.argv[1]
    print(analyze(task))