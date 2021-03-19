from os import system as oss
import sys
import configx4
oss('clear')
oss('toilet -f mono12 -F gay "X4ST"')
head = """Author : Rakib Hossain

Github : https://www.github.com/teamx4ck

Facebook : X4ck cyber army

Fb page : Team X4CK

"""
print(head)
print('[1] Start')
print('[2] Join Facebook')
print('[0] Exit')
print('')
try:
	opt = int(input('Enter your option : '))
except:
	print('Please check your input!')
	sys.exit()
if opt==1:
	oss('figlet "1"')
	oss('toilet "2"')
	oss('toilet -f mono12 "3"')
	oss('toilet -f mono12 -F gay "4"')
	try:
		opt2 = int(input('Enter option : '))
	except:
		print('Error!')
	if opt2==1:
		name1 = str(input('Enter your name : '))
		configx4.one(name1)
	elif opt2==2:
		name2 = str(input('Enter your name : '))
		configx4.two(name2)
	elif opt2==3:
		name3 = str(input('Enter your name : '))
		configx4.three(name3)
	elif opt2==4:
		name4 = str(input('Enter your name : '))
		configx4.four(name4)
	elif opt2==0:
		sys.exit()
	else:
		print('Not found!')
elif opt==2:
	oss('xdg-open https://www.facebook.com/groups/x4ckcyberarmy/?ref=share')
elif opt==0:
	print('')
	print('Goog bye....')
	sys.exit()
else:
	print('Error! Check your option..')