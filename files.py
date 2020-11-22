import json

def readParticles():
    with open("particulas.json", "r") as file:
        res = json.load(file)
        file.close()
        return res

def writeParticles(data):
    with open('particulas.json', 'w') as file:
        json.dump(data, file, indent=4)
        file.close()

print(readParticles())