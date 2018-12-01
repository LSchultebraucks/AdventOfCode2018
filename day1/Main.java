import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
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
        int currentFrequency = 0;

        HashMap<Integer, Boolean> pastFrequences = new HashMap<>();

        pastFrequences.put(0, true);

        List<Integer> frequencies = new ArrayList<>();

        File inputFile = new File("input.txt");
        try {
            Scanner scanner = new Scanner(inputFile);

            while (scanner.hasNext()) {
                int frequency = scanner.nextInt();
                frequencies.add(frequency);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        boolean twiceFrequencyNotFound = true;

        while (twiceFrequencyNotFound) {
            for (int frequency : frequencies) {
                currentFrequency += frequency;
                boolean isPastFrequency = pastFrequences.containsKey(currentFrequency);
                if (isPastFrequency) {
                    System.out.println(currentFrequency + " appeared twice");
                    twiceFrequencyNotFound = false;
                    break;
                } else {
                    pastFrequences.put(currentFrequency, true);
                }
            }
        }


    }
}
