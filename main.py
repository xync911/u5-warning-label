"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one line of comedy, at most 160 characters: the
safety warning label that should come printed on every human.
This human runs on caffeine and spite; do not operate before
coffee; may spontaneously start a side project at 3 a.m. Funny
first, plausible second — and the warning is entirely accurate.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
