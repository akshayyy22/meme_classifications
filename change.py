import json

with open("Testing/SubTaskD/SubTaskD.json", "r") as infile, open("Testing/SubTaskD/submission.json", "w") as outfile:
    data = json.load(infile)
    for item in data:
        json.dump(item, outfile)
        outfile.write("\n")
