import random
import sys
import enkripsitransposisi
import dekripsitransposisi

def main():
    random.seed(42)

    for i in range(20):
        pesan = 'Andika' * random.randint(4, 40)
        pesan = list(pesan)
        random.shuffle(pesan)
        pesan = ''.join(pesan)

        print('Test #%s: "%s..."' % (i + 1, pesan[:50]))

        for kunci in range(1, len(pesan)):
            dienkripsi = enkripsitransposisi.enkripsiPesan(kunci, pesan)
            didekripsi = dekripsitransposisi.dekripsiPesan(kunci, dienkripsi)

            if pesan != didekripsi:
                print('Tidak cocok dengan kunci %s dan pesan %s.' % (kunci, pesan))
                print(didekripsi)
                sys.exit()

        print('Uji coba sandi Transposisi berhasil.')

if __name__ == '__main__':
    main()
