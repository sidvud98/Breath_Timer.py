import time
t=0
s=1
m=0
while 1==1:
	t+=1
	if t%8==0:
		print(0)
	else:
		print(8-(t%8) )
	time.sleep(1)
	if t%8==0:
		if s==1:
			print("Inhale")
		if s==2:
			print("Hold")
		if s==3:
			print("Exhale")
		if s==4:
			print("Hold")
			s = 0
		s+=1
	if t%180 ==0 :
		m+=3
		print("##################### ",m,"  minutes finished! #####################")
		
