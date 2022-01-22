import java.io.*;
import java.util.Scanner;
import java.util.*;

public class TwoSums {

    public static void main(String[] args) {
        String fileName = "/home/adam/Documents/Practice/DSA/twoSums/input.txt";
        File file = new File(fileName);
        int temp;
        List<Integer> arr = new ArrayList<Integer>();
		try{
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String line;
			while((line = br.readLine()) != null){
    			arr.add(Integer.parseInt(line));
			}
		} catch(Exception e){
			System.out.println("We had an exception");
		}
		
		System.out.println(arr);
    }
}
