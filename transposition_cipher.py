import pyperclip

def main():
    pesanSaya = 'Indonesia Raya Tanah Airku:IRTA'
    kunciSaya = 8
    sanditeks = enkripsiPesan(kunciSaya, pesanSaya)
    print(sanditeks + '|')
    pyperclip.copy(sanditeks)

def enkripsiPesan(kunci, pesan):
    kolom = [''] * kunci
    for col in range(kunci):
        pointer = col
        while pointer < len(pesan):
            kolom[col] += pesan[pointer]
            pointer += kunci
    return ''.join(kolom)

if __name__ == '__main__':
    main()
