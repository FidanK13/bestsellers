
def interface():
    f = open('bestsellers.txt', 'r')
    def my_list(f):
        my_list = []
        for i in f:
            my_list.append(i.strip().split('\t'))
        return my_list

    s = my_list(f)
    while True:
        print("""
        1: Look up year range
        2: Look up month/year
        3: Search for author
        4: Search for title
        Q: Quit
        """)
        ui=input()
        if ui==str(1):
            ilk=int(input('Enter beginning year: '))
            son=int(input('Enter ending year: '))
            def iller(ilk, son, s):
                siyahi = []
                for i in s:
                    if ilk <= int(i[3].strip()[-4:]) <= son:
                        siyahi.append(i)
                return siyahi
            print(iller(ilk,son,s))
        elif ui==str(2):
            ay=int(input('Enter month(as a number, 1 - 12): '))
            il=int(input('Enter year: '))
            def ayil(ay, il, s):
                siyahi = []
                for i in s:
                    if int(i[3].strip()[-4:]) == il and int(i[3].strip().split('/')[0]) == ay:
                        siyahi.append(i)
                return siyahi
            print(ayil(ay, il, s))
        elif ui==str(3):
            yazichi=input("Enter an author's name (or part of a name): ")

            def yazici(yazichi, s):
                siyahi = []
                for i in s:
                    if yazichi.lower() in i[1].lower():
                        siyahi.append(i)
                return siyahi
            print(yazici(yazichi,s))

        elif ui==str(4):
            hisse=input('Enter a title( or part of a title): ')

            def kitab(hisse, s):
                siyahi = []
                for i in s:
                    if hisse.lower() in i[0].lower():
                        siyahi.append(i)
                return siyahi
            print(kitab(hisse, s))
        elif ui in ('Q','q'):
            break
        else:
            print('duzgun secim daxil edin')
            continue

interface()
