import java.util.Arrays;
import java.io.*;
import java.util.*;
import org.json.simple.*;
import org.json.simple.parser.*;

public class javalistsort{
    public static void main(String[] args){
        JSONParser parser = new JSONParser();
        try {
            Object obj = parser.parse(new FileReader("./sort.json"));
            JSONObject jsonObject = (JSONObject)obj;
            System.out.println(jsonObject);
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        
    }
}