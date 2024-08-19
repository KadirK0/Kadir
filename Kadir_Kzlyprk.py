import random


def tas_kagit_makas_kadir_kizilyaprak():
    aksiyonlar = ['rock', 'paper', 'scissors', 'exit']
    skor_bilgisayar = 0
    skor_oyuncu = 0

    for tur in range(3):
        bilgisayar_secimleri = random.choice(aksiyonlar)

        while True:
            kullanici_secimleri = input('Choose your action or exit (rock, paper, scissors, exit): ')
            if kullanici_secimleri in aksiyonlar:
                break
            else:
                print('You chose an invalid option! Please choose rock, paper, scissors, or exit.')

        if kullanici_secimleri == 'exit':
            if tur == 0:
                print('Why did you exit right away? You could have played!')
            print('Exiting the game.')
            return False

        print('Computer chose: ' + bilgisayar_secimleri)
        print('You chose: ' + kullanici_secimleri)

        if kullanici_secimleri == bilgisayar_secimleri:
            print('It is a tie!')
        elif (kullanici_secimleri == 'rock' and bilgisayar_secimleri == 'scissors') or \
                (kullanici_secimleri == 'paper' and bilgisayar_secimleri == 'rock') or \
                (kullanici_secimleri == 'scissors' and bilgisayar_secimleri == 'paper'):
            print('You Win!!!')
            skor_oyuncu += 1
        else:
            print('You Lose!')
            skor_bilgisayar += 1

    print(f'Final Score - Player: {skor_oyuncu}, Computer: {skor_bilgisayar}')

    if skor_oyuncu > skor_bilgisayar:
        print('You are the overall winner!')
    elif skor_bilgisayar > skor_oyuncu:
        print('The computer is the overall winner!')
    else:
        print('The game is a tie!')

    return True


while True:
    devam = tas_kagit_makas_kadir_kizilyaprak()
    if not devam:
        break


    cevap = input('Wanna play again? (yes, no): ')


    if cevap.lower() == 'no':
        break


    elif cevap.lower() == 'yes':
        bilgisayar_secimleri = random.choice(['yes', 'no'])
        print(f'Computer chose: {bilgisayar_secimleri}')
        if bilgisayar_secimleri == 'no':
            print('Computer does not want to play again.')
            break
        elif bilgisayar_secimleri == 'yes':
            print('Starting the game again...')
            continue


    else:
        print('Invalid input. Please enter yes or no.')


