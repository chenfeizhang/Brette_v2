'''

This file calls nullhypothesis_step2_runme.py. Take shuffled STAs from series folders, calculate linear response curves for null hypothesis test.

'''

import os
from subprocess import call

# model name, code directory and data directory
hostname = 'chenfei'
model = 'Brette_soma1250_L2'
runs = 100 # null hypothesis runs
codedirectory = '/home/%s/Code_git'%(hostname)
datafolder = '/dyn_gain/scratch01/chenfei/%s/'%(model)
outputdirectory = '%s/Output/'%(datafolder)

# command for submitting jobs
queue_option = 'qsub -q fulla.q -q openmp-fulla01.q -q hel.q -t 1:%d:1 -b y -j y -o %s' %(runs, outputdirectory)
programme = 'python'
script = '%s/transferit/nullhypothesis_step2_runme.py'%(codedirectory)
command = queue_option + ' ' + programme + ' ' + script 

for tau in (5,): 
  for (thr,posNa) in ((-18,40),): 
    for fr in (5, ): 
      appendix = 'tau%sfr%sthreshold%sposNa%s'%(tau, fr, thr, posNa)
      foldername = datafolder + appendix
      if os.path.isdir(foldername+'/nullhypothesis') == False:
        os.mkdir(foldername+'/nullhypothesis')
      call(command + ' ' + appendix + ' ' + datafolder, shell=True)

