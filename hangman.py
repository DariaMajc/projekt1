list_of_words2 = ['giraffe', 'zebra', 'tiger',
                 'toucan', 'monkey', 'hippo',
                 'rhino', 'kangaroo', 'lion']

list_of_words = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 9]

#lista dla użytkownika

print('*****************')
print(list_of_words[0], ' | ', list_of_words[1], ' | ', list_of_words[2])
print('*****************')
print(list_of_words[3], ' | ', list_of_words[4], ' | ', list_of_words[5])
print('*****************')
print(list_of_words[6], ' | ', list_of_words[7], ' | ', list_of_words[8])
print('*****************')

number = int(input('Pod każdym numerem kryje się egzotyczne zwierze. Wybierz jeden z numerów: '))
if (number) <= 8 and (number > 0):
    user_number = number



if user_number == list_of_words[user_number - 1]:
    if user_number == 1:
        print('Twoje słowo ma 7 liter.')
    elif user_number == 2:
        print('Twoje słowo ma 5 liter.')
    elif user_number == 3:
         print('Twoje słowo ma 5 liter.')
    elif user_number == 4:
        print('Twoje słowo ma 6 liter.')
    elif user_number == 5:
        print('Twoje słowo ma 6 liter.')
    elif user_number == 6:
        print('Twoje słowo ma 5 liter.')
    elif user_number == 7:
        print('Twoje słowo ma 5 liter.')
    elif user_number == 8:
        print('Twoje słowo ma 8 liter.')
    elif user_number == 9:
        print('Twoje słowo ma 4 litery.')



user_word = list_of_words2[user_number - 1]
uwlist = list(user_word)
trials = 10

for i in range(len(user_word)):
    uwlist[i] = '_'

while trials > 0:
    print('Masz', trials, 'szans.')
    print(' '.join(uwlist))
    print('Podaj literę: ')
    user_char = input()


    if user_char in user_word:
        for i in range(len(user_word)):
            if user_word[i] == user_char:
                uwlist[i] = user_char
            elif user_word == user_char:
                uwlist = user_char
                print('Odgadłeś całe słowo')
                break


        if ''.join(uwlist) == user_word:
            print(' '.join(uwlist))
            print('Gratulacje, wygrałeś!')
            break
    else:
        trials = trials - 1
        if trials == 0:
            print('Masz', trials, 'szans.')
            print('Przegrałeś :(')









