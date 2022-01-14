class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1
            return digits
        else:
            # complications
            return self.plusOne(digits[:len(digits)-1]) + [0]