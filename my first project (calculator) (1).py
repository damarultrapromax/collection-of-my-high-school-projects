print("kalkulator sedrhana no ai ai an rilll 100% no fek fek")
#biar bisa ngasi angka sama oprasi hitung nya
angka1 = int(input("Masukan angka pertama: "))
oprasi = input("pilih operasi + - * / ** : ")
angka2 = int(input("masukan angka ke dua: "))
#kalau pilih oprasi + nanti python bakalan pangil ini
if oprasi == "+":
    hasil = angka1 + angka2
    print(hasil)
  #kalau pilih oprasi - nanti python bakalan pangil ini  
elif oprasi == "-":
    hasil = angka1 - angka2
    print(hasil)
    #kalau pilih oprasi * nanti python bakalan pangil ini
elif oprasi == "*":
    hasil = angka1 * angka2
    print(hasil)
    #kalau pilih oprasi / nanti python bakalan pangil ini
elif oprasi == "/":
    # biar engga eror waktu di kasi 0
    if angka2 == 0:
        print("Masa dibagi nol jir ya engga bisa lah kocak")
    else:
        hasil = angka1 / angka2
        print(hasil)
        #kalau pilih oprasi ** nanti python bakalan pangil ini
elif oprasi == "**":
    hasil = angka1 ** angka2
    print(hasil)
else:
    print("lu ngetik apaan jir")

    #debug nya pake ai ya otak dah mentok nih (emot batu)
    #85% ai 15% sendiri

    