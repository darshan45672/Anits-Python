import java.util.Scanner;

public class Q3{
    public static void main(String[] args) {
        System.out.println("Enter the number");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        if (n==0){
            System.out.println("The number is zero");
        }else if(n>0){
            if (n%2==0){
                System.out.println("The number is positive even");
            }
            else{
                System.out.println("The number is positive odd");
            }
        }
        else{
            if (n%2==0){
                System.out.println("The number is negative even");
            }
            else{
                System.out.println("The number is negative odd");
            }
        }

        sc.close();
    }
}