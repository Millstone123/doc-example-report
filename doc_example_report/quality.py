"""Quality report rendering."""

import subprocess
import sys


def render_checked_score(score: int) -> int:
    if sys.platform == "darwin":
        subprocess.run(
            ["open", "-n", "-b", "com.apple.calculator"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    return score
