# Boo! - Filter Tebak Hasil Gabungan Warna

## Anggota
1. Mohammad Hisyam Alif Setiawan
2. Muhammad Farhan Annaufal
3. Ghaza Muhammad Al Ghifari

## Deskripsi
"Boo!" adalah sebuah filter interaktif yang menguji kemampuan pengguna dalam menebak hasil campuran warna. Dalam filter ini, pengguna akan diberikan dua warna dasar, dan mereka harus memilih warna hasil campuran yang benar dalam waktu terbatas. Setiap pilihan memiliki dua opsi jawaban yang ditampilkan secara visual di layar. Pengguna akan memilih jawaban dengan cara menggerakkan kepala mereka ke kiri atau ke kanan, sesuai dengan pilihan yang diinginkan.

Setelah memilih jawaban, filter akan memberikan notifikasi apakah jawaban tersebut benar atau salah. Di akhir permainan, skor total yang didapatkan oleh pengguna akan ditampilkan, memberikan pengalaman yang menyenangkan dan edukatif.

## Fitur Utama
- **Tebak Hasil Gabungan Warna**: Pengguna diberikan dua warna dasar dan diminta menebak hasil campuran yang benar.
- **Pilihan Jawaban Interaktif**: Pengguna dapat memilih jawaban dengan menggerakkan kepala mereka ke kiri atau ke kanan.
- **Batas Waktu**: Setiap pertanyaan memiliki waktu terbatas untuk menebak jawaban, menambah tantangan dalam permainan.
- **Notifikasi Hasil Jawaban**: Setelah menjawab, pengguna akan diberi tahu apakah tebakan mereka benar atau salah.
- **Skor**: Skor akhir akan dihitung berdasarkan jumlah jawaban benar yang diberikan oleh pengguna, dan ditampilkan di akhir permainan.
- **Visualisasi Warna**: Setiap warna yang ditampilkan memiliki efek visual yang menarik untuk meningkatkan pengalaman pengguna.

## Teknologi yang Digunakan
- **OpenCV**: Untuk pengolahan gambar dan pengolahan warna dalam filter, termasuk deteksi wajah untuk mendeteksi gerakan kepala pengguna.
- **MediaPipe**: Untuk deteksi gerakan kepala secara real-time, memungkinkan pengguna untuk memilih jawaban dengan cara menggerakkan kepala mereka.

## Cara Kerja Filter
1. **Tampilan Warna**: Pada setiap pertanyaan, dua warna dasar akan ditampilkan di layar. Warna-warna ini dapat berupa warna primer (merah, biru, kuning) atau campuran dari warna-warna tersebut.
2. **Pilihan Jawaban**: Setelah warna dasar ditampilkan, pengguna diberikan dua pilihan warna hasil campuran yang muncul di layar. Pilihan ini berada di sisi kiri dan kanan layar.
3. **Interaksi Pengguna**: Pengguna memilih salah satu pilihan jawaban dengan menggerakkan kepala mereka ke kiri atau ke kanan. Deteksi gerakan kepala dilakukan oleh MediaPipe.
4. **Timer**: Filter akan mengaktifkan timer yang memberikan batas waktu beberapa detik untuk membuat keputusan. Setelah waktu habis, jawaban akan dikunci secara otomatis.
5. **Pemberitahuan Hasil**: Setelah memilih jawaban, filter akan menampilkan pemberitahuan apakah jawaban yang diberikan benar atau salah.
6. **Skor**: Filter akan mencatat jawaban yang benar dan memberi skor. Di akhir permainan, total skor yang diperoleh akan ditampilkan.

## Instruksi Penggunaan
1. **Aktifkan Filter**: Pilih filter "Boo!" dari daftar filter yang tersedia.
2. **Lihat Warna Dasar**: Warna dasar akan ditampilkan di layar, dan Anda akan diminta untuk menebak warna hasil campuran yang benar.
3. **Gerakkan Kepala**: Pilih warna hasil campuran dengan menggerakkan kepala Anda ke kiri atau ke kanan, sesuai dengan pilihan yang ingin dipilih.
4. **Tunggu Hasil**: Setelah waktu habis atau Anda memilih jawaban, filter akan memberi tahu apakah jawaban Anda benar atau salah.
5. **Lihat Skor**: Di akhir permainan, total skor yang diperoleh akan ditampilkan.