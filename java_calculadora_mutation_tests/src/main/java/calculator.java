public class calculator {
    /**
     * This method return the plus between two numbers
     * @return a+b
     */
    public int add(int a, int b) {
        return a+b;
    }

    /**
     * This method return the difference between two numbers
     * @return a-b
     */
    public int subtract(int a, int b) {
        return a-b;
    }

    /**
     * This method multiply two numbers
     * @return a*b
     */
    public int multiply(int a, int b) {
        return a*b;
    }

    /**
     * This following is a basic test of division
     * @return a/b
     */
    public int divide(int a, int b) {
        return a/b;
    }

    /**
     * This method will sum the numbers form n down to 0
     *  This is a start value
     * @return The summation of all the numbers
     */
    public int summation(int start){
        int value = 0;
        while (start >0){
            value += start;
            start --;
        }
        return value;
    }

    public boolean isPositive(int number){
        return number>0;
    }

    /**
     * This method will compare 2 numbers
     * @return 0 if a==b, 1 if a> b, -1 if a<b
     */
    public int compare(int a, int b){
        int value = 0;
        if (a==b){
            value = 0;
        }else if (a > b){
            value =1;
        }else {
            value = -1;
        }
        return value;
    }
}
