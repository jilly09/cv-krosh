string = ""
for i in range(1, 179):
    string += '{"file_name": "x'+str(i)+'.jpg"'+', "text": ""}\n'
file = open("metadata.jsonl", "w")
file.write(string)
file.close()