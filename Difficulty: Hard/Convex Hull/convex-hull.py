class Solution:
    def findConvexHull(self,p):
        p=sorted(set(map(tuple,p)))
        if len(p)<3:return [[-1]]
        C=lambda a,b,c:(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        lo=[];hi=[]
        for x in p:
            while len(lo)>1 and C(lo[-2],lo[-1],x)<=0:lo.pop()
            lo.append(x)
        for x in p[::-1]:
            while len(hi)>1 and C(hi[-2],hi[-1],x)<=0:hi.pop()
            hi.append(x)
        return [list(x) for x in lo[:-1]+hi[:-1]]