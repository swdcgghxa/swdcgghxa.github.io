## pyarmor_obfuscate
https://pyarmor.readthedocs.io/_/downloads/zh/latest/pdf/
```bash
pip install pyarmor
由於pyarmor是全域執行檔故不可用`python -m pyarmor ...`
A: pyarmor obfuscate --recursive --output project/src/minst_data_expansion_o minst_data_expansion/__init__.py
B: pyarmor obfuscate --restrict=0 minst_data_expansion
R: pyarmor obfuscate --recursive --output minst_data_expansion/obfuscate/minst_data_expansion_o minst_data_expansion/src/minst_data_expansion/__init__.py
```

## setuptoole
https://pypi.org/pypi?%3Aaction=list_classifiers
https://pypi.org/help/#description-content-type
# 似乎可以解決多平台分發
https://stackoverflow.com/questions/59451069/binary-wheel-cant-be-uploaded-on-pypi-using-twine
```python
cd minst_data_expansion
python3 ./setup.py sdist bdist_wheel
python ./setup.py sdist bdist_wheel --plat-name="linux_x86_64" --py-limited-api=cp36
https://stackoverflow.com/questions/37023557/what-does-version-name-cp27-or-cp35-mean-in-python
```


## twine
前提：
```bash
apt install twine
or
python -m pip install --user --upgrade twine
twine upload --repository pypi dist/*
懶一點：
python -m twine upload --skip-existing -u="{user name}" -p="{password}" dist/*
python -m twine upload --skip-existing -u="__token__" -p="{pypi-...}" dist/*
```

## readme-renderer
```bash
python -m readme_renderer README.rst -o /tmp/README.html
```

## 打包打包二進制擴展
https://www.osgeo.cn/python-packaging/overview.html
https://blog.csdn.net/u014597198/article/details/104054250
https://www.osgeo.cn/python-packaging/guides/packaging-binary-extensions.html
## 打包技巧
https://www.mdeditor.tw/pl/pCej/zh-tw
## 專業解說 setuptools
https://mp.weixin.qq.com/s/mAoaIe_Sg3Vk2Sk_xZeI-w
## auditwheel 重新標記 Platform wheels python travis-ci和appveyor
auditwheel windows
https://pypi.org/project/cibuildwheel/
https://www.reddit.com/r/Python/comments/ae7pot/building_wheels_for_all_platforms_versions_and/
https://realpython.com/python-wheels/
## python 版本標籤
https://www.python.org/dev/peps/pep-0425/#python-tag
https://docs.python.org/3/c-api/stable.html

## https://pypi.org/project/minst-data-expansion-o/