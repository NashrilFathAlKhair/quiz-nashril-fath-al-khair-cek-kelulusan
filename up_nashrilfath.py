nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

while True:
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")
    pilihan = input("Pilih transaksi (1/2/3): ")

    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk: "))
        stok += jumlah
        print("Stok berhasil ditambah.")

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar: "))

        if jumlah > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok -= jumlah
            print("Stok berhasil dikurangi.")

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid!")

    print(f"Stok saat ini: {stok}")

print(f"\nStok terakhir : {stok}")
print("Terima kasih!")