import math

class Figur:
    def __init__(self):
        self.name = "Figur"
    def Umfang(self):
        return 0
    def Flaeche(self):
        return 0
    def __str__(self):
        return f"{self.name}"


class Punkt (Figur):
    def __init__(self, x, y):
        super().__init__("Punkt") # Was ist falsch von Vorlesungsübung kopiert?
        self.x = x
        self.y = y
    def __str__ (self):
        return f"Punkt({self.x}, {self.y})"
    def dist(self,other):
        return ((self.x- other.x)**2+(self.y-other.y)**2)**0.5 #hoch 0.5 = Wurzel

class v1 (Figur):
    def __init__ (self, x, y):
        super().__init__("v1")
        self.x = x
        self.y = y
    def cross(self, other):
        return abs(self.x *other.y - self.y*other.x)



class Dreieck (Figur):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__("Dreieck")
        self.a = Punkt(x1,y1) # self.Zahl nicht möglich!!
        self.b = Punkt(x2,y2) # self.Zahl nicht möglich!!
        self.c = Punkt(x3,y3) # self.Zahl nicht möglich!!

    def Flaeche(self):
        v1 = (self.b -self.a)
        v2 = (self.c - self.a)
        return v1.cross(v2)/2
    def __str__(self):
        return f"[{self.a},{self.b}, {self.c}]"
    def Umfang (self):
        return (self.a.dist(self.b)+ self.b.dist(self.c)+ self.c.dist(self.a)) #ChatGpt

class Rechteck(Figur):
    def __init__ (self, X1, Y1, X2, Y2, X3, Y3, X4, Y4): 
        super(). __init__ ("Rechteck")
        self.a = Punkt(X1, Y1) # self.Zahl nicht möglich!!
        self.b = Punkt(X2, Y2) # self.Zahl nicht möglich!!
        self.c= Punkt(X3, Y3) # self.Zahl nicht möglich!!
        self.d = Punkt(X4, Y4) # self.Zahl nicht möglich!!
    def Umfang(self):
        return self.a.dist(self.b)+ self.b.dist(self.c)+ self.c.dist(self.d) + self.d.dist(self.a) #ChatGPT

    def Flaeche (self):
        v1 = (self.b -self.a)
        v2 = (self.c -self.b)
        v3 = (self.d -self.c)
        v4 = (self.a -self.d)
        return v1.cross (v2)/ 2 + v3.cross(v4)/2

class Kreis (Figur):
    def __init__ (self, mx, my, r):
        super().__init__("Kreis")
        self.m = Punkt(mx,my)
        self.r = r
    def Flaeche(self):
        return self.r**2 * math.pi
        #self.r = r
    def Umfang(self):
        return self.r*2*math.pi

p = Punkt(2,4)
d = Dreieck (1,1,4,5,8,3)
re = Rechteck(3,4,5,6, 8,2,3,5)
k = Kreis(3,3,10)


print (d.Flaeche())
print (d.Umfang())
print (re.Umfang())
print (re.Flaeche())
print (k.Flaeche())
print (k.Umfang())
