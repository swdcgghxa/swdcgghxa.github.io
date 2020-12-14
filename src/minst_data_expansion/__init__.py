from . import read_img2db , simple_tool
x_train = read_img2db.x_train
y_train = read_img2db.y_train
x_test = read_img2db.x_test
y_test = read_img2db.y_test
get_simple_result = simple_tool.get_simple_result
img_use_increase = simple_tool.img_use_increase

__all__ = [
    "x_train",
    "y_train",
    "x_test",
    "y_test",
    "get_simple_result",
    "img_use_increase",
]