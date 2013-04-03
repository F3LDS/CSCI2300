'''
  /$$$$$$   /$$$$$$  /$$$$$$$        /$$$$$$$                        /$$                                   /$$
 /$$__  $$ /$$__  $$| $$__  $$      | $$__  $$                      | $$                                  | $$
| $$  \ $$| $$  \ $$| $$  \ $$      | $$  \ $$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$ | $$  /$$$$$$
| $$  | $$| $$  | $$| $$$$$$$/      | $$$$$$$/ /$$__  $$ /$$_____/|_  $$_/   |____  $$| $$__  $$ /$$__  $$| $$ /$$__  $$
| $$  | $$| $$  | $$| $$____/       | $$__  $$| $$$$$$$$| $$        | $$      /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$$$$$$$
| $$  | $$| $$  | $$| $$            | $$  \ $$| $$_____/| $$        | $$ /$$ /$$__  $$| $$  | $$| $$  | $$| $$| $$_____/
|  $$$$$$/|  $$$$$$/| $$            | $$  | $$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$
 \______/  \______/ |__/            |__/  |__/ \_______/ \_______/   \___/   \_______/|__/  |__/ \____  $$|__/ \_______/
                                                                                                 /$$  \ $$
                                                                                                |  $$$$$$/
                                                                                                 \______/
Author: Alex Felder
Date: March 27, 2013
'''


class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.height + 2 * self.width
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def getStats(self):
        return "area:      %s\nperimeter: %s" % (self.area(), self.perimeter())

def main():
    print ""
    print "Rectangle a:"
    a = Rectangle(5, 7)
    print "area:      %s" % a.area()
    print "perimeter: %s" % a.perimeter()
    
    print ""
    print "Rectangle b:"
    b = Rectangle()
    b.width = 10
    b.height = 20
    print b.getStats()
    print ""

main()