
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;


public class Template {
    
    static void pr(Object... a) {
        //if(true) return;
        for(Object x : a) {
            System.out.print(""+x+" ");
        }
        System.out.println();
    }
    
    Object solve() {
        return null;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        String ofile = args[0].substring(0, args[0].length()-2)+"out";
        System.out.println("output file is "+ofile);
        Writer writer = new FileWriter(ofile);
        int T = Integer.parseInt(reader.readLine());
        
        for(int tc=1; tc<=T; tc++) {
            Template problem = new Template();
            Object rt = problem.solve();
            System.out.println(String.format("Case #%d: %s", tc, ""+rt));
            System.out.println("======================================");
            writer.write(String.format("Case #%d: %s\n", tc, ""+rt));
        }
        
        reader.close();
        writer.close();
    }

}

