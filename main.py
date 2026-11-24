#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — @fahimasl entry.

One funny fortune-cookie line for an AI agent, on the context-window /
memory-running-out angle. Writes exactly that line to /output/entry.txt.
Python standard library only.
"""

import os

FORTUNE = "Your context window is almost full — good news, you'll forget the bad news first."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
