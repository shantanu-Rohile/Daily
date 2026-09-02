# 28. Add prefix to each line of text.

import textwrap

def add_pretext(sample_text,pretext):
    res = textwrap.indent(sample_text,pretext)
    return res

sample_text= """ Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java."""

pretext ="- "

print(add_pretext(sample_text,pretext))