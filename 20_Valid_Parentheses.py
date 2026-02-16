class Solution:
    def isValid(self, s: str) -> bool:
        dict_p = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for char in s:
            if char in dict_p:
                top_element = stack.pop() if stack else '#'
                if dict_p[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
            

       