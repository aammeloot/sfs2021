import os

# class 
class Pinger(object):
    host = "127.0.0.1"
    def __init__(self, hostname):
        self.host = hostname
    def run(self):
        os.system("ping -c 10 " + self.host)


# This is an example of a menu...
def ping_option(host):
    p = Pinger(host)
    p.run()

def option2():
    pass

def option3():
    pass

def option4():
    pass


# Main menu here

option = ""

while option != "5":
    print('''Welcome to the menu.
1 - Ping a machine
2 - Port scan
3 - Crack password
4 - Analyse files
5 - Quit''')
    option = input('Please enter your choice')

    # Selection
    if option == "1":
        host = input("What host do you want to ping?")
        ping_option(host)
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "5":
        print("Bye")
    else:
        print("Choice not recognised")
