import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.*;

public class PartNumber {
    public static void main(String[] args) throws FileNotFoundException {
        // declarations
        List<String> inputTable = new ArrayList<>();
        List<Number> numberList = new ArrayList<>();
        File myObj = new File("Day3(java)/input.txt");
        Pattern numberPattern = Pattern.compile("(\\d+)");
        Pattern characterPattern = Pattern.compile("[^.\\d]");
        int partNumberSum = 0;

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
            // check up
            if(n.line > 0){
                n.isPartNumber = characterPattern.matcher(inputTable.get(n.line - 1).substring(Math.max(0, n.indexStart-1), Math.min(inputTable.get(n.line - 1).length(), n.indexEnd + 1))).find();  
            }
            // check down
            if(!n.isPartNumber && n.line < inputTable.size() - 1 ){
                n.isPartNumber = characterPattern.matcher(inputTable.get(n.line + 1).substring(Math.max(0, n.indexStart-1), Math.min(inputTable.get(n.line + 1).length(), n.indexEnd + 1))).find();  
            }
            //check left
            if(!n.isPartNumber && n.indexStart > 0){
                n.isPartNumber = characterPattern.matcher( String.valueOf(inputTable.get(n.line).charAt(n.indexStart - 1))).find();
            }
             //check right
            if(!n.isPartNumber && n.indexEnd < inputTable.get(n.line).length() - 1){
                n.isPartNumber = characterPattern.matcher( String.valueOf(inputTable.get(n.line).charAt(n.indexEnd ))).find();
            }
        }
        for (Number n : numberList){
            if (n.isPartNumber){
                partNumberSum += n.value;
            }
        }
        System.out.println(partNumberSum);
    }

    static private class Number{
        int value, indexStart, indexEnd, line;
        boolean isPartNumber = false;
        
        public Number(int val, int idx1, int idx2, int l){
            value = val;
            indexStart = idx1;
            indexEnd = idx2;
            line = l;
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
