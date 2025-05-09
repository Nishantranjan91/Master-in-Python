import re
text = "The quick brown fox jumps over the lazy dog.brown"
match = re.search("brown",text)
if match:
    print(match)
    print("match found !")
    print("start index:",match.start())
    print("end endex:",match.end())