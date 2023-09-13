import yaml

file_name = "db.yaml"

def read_yaml(file_name):
	try:
		with open(file_name, "r") as f:
			f_inf = yaml.safe_load(f)
			return f_inf
	except:
		with open(file_name, "w") as f:
			pass

def write_key(file_name, account_key, account_info):
	with open(file_name, 'r') as f:
		reading = yaml.safe_load(f)
		# print("1 reading ", reading)

	with open(file_name, "w") as f_w:
		if reading == None:
			reading = {}

		reading[account_key] = account_info
		yaml.dump(reading, f_w)
		# print(read_yaml(file_name))
		return True

def delete_key(file_name, key):
	with open(file_name, 'r') as f:
		reading = yaml.safe_load(f)
		if reading == None:
			return False
		elif key not in reading:
			return False

	with open(file_name, "w") as f_w:
		reading.pop(key)
		yaml.dump(reading, f_w)
		return True



# print(write_yaml(file_name, "VB", "89"))
# print(write_yaml(file_name, "V67", "89"))
# print(write_yaml(file_name, "V7", "89"))
# print(delete_key(file_name, "V5B"))
# print(read_yaml(file_name))
