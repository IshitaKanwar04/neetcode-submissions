class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        if len(operations) == 1:
            return int(operations[0])
        for i in range(len(operations)):
            n = len(stack)-1
            if operations[i] == '+':
                stack.append(int(stack[n])+int(stack[n-1]))
            elif operations[i] == 'D':
                stack.append(2*int(stack[n]))
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        sum_s = 0
        for i in range(len(stack)):
            sum_s += stack[i]

        return sum_s 


