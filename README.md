# minst 可自訂義 加入資料
## 作者:40840159
## 問題聯絡:40840159@gm.nfu.edu.tw

1. 資料夾布局(很重要)
```
workspace
└── workspace
    └── 40840159
        ├── 0
        │   │── a.jpg
        │   └── b.jpg
        │   └── n.jpg 類推
        ├── 1
        ├── 2
        ├── 3
        └── 9 類推
```
2. 首先需要引入(注意：圖片都已歸一化)
```python
from minst_data_expansion_o import x_train, y_train, x_test, y_test
```

## 另有附上2個可愛的函數工調整
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
