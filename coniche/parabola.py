class parabola:
    
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):
            self.__a = int(p1)  
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []

        elif(tipo == "fuocoDiret"):
            self.__p1 = int(p1)
            self.__p2 = int(p2)
            self.__p3 = int(p3)
            self.__punti = []
            self.__a = 2/(4*self.__p2 - 4*self.__p3)
            self.__b = -2*self.__a * self.__p1
            self.__c = (4*self.__p2 + self.__b*self.__b - 1)/(4*self.__a)
        
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    

    def fuoco(self, asse_simmetria = "x"):
        if (asse_simmetria == "x"):
            y =-((self.__b)/((self.__a)*2))
            x = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
            return x,y

        elif (asse_simmetria == "y"):
            x =-((self.__b)/((self.__a)*2))
            y = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
            return x,y

    def direttrice(self, asse_simmetria = "x"):
        if (asse_simmetria == "x"):
            y= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            return f"y = {y}"

        elif (asse_simmetria == "y"):
            x= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
            return f"x = {x}"  

valori = parabola(input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ')) 
print("Le coordinate del fuoco sono:", valori.fuoco(input('Asse simmetria parallelo a ' ))) 
print("L'equazione della direttrice è:", valori.direttrice(input('Asse simmetria parallelo a ' )))