import random,string
def sentence(length):
	result = []
	alph = "abcdefghijklmnopqrs tuvwxyz"
	for i in range(length):
		result.append(random.choice(alph))

	return ''.join(result)


def compare(generated, origin):
	num = 0.0
	for i in range(len(origin)):
		if generated[i]==origin[i]:
			num += 1

	return num / len(origin)



def repeat():
	o = "methinks it is like a weasel"
	s = sentence(len(o))
	rate = {}
	sen = {}
	for i in range(100000000):
		num = round(compare(s, o), 5)
		rate[i]= num
		sen[num] = s
		if compare ==1:
			break
	maxnum = max(rate.values())
	return sen[maxnum]

print repeat()
