class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        for char in ransomNote:
            if char not in ransom_map:
                ransom_map[char] = 1
            else:
                ransom_map[char] += 1

        magazine_map = {}
        for char in  magazine:
            if char not in magazine_map:
                magazine_map[char] = 1
            else:
                magazine_map[char] += 1
        
        for key in ransom_map:
            if key not in magazine_map:
                return False
            
            if ransom_map[key] > magazine_map[key]:
                return False

        return True
