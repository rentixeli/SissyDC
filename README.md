### What the fudge?
```
Well SissyDC will take a DCSync file and will divide it to 3 files.
Usernames-DC.txt - Usernames only.
NTLMs-Only-DC.txt - NTLMs only ----> hashcat -m 1000 NTLMs-Only-DC.txt /usr/share/wordlists/rockyou.txt
Combined-DC.txt - A combination of Usernames + their NTLM hash.
```

### K how to run it?
```
python3 SissyDC.py <DCsync File>
Example: python3 SissyDC.py DCSync.txt
```

### Flow
# 1) DCSync
```
Save the DCSync file as txt file.
```
![alt text](https://raw.githubusercontent.com/rentixeli/SissyDC/main/Images/dcsync.png)
# 2) Run
```
python3 SissyDC.py DCSync.txt
```
![alt text](https://raw.githubusercontent.com/rentixeli/SissyDC/main/Images/run.png)
# 3) Enjoy
![alt text](https://raw.githubusercontent.com/rentixeli/SissyDC/main/Images/done.png)
