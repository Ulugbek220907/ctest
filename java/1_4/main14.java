

public class main14{
    public static void main(String[] args){
        System.out.println(add(1, 2, 3, 4, 5));
    }

    //varargs 
    static double add(int... args){
        double sum = 0;
        for(int num: args){
            sum += num;
        }
        return sum;
    }
}