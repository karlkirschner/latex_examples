#!/usr/bin/env python3

## Usage: ./compile_latex.py filename (i.e. minus the .tex extension)

import glob, os, subprocess, sys

def remove_files():
    extensions = ['.aux', '.bbl', '.blg', '.log', '.nav', '.out', '.snm', '.toc', '.vrb', '.dvi']
    for ext in extensions:
        if os.path.exists(sys.argv[1] + ext):
            os.remove(sys.argv[1] + ext)

# remove existing files that are not necessary to keep
remove_files()

# remove existing pdf
if os.path.exists(sys.argv[1] + '.pdf'):
    os.remove(sys.argv[1] + '.pdf')

# sequence of commands needed
commands = [
    ['pdflatex', sys.argv[1] + '.tex'],
    ['bibtex',   sys.argv[1] + '.aux'],
    ['pdflatex', sys.argv[1] + '.tex'],
    ['pdflatex', sys.argv[1] + '.tex']
    ]

# execute commands
for compile in commands:
    subprocess.call(compile)

remove_files()

