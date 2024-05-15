class Solution {
public:
    bool checkPrime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

    int diagonalPrime(std::vector<std::vector<int>>& nums) {
        int largestPrime = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (checkPrime(nums[i][i])) {
                if (largestPrime < nums[i][i]) {
                    largestPrime = nums[i][i];
                }
            }
        }

        int numRows = nums.size();
        int numCols = nums[0].size();

        int row = numRows - 1;
        int col = 0;

        while (row >= 0 && col < numCols) {
            if (checkPrime(nums[row][col])) {
                if (largestPrime < nums[row][col]) {
                    largestPrime = nums[row][col];
                }
            }
            row--;
            col++;
        }
        return largestPrime;
    }
};