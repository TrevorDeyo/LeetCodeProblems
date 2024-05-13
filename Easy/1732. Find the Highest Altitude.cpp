class Solution {
public:
    int largestAltitude(vector<int>& gain) {
    int highest = 0;
    int currentAltitude = 0;

    for (int gainChange : gain) {
        currentAltitude += gainChange;
        highest = std::max(highest, currentAltitude);
    }

    return highest;
    }
};