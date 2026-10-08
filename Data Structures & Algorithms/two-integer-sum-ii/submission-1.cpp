class Solution {
public:

    int index(int num) {
        if (num > -1) {
            return num;
        } 

        return -num + 1000; //negative numbers start from 1001
    }

    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> n(2001, -1);
        for (int i = 0; i < numbers.size(); ++i) {
            int x = numbers[i];
            int r = target - x;
            int ri = index(r);

            if (n[ri] != -1) {
                return {std::min(i, n[ri]) + 1, std::max(i, n[ri]) + 1};
            }

            n[index(x)] = i;
        }

        return {};
    }
};
