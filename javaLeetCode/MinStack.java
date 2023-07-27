import java.util.ArrayList;

class MinStack {

    ArrayList<Integer> stack;
    ArrayList<Integer> minNum;


    public MinStack() {
        stack = new ArrayList<>();
        minNum = new ArrayList<>();
    }

    public void push(int val) {

        if (minNum.isEmpty() || val <= minNum.get(minNum.size() - 1)){ // yo hope this works
            minNum.add(val);
        }
        stack.add(val);

    }

    public void pop() {
        if (stack.isEmpty()){
            return;
        }
        int popped = stack.remove(stack.size() - 1);
        if (minNum.get(minNum.size()-1) == popped){
            minNum.remove(minNum.size() - 1);
        }


    }

    public int top() {
        return stack.get(stack.size() - 1);

    }

    public int getMin() {
        return minNum.get(minNum.size() - 1);
    }
}