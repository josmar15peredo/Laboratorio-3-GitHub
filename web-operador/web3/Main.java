package web3;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
        int x;
		x = sc.nextInt();
		for (int i = 0; i < x; i++) {

		    int a, b;
		    a = sc.nextInt();
		    b = sc.nextInt();

		    if (a > b) {
		        System.out.println(">");
		    }
		    else if (a == b) {
		        System.out.println("=");
		    }
		    else {
		        System.out.println("<");
		    }
		}
	}
}
