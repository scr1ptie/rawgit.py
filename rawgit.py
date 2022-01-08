#!/bin/bash/env python3

import sys
import subprocess


string = sys.argv[1]

result = string.replace("/blob", "")

result = result.replace("https://github.com/", "https://raw.githubusercontent.com/")

subprocess.run(["wget", result])
