#!/usr/bin/python3

### By Gordibus.

### Rode map, for my mind, here is the system command surface
### https://docs.python.org/3/library/os.html
import os

#from gevent.subprocess import getoutput
#getoutput("ls -al")
print("Your environnement is:\n",os.name)

print("And then this is details of your system:\n",os.uname())

print("This is the different variable of environement:\n",list(os.environ.keys()))

print("Language use on my computer:\n",os.getenv('LANGUAGE'))

print("The current process id:\n",os.getpid())

print("The parent’s process id:\n",os.getppid())

print("The real user id:\n",os.getuid())

print("The effective user id:\n",os.geteuid())

#interressant
print("The user name:\n",os.getlogin())

print("The list of supplemental group ids associated with the current process:\n",os.getgroups())

print("The current process group:\n",os.getpgrp)

print("Return a tuple (ruid, euid, suid):\n",os.getresuid())

print("Return a tuple (rgid, egid, sgid)\n",os.getresgid())

print("Return the filename corresponding to the controlling terminal of the process:\n",os.ctermid())

print("This one is a littre long, it's a mapping ojbect keys and values of process envrionment:\n", os.environ)

print("See where I execute this program:\n", os.getcwd())