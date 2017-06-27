package util;

public class Substring implements CharSequence {
    private String s;
    private int beginIndex;
    private int length;

    public Substring(String s, int beginIndex, int endIndex) {
        this.s = s;
        this.beginIndex = beginIndex;
        this.length = endIndex - beginIndex;
        if (beginIndex < 0) {
            throw new StringIndexOutOfBoundsException(beginIndex);
        }
        if (length < 0 || endIndex > s.length()) {
            throw new StringIndexOutOfBoundsException(endIndex);
        }
    }

    @Override
    public int length() {
        return length;
    }

    @Override
    public char charAt(int index) {
        if (index < 0 || index >= length) {
            throw new StringIndexOutOfBoundsException(index);
        }
        return s.charAt(beginIndex + index);
    }

    @Override
    public CharSequence subSequence(int start, int end) {
        if (start < 0) {
            throw new StringIndexOutOfBoundsException(start);
        }
        if (end > length) {
            throw new StringIndexOutOfBoundsException(end);
        }
        return (start == 0 && end == length) ? this : new Substring(s, start + beginIndex, end + beginIndex);
    }

    @Override
    public String toString() {
        return s.substring(beginIndex, beginIndex + length);
    }

    public static void main(String[] args) {
        Substring sub = new Substring("abcde", 1, 4);
        System.out.println(sub.toString()); // bcd
        System.out.println(sub.length()); // 3
        for(int i=0; i<sub.length(); ++i) {
            System.out.println(sub.charAt(i));
        }
    }

}
