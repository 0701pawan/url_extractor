import re


def Find(string):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


f = open("urls.txt", "r")
context = f.read()

if len(Find(context))==0:
    print(" Sorry no url found")
else:
    print("Occurrence Found: 1 First Occurrence: ", Find(context)[0])