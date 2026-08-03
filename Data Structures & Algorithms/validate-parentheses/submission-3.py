class Solution:
    """def isValid(self, s: str) -> bool:
        string_size = len(s)
        if string_size % 2 != 0: 
            return False
        else:
            array_size = int(string_size/2)
            right_chars = ['_']*array_size
            left_chars = ['_']*array_size
            for i in range(0,(array_size)):
                left_chars[i] = s[array_size - (i+1)]
                right_chars[i] = s[array_size + (i)]
            for i in range(array_size):
                right_char = right_chars[i]
                left_char = left_chars[i]
                result = (ord(right_char) - ord(left_char))
                print(left_char, right_char, result, left_chars)
                if (result!=1 and result!=2): 
                    return False
            return True"""
    """def isValid(self, s: str) -> bool:
        stack=[]
        pop_value=''
        for char in s:
            if(char =='{' or char=='[' or char=='('):
                if(char=='{'):
                    stack.append('}')
                elif(char=='['):
                    stack.append(']')
                else:
                    stack.append(')')
            else:
                if(len(stack)>0):
                    pop_value=stack.pop()
                    if(pop_value!=char):
                        return False
                else: return False
        if(len(stack)==0):
                    return True
        else: return False"""
    def isValid(self, s: str) -> bool:
        mappings={'{': '}', '[': ']', '(':')'}
        stack = []
        for char in s:
            if char in mappings:
                stack.append(mappings[char])
            else:
                if not stack or stack.pop()!=char:
                    return False
        return not stack
                        





        