##class listnode:
##    def __init__(self,value):
##        self.data=value
##        self.next=None
##    def traverse(self):
##        a=self
##        while a is not None:
##            print(a.data, end=' ')
##            a=a.next
####    def delete(self):
####        assert self is not None, 'invalid pointer'
####        if self.next is None:
####            return None
####        tmp=self.next
####        x=tmp.data
####        self.next=tmp.next
####        return x
##    def delete1(self,x):
##        while self is not None and self.data==x:
##           self=self.next
##        a=self
##        b=self.next
##        while b is not None:
##            if b.data==x:
##                a.next=b.next
##            a=a.next
##            b=b.next
##    def length(self):
##        if self is None:
##            return 0
##        a=self
##        c=0
##        while a is not None:
##            c+=1
##            a=a.next
##        print(c)   
##    def Count(self,x):
##        count=0
##        if self.data==x:
##            count+=1
##        a=self
##        while a.next is not None:
##            if a.next.data==x:
##                count+=1
##            a=a.next    
##        print(count)
##    def del_tail(self):
##        a=self
##        b=self.next
##        while b.next is not None:
##            a=a.next
##            b=b.next
##        
##        a.next=None
##    def splitonneg(a):
##        if a is None:
##            return[None,None]
##        q=a
##        while q is not None:
##            if q.data<0:
##                p=q.next
##                q.next=None
##            return[a,p]
##            q=q.next
##            return[a,None]
##    def insb4tail(self,x):
##         a=self
##         b=self.next
##         while b.next is not None:
##             a=a.next
##             b=b.next
##         new=listnode(x)
##         new.next=b
##         a.next=new
##    def instail(self,x):
##        a=self
##        while a.next is not None:
##            a=a.next
##        new=listnode(x)
##        a.next=new
##        
##a=listnode(12)
##b=listnode(33)
##a.next=b
##c=listnode(33)
##b.next=c
####a.delete1(12)
##a.insb4tail(55)
##a.instail(60)
##a.delete1(12)
####a.traverse()
####a.length()
####a.Count(33)
####a.del_tail()
##a.traverse()
####b.traverse()
######a.delete()
class dlnode:
        def __init__(self,value):
            self.data=value
            self.right=None
            self.left=None
        def traverse(self):
            a=self
            while a.left is not None:
                a=a.left
            while a is not None:
             print(a.data,end=' ')
             a=a.right
        def insertleft(self,value):
               p=self
               q=dlnode(value)
               r=self.left
               self.left=q
               q.right=p
               q.left=r
               if r is not None:
                   r.right=q
        def insertright(self,value):
            p=self
            q=dlnode(value)
            r=self.right
            p.right=q
            q.left=p
            q.right=r
            if r is not None:
                r.left=q
        def search(self,target):
            a=self
            while a is not None and a.data!=target:
                a=a.right
            if a is not None:
                print(a)
            a=self.left
            while a is not None and a.data!=target:
                a=a.left
            if a is not None:
               print(a)
        def max(self):
            Max=self.data
            a=self
            while a is not None: 
                
                if a.data>Max:
                    Max=a.data
                a=a.right    
            a=self.left
            while a.left is not None:
               
                if a.data>Max:
                    Max=a.data
                a=a.left    
            print(Max)    
a=dlnode(13)
b=dlnode(24)
a.right=b
a.left=None
b.left=a
b.right=None
a.insertleft(15)
a.insertright(16)
a.max()
a.traverse()
##b.search(13)
##i=1
##for i in range(6):
##    i=i**2
##    print(i)
for i in range(10,6,-1):
    print(i)
    
    
