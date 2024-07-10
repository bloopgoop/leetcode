class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        levels = 0

        for operation in logs:
            if operation == "../":
                if levels:
                    levels -= 1
            elif operation == "./":
                pass
            else:
                levels += 1

        return levels
