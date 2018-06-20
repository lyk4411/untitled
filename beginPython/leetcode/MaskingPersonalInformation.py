import re


class MaskingPersonalInformation(object):
    def maskPII(self, S):
        if '@' in S:  # email
            first, after = S.split('@')
            return "{}*****{}@{}".format(
                first[0], first[-1], after).lower()

        else:  # phone
            digits = re.sub('\D*', '', S)
            local = "***-***-{}".format(''.join(digits[-4:]))
            if len(digits) == 10:
                return local
            return "+{}-".format('*' * (len(digits) - 10)) + local

if __name__ == '__main__':
    a = MaskingPersonalInformation()
    print(a.maskPII("LeetCode@LeetCode.com"))
    print(a.maskPII("AB@qq.com"))
    print(a.maskPII("1(234)567-890"))
    print(a.maskPII("86-(10)12345678"))