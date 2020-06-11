import math

class ComplexNumber:

    def __init__(self,real_part=0,imaginary_part=0):
        self.part(real_part,imaginary_part)


    def part(self,real_part,imaginary_part):
        if ((type(real_part)!=int)&(type(real_part)!=float)) & ((type(imaginary_part)!=int)&(type(imaginary_part)!=float)):
            raise ValueError("Invalid value for real and imaginary part")
        elif ((type(real_part)!=int)&(type(real_part)!=float)):
            self.imaginary_part=imaginary_part
            raise ValueError("Invalid value for real part")
        elif ((type(imaginary_part)!=int)&(type(imaginary_part)!=float)):
            self.real_part=real_part
            raise ValueError("Invalid value for imaginary part")
        else:
            self.real_part=real_part
            self.imaginary_part=imaginary_part

    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)

    def __str__(self):
        if self.imaginary_part>=0:
            return f"{self.real_part}+{self.imaginary_part}i"
        elif self.imaginary_part<0:
            return f"{self.real_part}{self.imaginary_part}i"

    def __add__(self,other):
        return ComplexNumber((self.real_part+other.real_part),(self.imaginary_part+other.imaginary_part))

    def __sub__(self,other):
        return ComplexNumber((self.real_part-other.real_part),(self.imaginary_part-other.imaginary_part))

    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)

    def __truediv__(self, other):
        if other.real_part==0 and other.imaginary_part==0:
            raise  ZeroDivisionError("divison by zero")
        else:
            sr, si, sor, oi = self.real_part, self.imaginary_part, other.real_part, other.imaginary_part
            r = float(sor**2 + oi**2)
            return ComplexNumber((sr*sor+si*oi)/r, (si*sor-sr*oi)/r)

    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)

    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part

a=ComplexNumber(2,"  3" )
print(a)