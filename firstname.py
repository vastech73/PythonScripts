import sys
def print_fule_name(a, b):
#fname = str(input("First Name:"))
#sname = str(input("Second Name:"))
    if len(a) > 10 and len(b) > 10:
        print("Fname & Sname should be less than 10 letters:")
        sys.exit()
    print("Hello "+a,b+"!"+ " You just delved into Python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_fule_name(first_name, last_name)

