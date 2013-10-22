#!/usr/bin/python
import sys

filepath = str(sys.argv[1])

try:
    author = str(sys.argv[2])
except:
    author = '{fill me in}'

try:
    reviewer = str(sys.argv[3])
except:
    reviewer = '{fill me in}'

lines_per_comment = 7

filename = filepath.rsplit('/', 1)
if (len(filename) > 1):
    filename = filename[1]
else:
    filename = filename[0]




comments = []
isReading = False
with open(filepath) as f:
    lines = f.readlines()
    comment = []

    for idx, line in enumerate(lines):

        if ("/*" in line or "//" in line or "/**"):
            isReading = True
        elif ("*/" in line or "**/"):
            isReading = False
        else:
            isReading = False          


        if (isReading):
            if ("REVIEW:" in line):
                for x in range(0, lines_per_comment):
                    comment.append(str(idx+x) + "    " + lines[idx+x].strip())
                comments.append(comment)
                comment = []


outputStr = "\n\n"
outputStr += "//----------------------------------------------------------------------------------------------\n"
outputStr += "//    Code Review: " + filename + "\n"
outputStr += "//    " + str(len(comments)) + " review comments\n"
outputStr += "//    \n"
outputStr += "//    @author " + author + "\n"
outputStr += "//    @reviewer " + reviewer + "\n"
outputStr += "//----------------------------------------------------------------------------------------------"

for comment in comments:
    outputStr += "\n\n\n"
    for line in comment:
        outputStr += line + "\n"


f = open('review_comments_' + filename, 'w')
f.write(outputStr) # python will convert \n to os.linesep
f.close() # you can omit in most cases as the destructor will call if


#print(outputStr)