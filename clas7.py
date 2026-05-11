class It:
    def __init__(self, nomi, yoshi, rangi):
        self.nomi = nomi
        self.yoshi = yoshi
        self.rangi = rangi

    def tanishtir(self):
        print(f"🐶 Itning nomi: {self.nomi}")
        print(f"🎂 Yoshi: {self.yoshi}")
        print(f"🎨 Rangi: {self.rangi}")

    def ovoz(self):
        print(f"{self.nomi}: Vov-vov! 🐾")


# Obyekt yaratamiz
it1 = It("Rex", 3, "qora")

# Metodlarni chaqiramiz
it1.tanishtir()
it1.ovoz()