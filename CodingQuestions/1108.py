#1108. Defanging an IP Address

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        apple = "a.pp.le"
        apple = apple.replace(".", "[.]")
        return address.replace(".", "[.]")

new = Solution()
print(new.defangIPaddr("apple"))
