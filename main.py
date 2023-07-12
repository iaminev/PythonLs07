def is_lyrics(lyrics):
    vowel_letters = 'ауоыиэяюёе'
    lyrics_list = lyrics.split()
    numbers_list = list()

    for w in lyrics_list:
        numbers_list.append(len([pos for pos, char in enumerate(w) if char in vowel_letters]))

    num_letters = numbers_list[0]
    l = list(filter(lambda x: x != num_letters, numbers_list))
    if len(l) == 0:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'
def task34():
    print("Задача 34.")
    #lyrics = input("Введите кричалку: ")
    lyrics_1 = 'пара-ра-рам рым-пом-папем па-рю-пу-дэ'
    lyrics_2 = 'пара ра рам рам пам папам па ра па да'
    lyrics_3 = 'пара-ра рам рам-пам-папам па ра па-да'

    print(f'{lyrics_1}: {is_lyrics(lyrics_1)}')
    print(f'{lyrics_2}: {is_lyrics(lyrics_2)}')
    print(f'{lyrics_3}: {is_lyrics(lyrics_3)}')

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range (1, num_rows+1):
        for j in range (1, num_columns+1):
            print("{0:5d}".format(operation(i,j)), end = '')
        print(end='\n')
def task36():
    print("Задача 36.")
    print_operation_table(lambda x, y: x * y,12,12)

if __name__ == '__main__':
    task34()
    task36()
