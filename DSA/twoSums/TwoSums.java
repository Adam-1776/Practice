import java.io.*;
import java.util.Scanner;
import java.util.*;

public class TwoSums {

	public static void readFile(List arr, String fileName) {
		File file = new File(fileName);
		try{
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			String line = "";
			while((line = br.readLine()) != null){
    			arr.add(Integer.parseInt(line));
			}
		} catch(Exception e){
			System.out.println(e);
		}
	}

    public static void main(String[] args) {
        String fileName = "D:\\Documents\\Practice\\DSA\\twoSums\\input.txt";
        List<Integer> arr = new ArrayList(100);
		readFile(arr, fileName);
		System.out.println(arr);
    }
}
