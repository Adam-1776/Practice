import java.io.*;
import java.util.Scanner;

public class TwoSums {

    public static void main(String[] args) {
        System.out.println(new File(".").getAbsoluteFile());
        String fileName = "/home/adam/Documents/Practice/DSA/twoSums/input.txt";
        File file = new File(fileName);
	System.out.println(file.canRead());
	try{
	FileReader fr = new FileReader(file);
	BufferedReader br = new BufferedReader(fr);
	String line;
	while((line = br.readLine()) != null){
    		//process the line
    		System.out.println(line);
	}
	}
	catch(Exception e){
		System.out.println("We had an exception");
	}
    }
}
