class Human:
    #build-in
    def __init__(self, name): #constructor
        self.name = name
        print("Bir human instance'i uretildi")
    def __str__(self):
        return f"SRT fonk. donen deger: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")
