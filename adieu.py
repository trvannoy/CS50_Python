import inflect

p = inflect.engine()
name_list = []

def main():
    try:
        while True:
            name_list.append(input("Name: "))



    except EOFError:
        mylist = p.join(name_list)
        print(f'Adieu, adieu, to {mylist}')

        #print(name_list)

main()
