def get():
    with open("API_KEY", "r") as file:
        return file.read()