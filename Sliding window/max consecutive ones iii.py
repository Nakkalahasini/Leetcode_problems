from typing import List

class Solution:
    """
    Problem: Max Consecutive Ones III
    Platform: LeetCode
    Link: https://leetcode.com/problems/max-consecutive-ones-iii/
    Difficulty: Medium

    Topics:
    - Sliding Window
    - Two Pointers
    - Array

    Approach:
    We use the Sliding Window technique.
    Expand the window using the right pointer.
    Count the number of zeros inside the window.
    If zeros exceed k, shrink the window from the left.
    Keep track of the maximum window size.

    Time Complexity: O(n)
    - Each element is visited at most twice (left and right pointers).

    Space Complexity: O(1)
    - We use only a few variables.
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0      # Maximum length of valid subarray
        left = 0            # Left pointer of sliding window
        zero_count = 0      # Number of zeros in current window

        for right in range(len(nums)):
            
            # If current element is 0, increment zero count
            if nums[right] == 0:
                zero_count += 1

            # If zero count exceeds k, shrink window from left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
