# https://setuptools.readthedocs.io/en/latest/setuptools.html#building-and-distributing-packages-with-setuptools
# https://zhuanlan.zhihu.com/p/24312755
# https://docs.python.org/3/distutils/builtdist.html
# pip install wheel , setuptools
# 工具 => pip install semver
# 測試 => https://tox.readthedocs.io/en/latest/
from setuptools import setup , find_packages , version
from os import path

# ### sdist vs bdist 
# # sdist: 包含 setup ...等等 => 歸檔文件
# # bdist: 包含 setup ...等等 => 
# 
# ## build => 編譯
# 
# ### whl
# #1. python3 ./setup.py sdist bdist_wheel
# #2. python3 ./setup.py bdist_wheel
# ## 安裝 whl包或 tar.gz包
# # python3 -m pip install myapptest-0.1.0-py3-none-any.whl
# 
# ### egg
# # python3 ./setup.py bdist_egg
# 
# ## window.exe (需要在Windows10 or 7 ... 執行編譯)
# # python3 ./setup.py bdist_wininst

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README_EN.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name= "minst_data_expansion_o",
    version="1.3r3",
    zip_safe= True,
    python_requires='>=3.6',
    install_requires= [
        'tensorflow',
        'opencv-python',
    ],
    download_url= "https://swdcgghxa.github.io/minst_data_expansion_o",
    packages= find_packages("obfuscate"),
    package_dir= {"": "obfuscate"},
    package_data= {
        "": ["*.so" , "*.dll"],
    },

    author= "40840159",
    author_email= "40840159@gm.nfu.edu.tw",
    maintainer= "40840159",
    maintainer_email= "40840159@gm.nfu.edu.tw",
    description= "Allow users to add more training data in MINST",
    long_description_content_type= "text/markdown",
    long_description= long_description,
    keywords= ("minst", "tensorflow" , "expansion","minst_data_expansion"),
    url= "https://swdcgghxa.github.io/40840159",  
    platforms= "Independant",
    project_urls= {
        "Bug Tracker": "https://bugs.example.com",
        "Documentation": "https://docs.example.com",
        "Source Code": "https://code.example.com",
    },
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers= [
        "Programming Language :: Python :: 3.6",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
)