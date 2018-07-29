class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        q = []
        while ops:
            op = ops.pop(0)
            print op
            if op == 'C':
                r = q.pop()
                ans -= r
            elif op == 'D':
                r = q.pop()
                q.append(r)
                q.append(r*2)
                ans += r * 2
            elif op == '+':
                r1 = q.pop()
                r2 = q.pop()
                ans += r1 + r2
                q.append(r2)
                q.append(r1)
                q.append(r1+r2)
            else:
                ans += int(op)
                q.append(int(op))

        return ans
                