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
def qtan(self,theta):
    return self.qsin(theta)/self.qcos(theta)
def qatan(self,theta):#probably no point of these approximations since python is slow
    halfpi=1.5708
    fa=(halfpi*theta)/(1+abs(theta))
    if theta<5 and theta>-5:
        return fa
    sa=theta*(45+theta**2)/(45+9*theta**2)
   
    
    return (fa+sa)/2
