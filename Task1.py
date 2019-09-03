if __name__ == '__main__':

    file = open('ucheniki.txt')
    ocenka_count = 0
    ocenka_sum = 0

    print(' Вывод учеников с оценками ниже 7:')

    while True:
        line = file.readline()
        if not line:
            break

        splitted = line.split('-')
        ocenka_count += 1
        ocenka_sum += int(splitted[1])

        if int(splitted[1]) < 7:
            print(line)
    file.close()

    print('Средний бал класса - ' + str(ocenka_sum/ocenka_count))
    print('Общая статистика: ')

    file = open('ucheniki.txt')

    while True:
        line = file.readline()
        if not line:
            break
            
        print(line)

    file.close()
