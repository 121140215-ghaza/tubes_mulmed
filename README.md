# Boo! - Filter Tebak Hasil Gabungan Warna
Project Mata Kuliah Sistem / Teknologi Multimedia Teknik Informatika ITERA
Dosen Pengampu : Martin Clinton Tosima Manullang, S.T., M.T.

## Anggota
1. Mohammad Hisyam Alif Setiawan (@121140131MohammadHisyamAlifSetiawan)
2. Muhammad Farhan Annaufal (@MuhammadFarhanAnnaufal)
3. Ghaza Muhammad Al Ghifari (@121140215-ghaza)

## Laporan
Laporan atau report bisa diakses secara online melalui website overleaf: https://www.overleaf.com/read/kwmgbsstjgck#60a959

## Deskripsi
"Boo!" adalah sebuah filter interaktif yang menguji kemampuan pengguna dalam menebak hasil campuran warna. Dalam filter ini, pengguna akan diberikan dua warna dasar, dan mereka harus memilih warna hasil campuran yang benar dalam waktu terbatas. Setiap pilihan memiliki dua opsi jawaban yang ditampilkan secara visual di layar. Pengguna akan memilih jawaban dengan cara menggerakkan kepala mereka ke kiri atau ke kanan, sesuai dengan pilihan yang diinginkan.

Setelah memilih jawaban, filter akan memberikan notifikasi apakah jawaban tersebut benar atau salah. Di akhir permainan, skor total yang didapatkan oleh pengguna akan ditampilkan, memberikan pengalaman yang menyenangkan dan edukatif.

## Fitur Utama
- **Tebak Hasil Gabungan Warna**: Pengguna diberikan dua warna dasar dan diminta menebak hasil campuran yang benar.
- **Pilihan Jawaban Interaktif**: Pengguna dapat memilih jawaban dengan menggerakkan kepala mereka ke kiri atau ke kanan.
- **Batas Waktu**: Setiap pertanyaan memiliki waktu terbatas untuk menebak jawaban, menambah tantangan dalam permainan.
- **Notifikasi Hasil Jawaban**: Setelah menjawab, pengguna akan diberi tahu apakah tebakan mereka benar atau salah.
- **Skor**: Skor akhir akan dihitung berdasarkan jumlah jawaban benar yang diberikan oleh pengguna, dan ditampilkan di akhir permainan.

## Teknologi yang Digunakan
- **OpenCV**: Untuk pengolahan gambar dan pengolahan warna dalam filter, termasuk deteksi wajah untuk mendeteksi gerakan kepala pengguna.
- **MediaPipe**: Untuk deteksi gerakan kepala secara real-time, memungkinkan pengguna untuk memilih jawaban dengan cara menggerakkan kepala mereka.

## Cara Kerja Filter
1. **Tampilan Warna**: Pada setiap pertanyaan, dua warna dasar akan ditampilkan di layar.
2. **Pilihan Jawaban**: Setelah warna dasar ditampilkan, pengguna diberikan dua pilihan warna hasil campuran yang muncul di layar. Pilihan ini berada di sisi kiri dan kanan layar.
3. **Interaksi Pengguna**: Pengguna memilih salah satu pilihan jawaban dengan menggerakkan kepala mereka ke kiri atau ke kanan. Deteksi gerakan kepala dilakukan oleh MediaPipe.
4. **Timer**: Filter akan mengaktifkan timer yang memberikan batas waktu beberapa detik untuk membuat keputusan. Setelah waktu habis, jawaban akan dikunci secara otomatis.
5. **Pemberitahuan Hasil**: Setelah memilih jawaban, filter akan menampilkan pemberitahuan apakah jawaban yang diberikan benar atau salah.
6. **Skor**: Filter akan mencatat jawaban yang benar dan memberi skor. Di akhir permainan, total skor yang diperoleh akan ditampilkan.

## Instruksi Instalasi
Untuk menjalankan filter Boo!- Filter Tebak Hasil Gabungan Warna, beberapa pustaka (library) yang diperlukan adalah OpenCV dan MediaPipe. Berikut adalah langkah-langkah untuk menginstal dependensi yang diperlukan:
   1. Persyaratan Sistem:
     • Python 3.7-3.10 (Recommended 3.9)
     • Sistem operasi: Windows, macOS, atau Linux
   2. Langkah Instalasi:
     • Instalasi Python: Pastikan Python versi terbaru sudah terinstal. Jika belum, silakan unduh dan instal Python dari situs resmi Python.
     • Instalasi OpenCV: Setelah Python terinstal, kita perlu menginstal pustaka OpenCV yangdigunakan untuk pengolahan gambar. Gunakan perintah berikut untuk menginstal OpenCV melalui pip:
        
          pip install opencv-python

     • Instalasi MediaPipe: MediaPipe digunakan untuk deteksi dan pelacakan wajah secara real-time. Instal pustaka ini dengan perintah:

          pip install mediapipe

     • Instalasi dependensi tambahan: Beberapa pustaka tambahan yang diperlukan untuk menjalankan aplikasi adalah time dan random, yang sudah terinstal bersama Python secara default.
   3. Verifikasi Instalasi: Untuk memverifikasi bahwa semua pustaka telah terinstal dengan benar, jalankan kode berikut di terminal atau command prompt Python:
 
          import cv2
           import mediapipe as mp
             print("OpenCV and MediaPipe installed successfully!")
 
      Jika tidak ada error, instalasi berhasil.

## Instruksi Penggunaan
1. **Aktifkan Filter**: Pilih filter "Boo!" dari daftar filter yang tersedia.
2. **Lihat Warna Dasar**: Warna dasar akan ditampilkan di layar, dan Anda akan diminta untuk menebak warna hasil campuran yang benar.
3. **Gerakkan Kepala**: Pilih warna hasil campuran dengan menggerakkan kepala Anda ke kiri atau ke kanan, sesuai dengan pilihan yang ingin dipilih.
4. **Tunggu Hasil**: Setelah waktu habis atau Anda memilih jawaban, filter akan memberi tahu apakah jawaban Anda benar atau salah.
5. **Lihat Skor**: Di akhir permainan, total skor yang diperoleh akan ditampilkan.
