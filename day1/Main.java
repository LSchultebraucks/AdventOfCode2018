import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        partOne();
        partTwo();
    }

    private static void partOne() {
        int currentFrequency = 0;

        File inputFile = new File("input.txt");
        try {
            Scanner scanner = new Scanner(inputFile);

            while (scanner.hasNext()) {
            int frequency = scanner.nextInt();
            currentFrequency += frequency;
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Resulting Frequency is " + currentFrequency);
    }

    private static void partTwo() {

    }
}
