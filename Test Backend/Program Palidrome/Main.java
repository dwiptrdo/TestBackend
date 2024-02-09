import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); // membuat scanner untuk mendapatkan input dari pengguna

        System.out.print("Masukan Kata: "); // meminta pengguna memasukan kata
        String text = scanner.nextLine(); // membaca kata yang dimasukan oleh pengguna

        String reverse = ""; // variabel untuk menyimpan kata yang sudah dibalik

        // membalikan kata yang dimasukan pengguna
        for(int i=text.length()-1; i>=0; i--){
            char c = text.charAt(i);
            reverse += String.valueOf(c);
        }

        // memeriksa kata adalah palindrome atau bukan
        if (text.toLowerCase().equals(reverse.toLowerCase())){ // membandingkan kata asli dengan kata yang sudah dibalik, tanpa memperhatikan huruf besar kecil
            System.out.println("Kata" + " " + text + " " + "adalah palindrome");
        }
        else{
            System.out.println("Kata " + text + " bukan palindrome");
        }

        scanner.close(); // menutup scanner
    }
}
