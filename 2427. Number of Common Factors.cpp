class Solution {
public:
    int commonFactors(int a, int b) {
        int common_factors;
        
        // find the max number to go to when looking for the common factors
        int max_val = std::max(a, b);

        // loop for calculating the common factors
        for(int i = 1; i <= max_val; i++) {
            if (a % i == 0 && b % i == 0) {
                common_factors++;
            }
        }
        return common_factors;
    }
};