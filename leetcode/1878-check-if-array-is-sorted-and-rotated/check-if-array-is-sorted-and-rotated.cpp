class Solution {
public:
  bool check(std::vector<int>& nums) {
    int length = nums.size();

    // Find the minimum element in the array
    int minValue = nums[0];
    for (int i = 1; i < length; i++) {
        if (nums[i] < minValue) {
            minValue = nums[i];
        }
    }

    // Find all occurrences of the minimum element
    std::vector<int> minIndices;
    for (int i = 0; i < length; i++) {
        if (nums[i] == minValue) {
            minIndices.push_back(i);
        }
    }

    // Check if any of the minimum indices satisfy the condition for a rotated array
    for (int minIndex : minIndices) {
        bool isSorted = true;
        for (int i = 0; i < length - 1; i++) {
            int currIndex = (minIndex + i) % length;
            int nextIndex = (minIndex + i + 1) % length;

            if (nums[nextIndex] < nums[currIndex]) {
                isSorted = false;
                break;
            }
        }
        if (isSorted) {
            return true;
        }
    }

    return false;
}
};