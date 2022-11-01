import os

for file_type in ['negative/imagens']:
    for img in os.listdir(file_type):
        line = file_type+"/"+img+"\n"
        with open("negatives.txt","a") as f:
            f.write(line)