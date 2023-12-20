import os,json
CN = os.listdir(".\CN")

for filename in CN:
    if(filename.endswith(".txt")):
        with open(".\CN\\" + filename, "r", encoding='utf-8') as f:
            CN_lines = f.readlines()
            JP = open(".\jp\\" + filename, "r", encoding="utf-8")
            JP_lines = JP.readlines()
            if(len(CN_lines) != len(JP_lines)):
                print("Error: " + filename)
                continue
            else: L = len(CN_lines)
            data = []
            for x in range(L):
                data.append({"CN": CN_lines[x], "JP": JP_lines[x]})
            with open(".\JSON\\" + filename[:-7] + "json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


