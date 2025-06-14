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

def list_book():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, qty FROM books")
    data = cursor.fetchall()
    print("\n📦 Available books")
    for id, title, qty in data:
        print(f"ID: {id} | Judul: {title} | Stok: {qty}")
    conn.close()

# Contoh penggunaan
if __name__ == "__main__":
    list_book()
    try:
        produk_id = int(input("\nMasukkan ID produk yang ingin dipinjam: "))
        jumlah_kurang = 1

        book_lend(produk_id, jumlah_kurang)
    except ValueError:
        print("❌ Input tidak valid. Harus berupa angka.")

