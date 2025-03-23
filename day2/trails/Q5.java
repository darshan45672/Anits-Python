import java.util.Scanner;

public class Q5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Percentage: ");
        int num = sc.nextInt();

        if(num>=90 && num<=100) {
            System.out.println("Grade A");
        } else if(num>=80 && num<90) {
            System.out.println("Grade B");
        } else if(num>=70 && num<80) {
            System.out.println("Grade C");
        } else if(num>=60 && num<70) {
            System.out.println("Grade D");
        } else if(num>=50 && num<60) {
            System.out.println("Grade F");
        }else {
            System.out.println("Fail");
        }
    }
}
