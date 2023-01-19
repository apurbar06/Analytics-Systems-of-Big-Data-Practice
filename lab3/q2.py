import matplotlib.pyplot as plt
import numpy as np

from IPython.display import Javascript
display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))

arr = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28,26, 31, 28, 27, 22, 39, 20, 10, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27]



stem = []   
leaves = []
for i in range(0,len(arr)):
    stem.append((int)(arr[i]/10))
    leaves.append(arr[i]%10)

plt.stem(stem,leaves,linefmt='-.')

plt.title('Stem Leaf Plot')
plt.xlabel('Range/Stems')
plt.ylabel('Points/Leaves')
plt.show()