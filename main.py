def no_key(msg):
	for x in range(1,27):
		decr_msg = ""
		for letter in msg.lower():
			encoded = chr(ord(letter) - x)
			decr_msg += encoded if ord(encoded) >= ord("a") else chr(26 + ord(encoded))
		print("decrypted msg with key value {}-->".format(x) + decr_msg)
		
def yes_key(msg, key):
	key = int(key) % 26
	decr_msg = ""
	for letter in msg.lower():
		encoded = chr(ord(letter) - key)
		decr_msg += encoded if ord(encoded) >= ord("a") else chr(26 + ord(encoded))
		
	print("decrypted msg-->" + decr_msg)



def encrypt():
	msg = input("enter the msg you wish to encrypt-->")
	key = input("enter the key-->")
	key = int(key) % 26
	print("The effective key value-->", key)
	encr_msg = ""
	for letter in msg.lower():
		encoded = chr(ord(letter) + key)
		encr_msg += encoded if ord(encoded) <= ord("z") else chr(ord(encoded) - 26) #(ord("a") - ord("z")) = -25
	print("encrypted msg -->" + encr_msg)


def decrypt():
	msg = input("enter the encrypted msg-->")
	key = input("do you have a key? if yes then enter else type 'no'-->")
	
	if key.lower() != "no":
		yes_key(msg, key)

	else:
		no_key(msg)
			


if __name__ == '__main__':
	cyp = input("Do you want to encrypt or decrypt(e/d)?")[0]
	if cyp.lower() == "e":
		encrypt()

	elif cyp.lower() == "d":
		decrypt()