import math

class Complex:
    def __init__(self, realPart, imagPart):
        self.realPart = realPart
        self.imagPart = imagPart            

    def show(self):
        if self.imagPart >=0:
            print ('%.2f+%.2fi'%(self.realPart, self.imagPart))
        elif self.imagPart <0:
            print ('%.2f%.2fi'%(self.realPart, self.imagPart))

    def add(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1+r2
        resultI = i1+i2
        result = Complex(resultR, resultI)
        return result

    def sub(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1-r2
        resultI = i1-i2
        result = Complex(resultR, resultI)
        return result   

    def mul(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = (r1*r2-i1*i2)
        resultI = (r1*i2+r2*i1)
        result = Complex(resultR, resultI)
        return result

    def div(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = float(float(r1*r2+i1*i2)/float(r2*r2+i2*i2))
        resultI = float(float(r2*i1-r1*i2)/float(r2*r2+i2*i2))
        result = Complex(resultR, resultI)
        return result

    def mod(self):
        print ('%.2f'%math.sqrt(self.realPart**2 + self.imagPart**2))

print ("Input two complex numbers: ")
c1r,c1i = map(float, input().split())
c2r,c2i = map(float, input().split())

c1 = Complex(c1r,c1i)
c2 = Complex(c2r,c2i)

result = c1.add(c2)
result.show()
result = c1.sub(c2)
result.show()
result = c1.mul(c2)
result.show()
result = c1.div(c2)
result.show()
c1.mod()
c2.mod()
