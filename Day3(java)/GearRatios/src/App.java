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
        Pattern characterPattern = Pattern.compile("[^.\\d]");


        // create list of Strings
        inputTable = initInput(myObj);

        int i = 0;
        for (String line : inputTable){
            Matcher matcher = numberPattern.matcher(line);
            //iterate over matches and create list of Numbers
            while (matcher.find()) {
                numberList.add( new Number(Integer.parseInt(matcher.group()), matcher.start(), matcher.end(), i) );
            }
            i++;
        }
        //iterate over list of Numbers and find out if they are part numbers

        for (Number n : numberList){
            //System.out.println(n);
        }

        for (Number n : numberList){
            // check up
            if(n.line != 0){
                n.isPartNumber = characterPattern.matcher(inputTable.get(n.line - 1).substring(Math.max(0, n.indexStart-1), Math.min(inputTable.get(n.line - 1).length(), n.indexEnd + 1))).find();  
            }
            // check down
            if(!n.isPartNumber && n.line != inputTable.size() -1){
                n.isPartNumber = characterPattern.matcher(inputTable.get(n.line + 1).substring(Math.max(0, n.indexStart-1), Math.min(inputTable.get(n.line + 1).length(), n.indexEnd + 1))).find();  
            }
            //check left
            if(!n.isPartNumber && n.indexStart != 0){
                n.isPartNumber = characterPattern.matcher( String.valueOf(inputTable.get(n.line).charAt(n.indexStart - 1))).find();
            }
             //check right
             if(!n.isPartNumber && n.indexEnd != inputTable.get(n.line).length() - 1){
                n.isPartNumber = characterPattern.matcher( String.valueOf(inputTable.get(n.line).charAt(n.indexEnd ))).find();
            }
        }
        for (Number n : numberList){
            System.out.println(n.isPartNumber + " " + String.valueOf(n.value));
        }




        System.out.println(inputTable);
    }












    static private class Number{
        int value = 0;
        int indexStart;
        int indexEnd;
        boolean isPartNumber = false;
        int line;
        
        public Number(int val, int idx1, int idx2, int l){
            value = val;
            indexStart = idx1;
            indexEnd = idx2;
            line = l;
        }
        @Override
        public String toString (){
            return "line: " + line + ", value: " + value + ", indexes: " + indexStart + "-" + indexEnd  + ", is part number: " + isPartNumber;
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
