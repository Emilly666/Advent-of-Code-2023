import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class App {
    public static void main(String[] args) {
        // declarations
        List<List<Character>> inputTable = new ArrayList<>();
        File myObj = new File("Day3(java)/input.txt");

        // create list of lists of characters
        inputTable = initInput(myObj);

        System.out.println(inputTable);
    }

    private static List<List<Character>> initInput(File input) {
        List<List<Character>> returnList = new ArrayList<>();
        Scanner myReader;
        try {
            myReader = new Scanner(input);
            while (myReader.hasNextLine()) {
                List<Character> line = new ArrayList<>();

                for (char ch : myReader.nextLine().toCharArray()) {
                    line.add(ch);
                }
                returnList.add(line);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        return returnList;
    }

}
