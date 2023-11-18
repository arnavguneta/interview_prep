
# online solution, instead of doing the calculation brute force, calculate the number of possible moves
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_len = len(s)
        if s_len == 0 or s_len == 1:
            return s_len
        
        char_count = {}  # Dictionary to store character counts
        max_count = 0    # Maximum count of a character in the window
        max_len = 0      # Maximum length of the substring
        
        left = 0  # Left pointer of the window

        for right in range(s_len):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])  # Update max_count
            
            # Check if the window size exceeds the available k operations
            if right - left + 1 - max_count > k:
                # Move the left pointer forward and adjust count for the character going out of the window
                char_count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)  # Update max_len
        
        return max_len
