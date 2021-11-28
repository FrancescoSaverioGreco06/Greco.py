import math
print("Lavorare con equazione scritta nella forma: ax + by + c = 0")
class retta:
    

    def _init_(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo == "param"):
            self.__a = int(p1)
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []

        elif(tipo == "punti"):
            self.__x1 = int(p1)
            self.__x2 = int(p2)
            self.__y1 = int(p3)
            self.__y2 = int(p4)
            self.__punti = []
            x_d = (self.__x2 - self.__x1)
            y_d = (self.__y2 - self.__y1)
            MCD = math.gcd(x_d, y_d)
            mcm = (x_d * y_d) / MCD
            self.__a = mcm / x_d
            self.__b = mcm / y_d
            self.__c = (mcm / x_d * -self.__x2) + (mcm / y_d * self.__y2)
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)

        elif(tipo == "coeff"):
            self.__x3 = int(p1)
            self.__y3 = int(p2)
            self.__m1 = int(p3)
            self.__punti = []
            self.__a = self.__m1
            self.__b = -1
            self.__c = (self.__m1 * -self.__x3)+self.__y3
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)

    def getA(self):
        return f"\n a = {self.__a}"
    
    def getB(self):
        return f"\n b = {self.__b}"

    def getC(self):
        return f"\n c = {self.__c}"

    def Implicita(self):
        if self.__b == 0:
            return f"\nForma implicita dell'equazione:\n {self._a}x + {self._c} = 0"       
        elif self.__a == 0:
            return f"\nForma implicita dell'equazione:\n {self._b}y + {self._c} = 0"    
        elif self.__c == 0:
            return f"\nForma implicita dell'equazione:\n {self.a}x + {self.__b}y = 0"    
        else:   
            return f"\nForma implicita dell'equazione:\n {self._a}x + {self.b}y + {self._c} = 0 "

    def Esplicita(self):
        if self.__b == 0:
            return f"\nForma esplicita dell'equazione: \n L'equazione è impossibile"
        elif self.__a == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self._c / self._b}"
        elif self.__c == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self._a / self._b}"
        else:
            return f"\nForma esplicita dell'equazione: \n y = {-self._a / self.b}x + {-self.c / self._b}"
    
    def m(self):
        if self.__b == 0:
            return f"\nCoefficiente angolare: \n Il coefficiente angolare non è definito; la retta è parallela all'asse y"
        else:
            return f"\nCoefficiente angolare: \n m = {-self._b / self._a}"
    
    def trovaY(self, x):
        return f"\n Y: \n y = {-self._a * x / self.b + (-self.c / self._b)}"


    def punti(self, N, M, x):
        self.__N = N
        self.__M = M
    
        for self._N in range (self._M):
            tupla = (x, (-self._a * x) / self.b + (-self.c / self._b))
            x = x + 1
            self.__punti.append(tupla)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.__punti}"         


    def instersezione(self, a1 , b1 , c1):
        self.__a1 = float(a1)
        self.__b1 = float(b1)
        self.__c1 = float(c1)
        if (-self._b / self.a) == (-self.b1 / self._a1):
            if self._c == self._c1:
                return f"\nLe rette sono coincidenti \n {self.__punti}"
            else:
                return f"Null"
        elif self._c == self._c1:
            return f"\nIl putnto di incontro delle due rette è: {self.__c}y" 
        else:
            return f"\nLe rette sono incidenti e le coordinate del punto d'incidenza sono: ({((-self._c / self.b)+(self.c1 / self.b1))/((-self.b / self.a)+(self.b1 / self.a1))}, {((-self.b / self.c)+(self.b1 / self.c1))/((-self.b / self.a)+(self.b1 / self._a1))})"

    def fascio_parallelo(self):
        if self.__b == 0:
            return f"\nL'equazione del fascio parallelo alla retta data è: \nx = k"
        else:
            return f"\nL'equazione del fascio parallelo alla retta data è: \ny = {-self.__a / self.__b}x + q"

valori = retta(input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ')) 
print(valori.Implicita())
print(valori.Esplicita())
print(valori.m())
print(valori.trovaY((input('x = ')))
print(valori.punti(input('inizio intervallo = ') , input('fine intervallo = ')))
print(valori.instersezione(input('a1 = ' ), input('b1 = ' ), input('c1 = ' )))
print(valori.fascio_parallelo())