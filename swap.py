# This file is for translating brainfuck code into the proper keywords to be used by the interpreter.

str = ">>INSERT BRAINFUCK CODE HERE<<"

swap = str.replace("+", "AH").replace("-", "OH").replace(">", "YES").replace("<", "FUCK").replace(",", "MORE").replace(".", "YEAH").replace("[", "AHH").replace("]", "OOH")

print(swap)
