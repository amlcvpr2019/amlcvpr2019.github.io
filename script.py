content = """Bhavya Khailkhura (Lawrence Livermore National Lab)
Catherine Olsson (Google Brain)
David Evans (University of Virginia)
Dimitris Tsipras (Massachusetts Institute of Technology)
Earlence Fernandes (University of Washington)
Eric Wong (Carnegie Mellon University)
Fartash Faghri (University of Toronto)
Florian Tramer (Stanford University)
Hadi Abdullah (University of Florida)
Jonathan Uesato (DeepMind)
Karl Ni (In-Q-Tel)
Kassem Fawaz (University of Wisconsin-Madison)
Kathrin Grosse (CISPA)
Krishna Gummadi (MPI-SWS)
Matthew Wicker (University of Georgia)
Nathan Mundhenk (Lawrence Livermore National Lab)
Nicholas Carlini (Google Brain)
Nicolas Papernot (Google Brain and University of Toronto)
Octavian Suciu (University of Maryland)
Pin-Yu Chen (IBM)
Pushmeet Kohli (DeepMind)
Shreya Shankar (Stanford University)
Suman Jana (Columbia University)
Varun Chandrasekaran (University of Wisconsin-Madison)
Xiaowei Huang (Liverpool University)
Yanjun Qi (University of Virginia)
Yigitcan Kaya (University of Maryland)
Yizheng Chen (Georgia Tech)
Chaowei Xiao (University of Michigan)
Hao Su (UCSD)"""
from pdb import set_trace as st
import numpy as np
cs = content.split('\n')
cs = np.sort(cs)
content_str = ""
for item in cs:
	content_str += "<li>{}</li>\n".format(item)
print(content_str)