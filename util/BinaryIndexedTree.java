package util;

/**
 * Binary indexed tree for accumulated sum. All indexes are 1 based.
 * @see https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
 * @see http://www.hawstein.com/posts/binary-indexed-trees.html
 * @see https://en.wikipedia.org/wiki/Fenwick_tree
 *
 */
public class BinaryIndexedTree {
    
    private long[] tree;
    
    public BinaryIndexedTree(int size) {
        tree = new long[size+1];
    }
    
    /**
     * 
     * @param idx 1 based index
     * @return sum of elements [1 .. idx] (inclusive)
     */
    public long getSum(int idx){
        long sum = 0;
        while (idx > 0){
            sum += tree[idx];
            idx -= (idx & -idx);
        }
        return sum;
    }
    
    /**
     * 
     * @param idx 1 based index
     * @param delta the delta change of element idx
     */
    public void update(int idx ,long delta) {
        while (idx <= tree.length-1) {
            tree[idx] += delta;
            idx += (idx & -idx);
        }
    }

    /**
     * A bit faster than getSum(idx) - getSum(idx-1).
     * @param idx 1 based index
     */
    public long getSingle(int idx) {
        long sum = tree[idx];
        if (idx > 0) {
            int z = idx - (idx & -idx);
            idx--;
            while (idx != z) {
                sum -= tree[idx];
                idx -= (idx & -idx);
            }
        }
        return sum;
    }
}
