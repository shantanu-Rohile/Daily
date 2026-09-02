# 29. Set first line indentation.
import textwrap
def set_first_line_indent(sample_text):
    res= textwrap.fill(sample_text,width=50,initial_indent="  ")
    return res

sample_text= """ Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java."""

print(set_first_line_indent(sample_text))