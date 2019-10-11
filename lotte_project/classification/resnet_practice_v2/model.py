from keras.applications import InceptionResNetV2
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras import initializers
from keras.optimizers import Adam
from tensorflow.keras import layers
import resnet_prac as rp
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

model = Sequential()

model.add(InceptionResNetV2(include_top=False, input_shape=(75,75,3),weights='imagenet'))
model.add(Flatten())
model.add(Dense(units=rp.class_num, activation='softmax'))

print(model.summary())

# 신기하게도 multi-classify인데도 loss function을 binary-crossentropy를 쓰는 것이 효과적.
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

hist = model.fit(rp.X_train, rp.Y_train,
          batch_size=rp.batch_size,
          epochs=rp.epochs,
          validation_data=(rp.X_test, rp.Y_test),
          shuffle=True)

'''
model.fit_generator(
    rp.train_generator,
    epochs=rp.epochs,
    steps_per_epoch= rp.steps_per_epochs,
    validation_data=rp.test_generator,
    validation_steps=5
)
'''
print()
loss, acc = model.evaluate(rp.X_test, rp.Y_test, verbose=1)
# loss, acc = model.evaluate_generator(rp.test_generator, steps=5)

print('Test loss:', loss)
print('Test Accuracy', acc)

predictions = model.predict(rp.X_test)



error_path = '/home/pc/Desktop/Machine_Learning/Project_Lotte/sample_data/error/'

# 이미지 출력 너무 많으면 프리징걸림.
# 따라서 에러 이미지를 저장해주는 것으로 변경.
class_error_print = np.zeros(51)


# 에러 출력 및 에러 데이터 저장.
# 이미지를 불러오려고 했으나 에러이미지가 너무 많아 오버플로우.
for i in range(rp.X_test.shape[0]):
    if predictions[i] is not rp.Y_test[i]:
        cv2.imwrite(os.path.join(error_path,str(i)+'.jpg'),rp.X_test[i])
        class_error_print[np.argmax(rp.Y_test[i])]+=1
     #   plt.figure()
     #   plt.imshow((rp.X_test[i]*255).astype(np.uint8))
#plt.show()
#rp.folder_list[np.argmax(rp.Y_test[i])]

for j in range(rp.folder_list.size):
    print(str(rp.folder_list[j])+" has "+str(int(class_error_print[j]))+" error")

# plotting
fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='center left')

acc_ax.plot(hist.history['acc'], 'b', label='train acc')
acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')
acc_ax.set_ylabel('accuracy')
acc_ax.legend(loc='center right')

plt.show()
