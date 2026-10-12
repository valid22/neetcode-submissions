const auto fast_io = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<int> waiting;
        std::vector<int>days(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); ++i) {
            while (!waiting.empty() && temperatures[i] > temperatures[waiting.top()]) {
                days[waiting.top()] = i - waiting.top();
                waiting.pop();
            }

            waiting.push(i);
        }

        return days;
    }
};
