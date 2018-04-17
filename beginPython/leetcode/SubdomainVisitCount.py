import collections

from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class StringCompression(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

if __name__ == '__main__':
    cpdomains1 = ["9001 discuss.leetcode.com"]
    cpdomains2 = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    a = StringCompression()
    b = StringCompression()
    print(a.subdomainVisits(cpdomains1))
    print(b.subdomainVisits(cpdomains2))
