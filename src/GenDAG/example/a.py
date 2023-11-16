import b
import c

def pow(e,f):
    answer=1
    for i in range(f):
        answer=b.mul(answer,e)
    return answer

if __name__=="__main__":
    print(pow(2,3))