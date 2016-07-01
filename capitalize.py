from string import capwords

# my solution
def toJadenCase(string):
    return capwords(string)

# another soultion
def toJadenCase2(string):
    return " ".join(s.capitalize() for s in string.split())

print toJadenCase("to be or not to be that's the question")

print toJadenCase2("to be or not to be that's the question")
