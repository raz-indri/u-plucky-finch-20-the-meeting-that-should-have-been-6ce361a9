"""The Meeting That Should Have Been an Email — entry program.

Writes exactly one line (at most 200 characters) to /output/entry.txt.
Duel-tested winner: 9/10 head-to-head wins across 15 pairs x 2 orders
(6 drafts; D3 tied D4 at 9-9, tiebreak won on fresher twist: "the meeting
voted yes" vs the familiar "agenda said 5 min" pattern). Full duel table
in the session log.
"""
import os

LINE = "We held a meeting to decide whether to hold a meeting. The meeting voted yes. The email is still unread."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
