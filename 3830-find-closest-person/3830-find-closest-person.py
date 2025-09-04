class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        disx=abs(x-z)
        disy=abs(y-z)
        if disx>disy:
            return 2
        elif disx<disy:
            return 1
        else:
            return 0