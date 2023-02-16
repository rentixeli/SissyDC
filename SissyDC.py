#!/bin/env/python3
import sys

users = []
ntlms = []
together = []

try:
	if len(sys.argv) == 2:
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print ("python3 SissyDC.py <DCSync File>\nExample: python3 SissyDC.py DCsync.txt")
		else:
			try:
				with open(sys.argv[1], 'r') as fileName:
					file = fileName.readlines()
					for i in file:
						if ":::" in i:
							if "Guest:501:" not in i:
								if "DefaultAccount:503" not in i:
									if "krbtgt:502" not in i:
										users += [i.split(':')[0]]
										ntlms += [i.split(':')[3]]
										together += [i.split(':')[0] + ":" + i.split(':')[3]]
			except:
				print("You don't have this file in the directory you shitty fuck")
	else:
		print("What the fuck are you trying to do mother fucker?")
except:
	print("What the fuck are you trying to do mother fucker?")

if not users:
	pass
else:
	with open('Usernames-DC.txt', 'w') as userz:
		userz.write('\n'.join(users))

	with open('NTLMs-Only-DC.txt', 'w') as ntlmz:
			ntlmz.write('\n'.join(ntlms))

	with open('Combined-DC.txt', 'w') as togetherz:
		togetherz.write('\n'.join(together))
	print("Success brotha!\nUsernames-DC.txt - Usernames only.\nNTLMs-Only-DC.txt - NTLMs only ----> hashcat -m 1000 NTLMs-Only-DC.txt /usr/share/wordlists/rockyou.txt\nCombined-DC.txt - both Usernames and NTLMs combined.")
