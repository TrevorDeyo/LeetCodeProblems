class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // Create a frequency map of characters in magazine
        unordered_map<char, int> freqMap;
        for (char c : magazine) {
            freqMap[c]++;
        }

        // Iterate through ransonNote and check if it can be constructed
        for (char c : ransomNote) {
            if (freqMap.find(c) == freqMap.end() || freqMap[c] <= 0) {
                // If character not found or its count is zero, return false
                return false;
            }
            // Decrement the count of the character
            freqMap[c]--;
        }
        return true; // All characters in ransomNote can be constructed
    }
};