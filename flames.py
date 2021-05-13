def flames(str1,str2):
        names=name1+name2
        for i in names:
                if names.count(i)!=1:
                        names=names.replace(i,'')
        print('''
         _____ _
        |  ___| | __ _ _  __ ___   ___  ___
        | |_  | |/ _` | '_ ` _ \ / _ \/ __|
        |  _| | | (_| | | | | | |  __/\__ \\
        |_|   |_|\__,_|_| |_| |_|\___||___/''')
        print("\nF = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")
        number = len(names)%6
        rel = ""

        if number == 1:
                rel += "Friends"
        elif number == 2:
                rel += "Love"
        elif number == 3:
                rel += "Affection"
        elif number == 4:
                rel += "Marriage"
        elif number == 5:
                rel += 'Enemy'
        elif number == 0:
                rel += "Siblings"
        else:
                pass

        return rel
name1=input('FLAMES\nEnter name of first person:').upper()
name2=input('Enter name of second person:').upper()

print('the relationship between him and her crush is ',flames(name1,name2))
