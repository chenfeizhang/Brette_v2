'''

Take the 95 percent bound of these linear response curves as the final null hypothesis test curve. 

'''

import numpy as np
import scipy.io as sio

hostname = 'chenfei'
model = 'Brette_soma1250_L2'
runs = 100 # null hypothesis runs
codedirectory = '/home/%s/Code_git'%(hostname)
datafolder = '/dyn_gain/scratch01/chenfei/%s/'%(model)

for tau in (5,): 
  for (thr,posNa) in ((-18,40),): 
    fr = 5 
    appendix = 'tau%sfr%sthreshold%sposNa%s'%(tau, fr, thr, posNa)
    foldername = datafolder + appendix
    gain = []
    for i in range(1,runs+1):
      data = np.load(datafolder+appendix+'/nullhypothesis/transferdata_nullhypothesis_run%d.npy'%(i))
      dic = data.item()
      gain.append(dic['gain'])
    
    gain = np.array(gain)
    gain = np.sort(gain, axis=0)
    nullgain = gain[int(runs*0.95)]
    if thr<0:
      thr = 'n%d'%(abs(thr))
    else:
      thr = '%d'%(thr)
    data_appendix = 'tau%dfr%dthreshold%sposNa%d'%(tau, fr, thr, posNa)
    data = sio.loadmat(datafolder+'/dynamic_gain_Hz_per_nA_%s.mat'%(data_appendix))
    data['nullgain_%s'%(data_appendix)] = nullgain
    sio.savemat(datafolder+'dynamic_gain_Hz_per_nA_%s'%(data_appendix), data)
