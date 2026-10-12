class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<int> waiting;
        std::vector<int>days(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); ++i) {
            while (!waiting.empty() && temperatures[i] > temperatures[waiting.top()]) {
                int j = waiting.top();
                waiting.pop();
                days[j] = i - j;
            }

            waiting.push(i);
        }

        return days;
    }
};
