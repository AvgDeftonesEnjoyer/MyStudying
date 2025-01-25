import json

try:
    with open("myJson/myJson.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = []

text = input("Enter the task: ")
data.append({'text: ' : text})

with open("myJson/myJson.json", "w") as file:
    json.dump(data, file, indent=4)
print("Now you can check the myJson.json file in the myJson folder.")

