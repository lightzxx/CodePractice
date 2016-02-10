import java.util.Scanner;
public class LeapYear {
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int year = in.nextInt();
		boolean isLeapYear;
		isLeapYear = (year % 4 == 0);
		isLeapYear = isLeapYear && (year % 100 != 0);
		isLeapYear = isLeapYear || (year % 400 == 0);
		System.out.println(isLeapYear);
	}
}
