from connection import get_connection

# ID produk yang ingin dikurangi dan jumlah pengurangan
# produk_id = 2
# jumlah_kurang = 3

def book_lend(produk_id,jumlah_kurang):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE books
    SET qty = qty - ?
    WHERE id = ? AND qty >= ?;
    """, (jumlah_kurang, produk_id, jumlah_kurang))

    if cursor.rowcount == 0:
        print("buku tidak mencukupi.")
    else:
        print("berhasil meminjam buku.")

    conn.commit()

    # Tutup koneksi
    conn.close()

# Contoh penggunaan
if __name__ == "__main__":
    book_lend(2, 3)

