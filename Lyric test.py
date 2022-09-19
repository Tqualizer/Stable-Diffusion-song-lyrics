import random
import sys
import subprocess
f = open("Three Hammers.txt")
quotes = f.readlines()
f.close()
sampling = random.sample(quotes, 2)
for sample in sampling:
    print(sample.rstrip())
    subprocess.call(['python', 'optimizedSD/optimized_txt2img_TM.py', "--prompt", sample.rstrip(),"--n_samples","1"])