#Fixed XOR

#Write a function that takes two equal-length buffers and produces their XOR combination. 
def xor_hex(a,b):
	bin_a = bin(int(a, 16))[2:]
	bin_b = bin(int(b, 16))[2:]
	return hex(int(bin_a,2) ^ int(bin_b,2))

def main():
	hex_s_a = '1c0111001f010100061a024b53535009181c'
	hex_s_b = '686974207468652062756c6c277320657965'
	hex_s = xor_hex(hex_s_a,hex_s_b)
	print(hex_s)

if __name__ == '__main__':
	main()

