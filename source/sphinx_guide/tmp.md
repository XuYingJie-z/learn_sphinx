---
file_format: mystnb
kernelspec:
  name: python
  display_name: Python
---


# 临时文件




```{code-cell} 
---
tags: [hide-output]
---
for i in range(3):
    print("Millhouse did not test cootie positive")
```

```{code-cell} 
:tags: [remove-cell]

import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(2, 100) * 100
```

```{code-cell} 
:tags: [hide-input]

# This cell has a hide-input tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])
```

```{code-cell} 
:tags: [hide-input]

# This cell has a hide-input tag
fig, ax = plt.subplots()
points =ax.scatter(*data, c=data[0], s=data[0])
```
