 def qsin(self,theta):   
        if theta==0:
            return 0  
        pi=3.1416
        n=theta%pi
        x=pi-n
        ans= 16*n*x/(5*pi*pi-4*n*x)
        if (theta//pi)%2==0:
            return ans
        else:
            return -ans
def qcos(self,theta):
        pi=3.1416
        return self.qsin(theta+pi/2)
