package day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Day1 {
    public static void main(String[] args) {
        partOne();
        partTwo();
    }

    private static void partOne() {
        int currentFrequency = 0;

        try (Stream<String> fileStream = Files.lines(Paths.get("day1/input.txt"))) {
            currentFrequency = fileStream.mapToInt(Integer::parseInt).sum();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Resulting Frequency is " + currentFrequency);
    }

    private static void partTwo() {
        int currentFrequency = 0;

        HashMap<Integer, Boolean> pastFrequences = new HashMap<>();

        pastFrequences.put(0, true);

        List<Integer> frequencies = new ArrayList<>();

        File inputFile = new File("day1/input.txt");
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
