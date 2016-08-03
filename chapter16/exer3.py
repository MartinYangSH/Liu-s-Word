class Rational():
    def gcd(self,a,b):
        if a > b:
            min = b
            max = a
        else:
            min = a
            max = b    
        if max%min == 0:
            return min
        else:
            a = max%min
            b = min
            return self.gcd(a,b)

print Rational().gcd(319,377)