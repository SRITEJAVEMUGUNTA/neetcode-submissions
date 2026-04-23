class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry:
                digits[i] += 1

            
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break

        if carry:
            return [carry] + digits

        else:
            return digits