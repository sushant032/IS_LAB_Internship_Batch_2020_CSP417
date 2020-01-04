import matplotlib.pyplot as plt
f = open("test.txt")
lines = f.readlines()
text = ""
for i in lines:
	text+=i
text = text.strip()
chars = sorted(set(text))
chrs = {}
for i in chars:
	if i.isalpha():
		chrs[i] = text.count(i)
		# print(i,chrs[i])
plt.bar(chrs.keys(),chrs.values(),color='g')
plt.show()