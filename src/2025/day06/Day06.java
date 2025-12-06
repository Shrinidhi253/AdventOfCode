import java.util.ArrayList;

public class Day06 {
    ArrayList<String[]> data;
    int numRows;
    int numCols;

    Day06(ArrayList<String[]> data) {
        this.data = data;
        this.numRows = data.size();
        this.numCols = data.get(0).length;
    }
    long day06Part1() {
        long grandTotal = 0;

        for (int j = 0; j < numCols; j++) {
            String operation =  this.data.get(numRows - 1)[j];
            long total = Integer.parseInt(this.data.get(0)[j]);

            for (int i = 1; i < numRows - 1; i++) {
                if (operation.equals("+")) {
                    total += Long.parseLong(this.data.get(i)[j]);
                }
                else {
                    total *= Long.parseLong(this.data.get(i)[j]);
                }
            }
            grandTotal += total;
        }
        return grandTotal;
    }
}
