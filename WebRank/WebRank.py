import numpy as np

def hub(m,showstep):
  err = 0.0001
  length = len(m[0])
  h = np.ones(length)
  mmt = np.dot(m,m.T)
  h_prev = np.zeros_like(h)
  step=1
  if(showstep):
    print("Step: ",step," ",h)
  while(np.all(np.abs(h-h_prev)<err)==False):
    h_prev = h
    h = np.dot(mmt,h)
    h = h*length/np.sum(h)  
    step+=1
    if(showstep):
      print("Step: ",step," ",h)
  h = np.round(h,3)

  return h

def authority(m,showstep):
  err = 0.0001
  length = len(m[0])
  a = np.ones(length)
  mtm = np.dot(m.T,m)
  a_prev = np.zeros_like(a)
  step=1
  if(showstep):
    print("Step: ",step," ",a)
  while(np.all(np.abs(a-a_prev)<err)==False):
    a_prev = a
    a = np.dot(mtm,a)
    a = a*length/np.sum(a) 
    step+=1
    if(showstep):
      print("Step: ",step," ",a)
  a = np.round(a,3)

  return a

def pageRank(sm,showstep):
  err = 0.0001
  length = len(sm[0])
  r = np.ones(length)
  r_prev = np.zeros_like(r)
  step=1
  if(showstep):
    print("Step: ",step," ",r)
  while(np.all(np.abs(r-r_prev)<err)==False):
    r_prev = r
    r = 0.8*np.dot(sm,r)+0.2
    r = r*length/np.sum(r) 
    step+=1
    if(showstep):
      print("Step: ",step," ",r)
  r = np.round(r,3)

  return r

m = np.array([[0,1,1,0],
              [0,0,0,0],
              [0,0,0,1],
              [0,0,1,0]])

b = np.array([[1,1,1],
              [0,0,1],
              [1,1,0]])
              
sm = np.array([[0.5, 0, 0.5],
               [0, 1, 0.5],
               [0.5, 0, 0]])

print("Final Hub weights: ",hub(b,False))
print("Final Authority weights: ",authority(b,False))
#print(hub(m)+authority(m))
print("Final Page Rank: ",pageRank(sm,False))







