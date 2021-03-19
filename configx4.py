from os import system as oss
main3 = """
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	
	}
fi

PS1='x4ck@local$ '"""
def one(name):
	nam1='figlet '+name
	oss('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
	onf = open('/data/data/com.termux/files/usr/etc/bash.bashrc','w')
	onf.write('clear')
	onf.write('\n')
	onf.write(nam1)
	onf.write('\n')
	onf.write('echo Tool by team X4ck')
	onf.write('\n')
	onf.write(main3)
def tow(name2):
	nam2='toilet '+name2
	oss('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
	onf = open('/data/data/com.termux/files/usr/etc/bash.bashrc','w')
	onf.write('clear')
	onf.write('\n')
	onf.write(nam2)
	onf.write('\n')
	onf.write('echo "Tool by team X4ck"')
	onf.write('\n')
	onf.write(main3)
def three(name3):
	nam3='toilet -f mono12 '+name3
	oss('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
	onf = open('/data/data/com.termux/files/usr/etc/bash.bashrc','w')
	onf.write('clear')
	onf.write('\n')
	onf.write(nam3)
	onf.write('\n')
	onf.write('echo "Tool by team X4ck"')
	onf.write('\n')
	onf.write(main3)
def four(name4):
	nam4='toilet -f mono12 -F gay '+name4
	oss('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
	onf = open('/data/data/com.termux/files/usr/etc/bash.bashrc','w')
	onf.write('clear')
	onf.write('\n')
	onf.write(nam4)
	onf.write('\n')
	onf.write('echo "Tool by team X4ck"')
	onf.write('\n')
	onf.write(main3)
