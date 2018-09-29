from binascii import unhexlify
import base64
#given a number less than 256, 
#prints all the bit representations for that number. Try to use 8-bits.
def show_bits(num):
	print('decimal:', num)
	print('binary:', bin(num))
	print('hex:', hex(num))
	print('character:',chr(num))

def make_bin(num):
	if (num < 0):
		return -1
	else:
		num_b = ''
		while (num > 0):
			if (num % 2 == 0):
				num_b += '0'
				num /= 2
			else:
				num_b += '1'
				num = (num - 1) / 2
	return num_b[::-1]

def main():
	#Challenge1: convert hex to base64
	#input string
	hex_s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	hex_decoded_s  = unhexlify(hex_s)
	print(hex_decoded_s)

	bas64_str = base64.b64encode(hex_decoded_s)
	print(bas64_str)

	#output
	#SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
if __name__ == '__main__':
	main()