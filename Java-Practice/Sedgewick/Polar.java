/*
	Creative Exercises 1.2.26 on 
	Introduction to Programming in Java: An Interdisciplinary Approach
*/
public class Polar{
	public static void main(String[] args){
		double x = Double.parseDouble(args[0]);
		double y = Double.parseDouble(args[1]);
		double beta = Math.atan2(y, x);
		double r = y / Math.sin(beta);
		System.out.println("Angle is "+beta);
		System.out.println("Radius is "+ r);
	}
}