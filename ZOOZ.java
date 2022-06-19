import java.util.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int j=0; j<t; j++) {
		    int n = sc.nextInt();

		    if (n%2 == 0) {
	                System.out.print("1");
	                for(int i=1; i<n-1; i++) {
	                    System.out.print("0");
	                }
	                System.out.print("1\n");
	            }
	            else {
	                for (int i=0; i<n/2; i++) {
	                    System.out.print("0");
	                }
	        
	                System.out.print("1");
	        
	                for (int i=(n/2)+1; i<n; i++) {
	                    System.out.print("0");
	                }
	                System.out.print("\n");
	            }
		}
	}
}