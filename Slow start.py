mport random
from random import seed

def signal(arrofAck):
    seed(1)
    for i in range(5):
        arrofAck[i]=(random.randint(1,100000000000)%2)
def slow_Stat(Wm,Wo,Wn,Cu_BT,arrofAck):
    for j in range(5):
        if(arrofAck[j]==1):
            print ("Successful transmission\n")
            if (Cu_BT <= Wm):
                if (Cu_BT == Wo):
                    Cu_BT = Wo
                    print("Backoff Window Size is:-->",Cu_BT)    
                else:
                    Cu_BT=Cu_BT/2
                    print("Backoff Window Size is:-->",Cu_BT)
            else:
                Cu_BT=Cu_BT-Wo
                print("Backoff window Size is:-->",Cu_BT)
        else:
             if (Cu_BT < Wm):
                Cu_BT = Cu_BT * 2
                print("Backoff window size is*:-->",Cu_BT)
             else:
                print("frame lost due to collision","or interference")
             if(Cu_BT==Wn):
                 Cu_BT=Wn
                 print("Backoff Window size is:-->",Cu_BT)
             else:
                 Cu_BT=Cu_BT+Wo
                 print("Backoff Window size is:-->",Cu_BT)
if __name__=="__main__":
    print("enter initial window size:")
    Wo=int(input())
    print("enter maximum window size:")
    Wn=int(input())
    arrofAck=[None]*5
    print("enter the Threshold value:")
    Wm=int(input())
    print("enter the current backoff window size:")
    Cu_BT=int(input())
    signal(arrofAck)
    slow_Stat(Wm,Wo,Wn,Cu_BT,arrofAck)                
        
    
