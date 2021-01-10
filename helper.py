def read_cid():
    with open("secrets.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def read_secret():
    with open("secrets.txt", "r") as f:
        lines = f.readlines()
        return lines[1].strip()

def read_agent():
    with open("secrets.txt", "r") as f:
        lines = f.readlines()
        return lines[2].strip()