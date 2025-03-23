import java.util.Scanner;

public class Q4 {
 public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the side1: ");
    int side1 = sc.nextInt();
    System.out.println("Enter the side2: ");
    int side2 = sc.nextInt();
    System.out.println("Enter the side3: ");
    int side3 = sc.nextInt();

    if (side1 != 0 && side2 !=0 && side3 !=0) {
        if (side1+side2>side3 && side2+side3>side1 && side1+side3>side2) {
            if (side1 == side2 && side2 == side3 && side1 == side3) {
                System.out.println("Equilateral triangle");
            } else if (side1 == side2 || side2 == side3 || side1 == side3) {
                System.out.println("Isosceles triangle");
            } else {
                System.out.println("Scalene triangle");
            }
        } else {
            System.out.println("not a triangle");
        }
    }
    sc.close();
 }   
}
