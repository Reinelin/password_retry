password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('please enter password:')
	if pwd == 'a123456':
		print('succesful login')
		break
	else:		
		print('wrong password')
		if i > 0: 
			print( i ,'more chance')
		else:
			print('no more chance')
