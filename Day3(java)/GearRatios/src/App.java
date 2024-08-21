import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.*;

public class App {
    public static void main(String[] args) {
        // declarations
        List<String> inputTable = new ArrayList<>();
        File myObj = new File("Day3(java)/test.txt");
        Pattern numberPattern = Pattern.compile("(\\d+)");

        // create list of lists of characters
        inputTable = initInput(myObj);

        for (String line : inputTable){
            Matcher matcher = numberPattern.matcher(line);

            while (matcher.find()) {
                List<Integer> idx = new ArrayList<>();
                for (int i = matcher.start(); i < matcher.end(); i++){
                    idx.add(i);
                }

                Number n = new Number(Integer.parseInt(matcher.group()), idx);
                System.out.println(n.indexes);
            }
            System.out.println("\n");
        }




        System.out.println(inputTable);
    }

    static private class Number{
        int value = 0;
        List<Integer> indexes = new ArrayList<>();
        boolean isPartNumber = true;
        
        private Number(int val, List<Integer> idx){
            value = val;
            indexes = idx;
        }
    }







    private static List<String> initInput(File input) {
        List<String> returnList = new ArrayList<>();
        Scanner myReader;
        try {
            myReader = new Scanner(input);
            while (myReader.hasNextLine()) {
                returnList.add(myReader.nextLine());
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return returnList;
    }
}
