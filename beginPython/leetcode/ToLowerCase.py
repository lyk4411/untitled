class ToLowerCase(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord('a')+ord(s)-ord('A')) if ord(s) <= ord('Z') and ord(s) >= ord('A') else s for s in str])

if __name__ == '__main__':
    a = ToLowerCase()
    print(a.toLowerCase("Hello"))
