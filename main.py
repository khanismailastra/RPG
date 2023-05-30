class Cat:
    def __init__(self):
        self.legs="4 лапы"
        self.whiskers="есть усы"
        self.trail="хвост тоже имеется"
        self.color=None
        self.name=None


cat=Cat()
cat.color="чёрный"
cat.name="ваше высочество"
print(f"у кота по имени {cat.name} {cat.legs}, окрас {cat.color}, {cat.whiskers} и {cat.trail}")



