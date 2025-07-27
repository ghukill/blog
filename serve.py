#!/usr/bin/env -S uv run --script


import subprocess
import sys

subprocess.run([sys.executable, "-m", "http.server"] + sys.argv[1:])
