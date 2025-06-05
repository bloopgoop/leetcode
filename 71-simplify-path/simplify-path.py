class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for directory in paths:
            if not directory:
                continue
                
            directory.replace("/", "")

            if directory == "..":
                if stack:
                    stack.pop()

            elif directory == ".":
                pass

            else:
                stack.append(directory)

        res = ""
        for d in stack:
            res += "/" + d

        return res or "/"