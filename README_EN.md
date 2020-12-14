# minst expansion to add data
### Author:40840159
### machine translation
### Question contact:40840159@gm.nfu.edu.tw

1. Folder layout (very important)
```
workspace
└── workspace
    └── 40840159
        ├── 0
        │   │── a.jpg
        │   └── b.jpg
        │   └── n.jpg So on and so forth
        ├── 1
        ├── 2
        ├── 3
        └── 9 So on and so forth
```
2. First need to introduce (note: the pictures have been normalized)
```python
from minst_data_expansion_o import x_train, y_train, x_test, y_test
```

## There are also 2 lovely function adjustments
* get_simple_result
  ```python
  def get_simple_result(x):
    '''x:np.ndarray
    return int
    '''
  ```
* img_use_increase
  ```python
  def img_use_increase(img,multiple=10,noise_removal=100):
    '''img (...,x,x) 0~1 float
    return (...,x,x) 0~1 float'''
  ```
