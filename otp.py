import pyotp
from time import sleep
from saving import read_yaml, write_key, delete_key

file_name = 'db.yaml'

a = read_yaml(file_name)

def add_key():
	n = True
	while n == True:
		a = read_yaml(file_name)
		add_new = input("Add new key?(y,n,d)")

		if add_new == "y":
			while True:
				print("-" * 30 + " NEW ACCOUNT " + "-" * 30)
				account_key = input("Write key:")
				if account_key == "":
					return "Account wasn`t added"

				keys_list = read_yaml(file_name)
				# print(keys_list)
				if a != None:
					if account_key in keys_list:
						print("It's already in DB")
						continue

				account_info = input("Write account info:")

				if account_info == "":
					account_info_second = input("Write account info ONE MORE TIME:")
				else:
					account_info_second = None

				if account_info_second != None and account_info_second != "":
					account_info = account_info_second
				elif account_info_second != None and account_info_second == "":
					print(f"Account {account_key} wasn`t saved!")
					continue
				
				try:
					totp = pyotp.TOTP(account_key)
					otp = totp.now()
					write_key(file_name, account_key, account_info)
					# a = (f.read()).split('\n')
					print(f'\n{account_key}:{account_info}')
					print("Success")
				except:
					print('Key doesnot correct!')
		elif add_new == "d":
			if a != None and a != {}:
				print(a)
				m = True
				while m == True:
					print("-" * 30 + f" DELETE ACCOUNT " + "-" * 30)
					a = read_yaml(file_name)
					number = 1
					for info in a:
						account_key = info
						account_information = a.get(info)
						print(f"{number}. KEY:{account_key} - {account_information}")
						number += 1
					account_key = input("Write key:")
					if account_key == "":
						print("End")
						m = False
						break
					else:
						result = delete_key(file_name, account_key)
						if result:
							print(f"Success! Key {account_key} was deleted")
						else:
							print("Failed")
			else:
				print("You have 0 accounts")
		elif add_new == "":
			n = False
			print(n, "hgdshjagdsj")
			
	


# if a == None:
# 	print("No keys")
# 	add_new = input("Add new key?(y,n)")
# 	if add_new == "y":
# 		result_adding = add_key()
# 		if result_adding != False:
# 			print(result_adding)

while True:
	a = read_yaml(file_name)
	if a == None:
		print("0 keys in database!")
		print(add_key())
	else:
		print(f"{len(a)} keys in database")
		print(add_key())
		a = read_yaml(file_name)
		if a == None:
			continue

		for i in range(60):
			print("\n"*40+"-" * 30 + " NEW CODES " + "-" * 30)
			number = 1
			for info in a:
				account_key = info
				account_information = a.get(info)
				# print(account_key)
				totp = pyotp.TOTP(account_key)
				otp = totp.now()
				print(f"OTP: {otp} KEY:{account_key} - {account_information}")
			sleep(1)
