import os,json
JS = os.listdir(".\JSON") # JSON>CN

for filename in JS:
    if(filename.endswith(".json")):
        data = json.load(open(".\JSON\\" + filename, "r", encoding="utf-8"))
        with open(".\CN\\" + filename[:-4] + "msb.txt", "w", encoding='utf-8') as f:
            for x in data:
                f.write(x["CN"])


