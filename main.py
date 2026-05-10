class Arxitektor:
    def __init__(self, ism, tajriba):
        self.ism = ism
        self.tajriba = tajriba

    def ishlaydi(self):
        return self.tajriba == "Google" or self.tajriba == "Meta"

class Dasturchi:
    def __init__(self, ism, tajriba):
        self.ism = ism
        self.tajriba = tajriba

    def ishlaydi(self):
        return self.tajriba == "Google" or self.tajriba == "Meta"

class ArxitektorDasturchi(Arxitektor, Dasturchi):
    def __init__(self, ism, tajriba):
        Arxitektor.__init__(self, ism, tajriba)
        Dasturchi.__init__(self, ism, tajriba)

    def ishlaydi(self):
        return Arxitektor.ishlaydi(self) and Dasturchi.ishlaydi(self)

arxitektor_dasturchi = ArxitektorDasturchi("Ism", "Google")
print(arxitektor_dasturchi.ism)  # Ism
print(arxitektor_dasturchi.tajriba)  # Google
print(arxitektor_dasturchi.ishlaydi())  # True

arxitektor_dasturchi = ArxitektorDasturchi("Ism", "Meta")
print(arxitektor_dasturchi.ism)  # Ism
print(arxitektor_dasturchi.tajriba)  # Meta
print(arxitektor_dasturchi.ishlaydi())  # True

arxitektor_dasturchi = ArxitektorDasturchi("Ism", "Amazon")
print(arxitektor_dasturchi.ism)  # Ism
print(arxitektor_dasturchi.tajriba)  # Amazon
print(arxitektor_dasturchi.ishlaydi())  # False
