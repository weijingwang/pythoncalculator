#add
print("add _ _ _ or sub _ _ _ or mul _ _ _ or div _ _ _")
input_str = raw_input("Enter: ")#input

#print (input_str)
input_str = input_str.split(" ")
#print (input_str)

output_str = 0

if input_str[0] == "add":
	#print ("good")
	input_str = (input_str[1:])
	input_str = [int(every_number) for every_number in input_str]
	#print input_str
	for every_number in input_str:
	 	output_str += every_number
	 	print (output_str)
elif input_str[0] == "sub":
	#print ("good")
	input_str = (input_str[1:])
	input_str = [int(every_number) for every_number in input_str]
	#print input_str
	for every_number in input_str:
	 	output_str -= every_number
	 	print (output_str)
elif input_str[0] == "mul":
	output_str = 1
	#print ("good")
	input_str = (input_str[1:])
	input_str = [float(every_number) for every_number in input_str]
	#print input_str
	for every_number in input_str:
	 	output_str *= every_number
	 	print (output_str)
elif input_str[0] == "div":
	#print ("good")
	input_str = (input_str[1:])
	input_str = [float(every_number) for every_number in input_str]
	#print input_str
	output_str = input_str[0]
	input_str = input_str[1:]
	#print (input_str)
	for every_number in input_str:
	 	output_str //= every_number
	 	print ("About {}").format(output_str)
else:
	print ("add _ _ _ or sub _ _ _ or mul _ _ _ or div _ _ _")

