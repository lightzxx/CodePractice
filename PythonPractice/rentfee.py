import sys

rent_fee = float(sys.argv[1])
rate = 4.56
weeks = 4
months = 6

print "One month fee:", rent_fee * rate * weeks, "RMB"
print
print "One month fee:", rent_fee * weeks, "AU dollars"
print
print "Half year fee:",rent_fee * rate * weeks * months, "RMB"
print
print "Half year fee:", rent_fee * weeks * months, "AU dollars"
print
print "One year fee:", rent_fee * rate * weeks * months*2, "RMB"
print
print "One year fee:", rent_fee *weeks * months*2, "AU dollars"
print