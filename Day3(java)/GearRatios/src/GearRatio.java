import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.*;

public class GearRatio {
    public static void main(String[] args) throws FileNotFoundException {
        // declarations
        List<String> inputTable = new ArrayList<>();
        List<Number> numberList = new ArrayList<>();
        List<Gear> gearList = new ArrayList<>();
        File myObj = new File("Day3(java)/input.txt");
        Pattern numberPattern = Pattern.compile("(\\d+)");
        Pattern starPattern = Pattern.compile("\\*");
        int gearRatioSum = 0;

        // create list of Strings
        inputTable = initInput(myObj);

        int i = 0;
        for (String line : inputTable) {
            Matcher matcher = numberPattern.matcher(line);
            // iterate over matches and create list of Numbers
            while (matcher.find()) {

                List<Integer> temp = new ArrayList<>();
                for (int idx = matcher.start(); idx < matcher.end(); idx++) {
                    temp.add(idx);
                }
                numberList.add(new Number(Integer.parseInt(matcher.group()), i, temp));
            }
            // iterate over matches and create list of Gears
            matcher = starPattern.matcher(line);
            while (matcher.find()) {
                gearList.add(new Gear(matcher.start(), i));
            }
            i++;
        }
        for (Gear g : gearList) {
            for (Number n : numberList) {
                // check up
                if (g.line > 0) {
                    if (n.line == g.line - 1 && (n.indexes.contains(g.index - 1) || n.indexes.contains(g.index)
                            || n.indexes.contains(g.index + 1))) {
                        g.numbers.add(n.value);
                    }
                }
                // check down
                if (g.line < inputTable.size() - 1) {
                    if (n.line == g.line + 1 && (n.indexes.contains(g.index - 1) || n.indexes.contains(g.index)
                            || n.indexes.contains(g.index + 1))) {
                        g.numbers.add(n.value);
                    }
                }
                // check left
                if (g.index > 0) {
                    if (n.line == g.line && n.indexes.contains(g.index - 1)) {
                        g.numbers.add(n.value);
                    }
                }
                // check right
                if (g.index < inputTable.size() - 1) {
                    if (n.line == g.line && n.indexes.contains(g.index + 1)) {
                        g.numbers.add(n.value);
                    }
                }
            }
            if (g.numbers.size() == 2) {
                gearRatioSum += g.numbers.get(0) * g.numbers.get(1);
            }
        }
        System.out.println(gearRatioSum);
    }

    static private class Gear {
        int index, line;
        List<Integer> numbers = new ArrayList<>();

        public Gear(int idx, int l) {
            index = idx;
            line = l;
        }
    }

    static private class Number {
        int value, line;
        List<Integer> indexes = new ArrayList<>();

        public Number(int val, int l, List<Integer> i) {
            value = val;
            line = l;
            indexes = i;
        }
    }

    private static List<String> initInput(File input) throws FileNotFoundException {
        List<String> returnList = new ArrayList<>();
        Scanner myReader;
        myReader = new Scanner(input);

        while (myReader.hasNextLine()) {
            returnList.add(myReader.nextLine());
        }

        myReader.close();
        return returnList;
    }
}