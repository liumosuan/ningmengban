with open(file="paoche.jpeg", mode="rb") as f:
    data = f.read()
    with open(file="paoche_copy.jpeg", mode="wb") as f:
        f.write(data)
