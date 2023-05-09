# KedaiKopiDiskon
Deskripsi
Kode ini adalah implementasi dari program kopi sederhana yang menggunakan konsep OOP. Program ini terdiri dari tiga kelas utama, yaitu Menu, Diskon, dan CoffeeShop. Kelas Menu digunakan untuk merepresentasikan menu minuman kopi, sedangkan kelas Diskon digunakan untuk menghitung diskon berdasarkan jumlah pesanan. Kelas CoffeeShop digunakan untuk menghitung total harga pesanan pelanggan dengan memanfaatkan kelas Menu dan Diskon.

Kelas
Menu
Kelas ini merepresentasikan menu minuman kopi dengan atribut name dan price. Metode get_name() digunakan untuk mengambil nama menu, sedangkan metode get_price() digunakan untuk mengambil harga menu.

Diskon
Kelas ini digunakan untuk menghitung diskon berdasarkan jumlah pesanan. Kelas ini memiliki atribut diskon_rate yang merupakan kamus yang menyimpan tingkat diskon berdasarkan jumlah pesanan. Metode get_diskon_rate(quantity) digunakan untuk mengambil tingkat diskon berdasarkan jumlah pesanan yang diberikan.

CoffeeShop
Kelas ini digunakan untuk menghitung total harga pesanan pelanggan dengan memanfaatkan kelas Menu dan Diskon. Kelas ini memiliki atribut menu yang merupakan kamus yang menyimpan daftar menu minuman kopi yang tersedia. Kelas ini juga memiliki atribut ppn_rate yang digunakan untuk menghitung PPN. Metode calculate_total_price(choice, quantity) digunakan untuk menghitung total harga pesanan berdasarkan abjad menu dan jumlah pesanan yang diberikan.

Customer
Kelas ini digunakan untuk memesan minuman kopi dari CoffeeShop. Kelas ini memiliki atribut coffee_shop yang merepresentasikan CoffeeShop yang digunakan. Metode order(choice, quantity) digunakan untuk memesan minuman kopi berdasarkan abjad menu dan jumlah pesanan yang diberikan.
