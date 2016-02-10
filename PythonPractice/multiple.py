def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm % oldn
	return n

class Fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def show(self):
		print(self.num, "/", self.den)

	def __add__(self, other_fraction):
		newnum = self.num * other_fraction.den + \
					self.den * other_fraction.num
		newden = self.den * other_fraction.den
		common = gcd(newnum, newden)
		return Fraction(newnum//common, newden//common)

	def __mul__(self, other_fraction):
		newnum = self.num * other_fraction.num
		newden = self.den * other_fraction.den
		common = gcd(abs(newnum), newden)
		return Fraction(newnum//common, newden//common)

	def __sub__(self, other):
		newnum = self.num * other.den - self.den * other.num
		newden = self.den * other.den
		common = gcd(newnum, newden)
		if newnum > 0:
			return Fraction(abs(newnum) // common, newden//common)
		elif newnum<0:	
			return "-"+str(Fraction(abs(newnum) // common, newden//common))
		elif newnum == 0:
			return 0

	def __div__(self, other):
		newnum = self.num * other.den
		newden = self.den * other.num
		common = gcd(newnum, newden)
		return Fraction(newnum//common, newden//common)


	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __gt__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum > secondnum
	def __lt__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum < secondnum

x = Fraction(1,2)
y = Fraction(2,3)
print(x.__add__(y))
print(x * y)
print(x - y)
print(x / y)
print(x == y)
print(x > y)
print(x < y)



