from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
s = socket(AF_INET, SOCK_STREAM)

saddr = ('127.0.0.1', 8888)
s.connect(saddr)

data = s.recv(1024)
print(data.decode())

message = 'HELLO vijayakumar.san\n'
s.send(message.encode())
#print(message)
#data = s.recv(1024)
#print(data.decode())
Answer = 'ANSWER '

while True:
	expression = s.recv(4096)
	decodedexp = expression.decode()
	print(decodedexp)
	separated = decodedexp.split()
	if separated[0] != 'MATH':
		print(separated)
		break 
	elif separated[0] == 'MATH':
		convert1 = int(separated[1])
		convert2 = int(separated[3])
		if separated[2] == '+':
			add = convert1 + convert2
			add2 = str(add)
			add3= Answer + add2 + '\n'
			s.send(add3.encode())
			print(add3)
			continue
		elif separated[2] == '-':
			sub = convert1 - convert2
			sub2 = str(sub)
			sub3 = Answer + sub2 + '\n'
			s.send(sub3.encode())
			print(sub3)
			continue
		elif separated[2] == '*':
			mul = convert1 * convert2
			mul2 = str(mul)
			mul3 = Answer + mul2 + '\n'
			s.send(mul3.encode())
			print(mul3)
			continue
		elif separated[2] == '/':
			div = convert1 / convert2
			div1 = round(div,2)
			div1 = int(div1)
			div2 = str(div1)
			div4 = Answer + div2 + '\n'
			s.send(div4.encode())
			print(div4)
			continue

s.close()

