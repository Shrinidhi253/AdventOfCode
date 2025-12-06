import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class FileParser {
    ArrayList<String[]> getInputData() {
        File file = new File("src/2025/day06/day06_maths_data.txt");

        try (Scanner reader = new Scanner(file)) {
            ArrayList<String[]> data = new ArrayList<>();

            while (reader.hasNextLine()) {
                String line = reader.nextLine();
                String[] values = line.trim().split("\\s+");
                data.add(values);
            }
            return data;
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found");
            return null;
        }
    }
}
