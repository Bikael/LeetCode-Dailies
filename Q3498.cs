using System;
using System.Collections.Generic;
public class Solution {
    public int ReverseDegree(string s) {
        Dictionary<string, int> alphabet = new Dictionary<string, int>();

        alphabet.Add("a", 26);
        alphabet.Add("b", 25);
        alphabet.Add("c", 24);
        alphabet.Add("d", 23);
        alphabet.Add("e", 22);
        alphabet.Add("f", 21);
        alphabet.Add("g", 20);
        alphabet.Add("h", 19);
        alphabet.Add("i", 18);
        alphabet.Add("j", 17);
        alphabet.Add("k", 16);
        alphabet.Add("l", 15);
        alphabet.Add("m", 14);
        alphabet.Add("n", 13);
        alphabet.Add("o", 12);
        alphabet.Add("p", 11);
        alphabet.Add("q", 10);
        alphabet.Add("r", 9);
        alphabet.Add("s", 8);
        alphabet.Add("t", 7);
        alphabet.Add("u", 6);
        alphabet.Add("v", 5);
        alphabet.Add("w", 4);
        alphabet.Add("x", 3);
        alphabet.Add("y", 2);
        alphabet.Add("z", 1);

        Console.WriteLine("the value of a is: " + alphabet(a));
    }
}