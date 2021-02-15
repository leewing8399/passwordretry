# 密码重试程式
	# password = 'a123456'
	# 让使用者重复输入密码
	# 最多输入3次
	# 如果正确 就印出 "登入成功"
	# 如果不正确 就印出"密码错误, 还有_次机会！"

password = '123'
i = 3 	# 剩余机会

while True:
	pwd = input('请输入密码: ')
	if pwd == password:
		print('登录成功!')
		break
	else :
		i= i-1
		print('密码错误，还有', i ,'次机会！')
		if i == 0 :
			break

