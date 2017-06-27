package util;

import java.util.ArrayList;
import java.util.List;

public class Kmp {

    private CharSequence needle;
    private int[] pi;

    public Kmp(CharSequence needle) {
        this.needle = needle;
        pi = getPartialMatch(needle);
    }

    public int indexIn(CharSequence hay) {
        return indexIn(hay, 0);
    }
    
    public int indexIn(CharSequence hay, int startIndex) {
        final int n = hay.length() - startIndex;
        final int m = needle.length();
        int begin = startIndex, matched = 0;
        while (begin <= n - m) {
            if (matched < m && hay.charAt(begin + matched) == needle.charAt(matched)) {
                ++matched;
                if (matched == m) {
                    return begin;
                }
            } else {
                if (matched == 0) {
                    ++begin;
                } else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }
        return -1;
    }

    /**
     * Note: the returned needles may overlap.
     * @param hay
     * @return all indexes of the needle in the hay.
     */
    public List<Integer> allIndexes(CharSequence hay) {
        final int n = hay.length();
        final int m = needle.length();
        List<Integer> ret = new ArrayList<>();
        int begin = 0, matched = 0;
        while (begin <= n - m) {
            if (matched < m && hay.charAt(begin + matched) == needle.charAt(matched)) {
                ++matched;
                if (matched == m) {
                    ret.add(begin);
                }
            } else {
                if (matched == 0) {
                    ++begin;
                } else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }
        return ret;
    }

    private static int[] getPartialMatch(CharSequence needle) {
        final int m = needle.length();
        int[] pi = new int[m];
        int begin = 1, matched = 0;
        while (begin + matched < m) {
            if (needle.charAt(begin + matched) == needle.charAt(matched)) {
                ++matched;
                pi[begin + matched - 1] = matched;
            } else {
                if (matched == 0) {
                    ++begin;
                } else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }
        return pi;
    }

    public static void main(String[] args) {
        Kmp needle = new Kmp("aabaa");
        String hay = "aabaabaabaa";
        System.out.println(needle.indexIn(hay)); //0
        System.out.println(needle.indexIn(hay, 1)); //3
        System.out.println(needle.allIndexes("aabaabaabaa")); //[0,3,6]
    }

}

