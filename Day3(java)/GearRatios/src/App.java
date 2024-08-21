import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.*;

public class App {
    public static void main(String[] args) {
        // declarations
        List<String> inputTable = new ArrayList<>();
        List<Number> numberList = new ArrayList<>();
        File myObj = new File("Day3(java)/test.txt");
        Pattern numberPattern = Pattern.compile("(\\d+)");

        // create list of Strings
        inputTable = initInput(myObj);

        int i = 0;
        for (String line : inputTable){
            Matcher matcher = numberPattern.matcher(line);
            //iterate over matches and create list of Numbers
            while (matcher.find()) {
                List<Integer> idx = new ArrayList<>();
                for (int j = matcher.start(); j < matcher.end(); j++){
                    idx.add(j);
                }
                numberList.add( new Number(Integer.parseInt(matcher.group()), idx, i) );
            }
            i++;
        }
        //iterate over list of Numbers and find out if they are part numbers

        for (Number n : numberList){
            System.out.println(n);
        }




        System.out.println(inputTable);
    }












    static private class Number{
        int value = 0;
        List<Integer> indexes = new ArrayList<>();
        boolean isPartNumber = true;
        int line;
        
        public Number(int val, List<Integer> idx, int l){
            value = val;
            indexes = idx;
            line = l;
        }
        @Override
        public String toString (){
            return "line: " + line + ", value: " + value + ", indexes: " + indexes.toString() + ", is part number: " + isPartNumber;
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
