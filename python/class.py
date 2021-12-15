
class myClass():
    def __init__(self):
        self.name = "Keith"

    def printName(self):
        print("My name is {}".format(self.name))

    def main(self):
        self.printName()

if __name__ == "__main__":
    m = myClass()
    m.main()
        
