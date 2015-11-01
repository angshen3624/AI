def answer(x):
	lhs = []
	rhs = [x]
	num = encode_num(x)
	t = len(num)
	count = 0
	flag = 1
	for i in range(t):
		if num[i] == 2:
			count += 1
	while count != 0:
		ad = ad_bit(num)
		ad_t = len(ad)
		for j in range(ad_t):
			if ad[j] == 1:
				if flag == 1:
					lhs.append(ad[j]*pow(3,ad_t-j-1))
				elif flag == -1:
					rhs.append(ad[j]*pow(3,ad_t-j-1))
		flag = -flag
		ad_num = decode_num(ad)
		dif = ad_num - decode_num(num)
		dif_encode = encode_num(dif)
		count = 0
		t = len(dif_encode)
		for i in range(t):
			if dif_encode[i] == 2:
				count += 1
		num = dif_encode

	tt = len(num)
	for j in range(tt):
		if num[j] == 1:
				if flag == 1:
					lhs.append(num[j]*pow(3,tt-j-1))
				elif flag == -1:
					rhs.append(num[j]*pow(3,tt-j-1))
	return lhs,rhs
	return True
def ad_bit(num_lst):
	a = []
	t = len(num_lst)
	for i in range(t):
		if num_lst[i] == 2:
			if num_lst[i-1] == 0:
				for j in range(t):
					if j == i-1:
						a.append(1)
					elif num_lst[j] != 2:
						a.append(num_lst[j])
					else:
						a.append(0)
			elif num_lst[i-1] == 1:
				for j in range(t):					
					if num_lst[j] == 0:
						idx = j
					a.append(0)
				a[idx] = 1
				a[0:idx] = num_lst[0:idx]
			return a

def encode_num(x):
	a = []
	while x>=3:
		mod3 = x%3	
		a.append(mod3)
		x = (x-mod3)/3
	if x!=0:
		a.append(x)
	a.append(0)
	a.reverse()
	return a

def decode_num(x):
	total = 0
	t = len(x)
	for i in range(t):
		total = total + x[t-i-1]*pow(3, i)
	return total

if __name__ == '__main__':
	#print encode_num(28)
	#print encode_num(512)
	#print ad_bit(encode_num(512))
	#print answer(1024)
	#num = [0, 2, 1, 1, 2, 1, 0]
	#print ad_bit(num)
	#num1 = [0,1,1,2]
	#num2 = [1,0,1,1,2]
	#print ad_bit(num1)
	#print ad_bit(num2)
	#print answer(1024)
	print "Hello, SB ang"