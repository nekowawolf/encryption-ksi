import pyperclip

def main():
    pesanSaya = 'Iaakn nudRa:oahIny ReaATs iAiTr|'
    kunciSaya = 8

    sanditeks = dekripsiPesan(kunciSaya, pesanSaya)

    print(sanditeks + '|')
    pyperclip.copy(sanditeks)

def dekripsiPesan(kunci, pesan):
    nomorKolom = -(-len(pesan) // kunci)
    nomorBaris = kunci
    numOfShadedBoxes = (nomorKolom * nomorBaris) - len(pesan)

    sanditeks = [''] * nomorKolom

    col = 0
    row = 0

    for symbol in pesan:
        sanditeks[col] += symbol
        col += 1

        if (col == nomorKolom) or (col == nomorKolom - 1 and row >= nomorBaris - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(sanditeks)

if __name__ == '__main__':
    main()
