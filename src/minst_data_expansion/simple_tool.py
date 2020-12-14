def get_simple_result(x):
    '''x:np.ndarray'''
    return max(((i,n) for i,n in enumerate(x.tolist())), key= lambda x:x[1])[0]

def img_use_increase(img,multiple=10,noise_removal=100):
    '''img (...,x,x) 0~1 float
    return (...,x,x) 0~1 float'''
    img = (img * 255)
    img = img * multiple
    img[img > 255] = 254
    img[img < noise_removal] = 0
    return img / 255.0