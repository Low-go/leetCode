public class symmetricTree {

    // let's try to do it recursivley and iterativly
    public Boolean isSymmetric(TreeNode root) {
        return Checker(root, root); // we want to compare copies of each node and their left and right
        // with the opposite left or right ones. so having two pairs of the tree
    }                                   // will assist with that comparison

    public boolean Checker(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) { // they have reached their conclusion and they must be correct
            return true;                                // base case
        }
        if (node1 == null || node2 == null) { //  if only one does and not the other it is false
            return false;
        }
        return
                (node1.val == node2.val && Checker(node1.left, node2.right) && Checker(node1.right, node2.left));
                // checks if the two nodes are the same, that condition needs to be met
                // the other conditions are a recursive call on the mirrored components. left with right of respective nodes
                // they will keep recursing over all elements. if conditions continue to be met they will come back either trur pr false

    }

}



