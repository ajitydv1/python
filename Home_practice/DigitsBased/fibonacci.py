f0=0
f1=1
fn=f0+f1
for i in range(0,10):
    fn=fn-2+fn-1
    print(fn,end=" ")
