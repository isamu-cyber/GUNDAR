#include <stdio.h>
#include <ctype.h> // Untuk fungsi toupper

int main() {
    // Mendeklarasikan string s2
    char s2[] = "jill"; // Menggunakan array karakter untuk menyimpan string

    // Mengubah huruf kedua menjadi kapital
    s2[1] = toupper(s2[1]); // Mengubah karakter kedua menjadi huruf kapital
    s2[3] = toupper(s2[3]); // Mengubah karakter keempat menjadi huruf kapital

    // Mencetak string s2
    printf("%s\n", s2);  // Output yang diharapkan: jiLl

    return 0;
}
