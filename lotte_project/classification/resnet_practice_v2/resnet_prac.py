import os
import numpy as np
import cv2
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 32
epochs = 10

# 위노그라드 옵션. 3x3 필터에 대한 연산 최적화
os.environ['TF_ENABLE_WINOGRAD_NONFUSED'] = '1'

data_path = '/home/pc/Desktop/Machine_Learning/Project_Lotte/sample_data/original/CropImage'


folder_list = np.array(os.listdir(data_path))

input=[]
label=[]

label_encoder = LabelEncoder()

# folder list를 unique 숫자로 인코딩
integer_encoded = label_encoder.fit_transform(folder_list)

# one hot encoding을 하기 위해 2차원으로 변형.
integer_encoded = integer_encoded.reshape(len(integer_encoded),1)

# one hot encoding
# categories='auto' 카테고리 num을 자동으로 설정.
# categories='list'를 하면 배열순으로 설정.
onehot_encoder = OneHotEncoder(sparse=False, categories='auto')
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

num = len(folder_list)

# 이미지 데이터 전처리와 로드
for index in range(len(folder_list)):
    path = os.path.join(data_path,folder_list[index])
    path = path +'/'
    sub_list = os.listdir(path)
    print('데이터 로딩중 ' + str(len(folder_list)) + '/' + str(num))
    num -= 1
    for sub in sub_list:
        subpath = os.path.join(path, sub)
        img_list = os.listdir(subpath)
        try:
            for img in img_list:
                img_path = os.path.join(subpath, img)
                img = cv2.imread(img_path)
                img = cv2.resize(img,(75,75))
                input.append(np.array(img))
                label.append((np.array(onehot_encoded[index])))
        except cv2.error:
            print(img_path)
input = np.array(input).astype(np.float32)
label = np.array(label).astype(np.float32)

# split train and test data
X_train, X_test, Y_train, Y_test = train_test_split(input, label, random_state=999)

class_num = folder_list.size
'''
# Agumentation
imageGenerator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    brightness_range=[.2,.2],
    validation_split=.1
)

train_generator = imageGenerator.flow(
    X_train,
    Y_train,
    batch_size=batch_size
)

test_generator = imageGenerator.flow(
    X_test,
    Y_test,
    batch_size=batch_size
)
'''

