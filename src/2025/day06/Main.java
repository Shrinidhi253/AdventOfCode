import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        FileParser fileParser = new FileParser();
        ArrayList<String[]> data = fileParser.getInputData();

        Day06 day06 = new Day06(data);

        long grandTotal1 = day06.day06Part1();

        System.out.printf("Grand total part 1: %d\n",  grandTotal1);
    }
}
