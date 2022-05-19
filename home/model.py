    
def mlmodel():

    train_path = '/mnt/d/codes/Handwriting-Classifier/training/' 
    test_path = '/mnt/d/codes/Handwriting-Classifier/imgseptest'


    import tensorflow as tf
    from keras_preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale=1./255)
    train_data = train_datagen.flow_from_directory(train_path,target_size=(64,64),batch_size=16,class_mode='categorical')

    # test_datagen = ImageDataGenerator(rescale=1./255)
    # test_data = test_datagen.flow_from_directory('./dataset_model/test',target_size=(64,64),batch_size=16,class_mode = 'categorical')

    cnn = tf.keras.models.Sequential()
    cnn.add(tf.keras.layers.Conv2D(filters = 32,kernel_size= 5,activation='relu',input_shape = [64,64,3],strides=2,padding='same'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters = 64,kernel_size= 3,strides = 1,activation='relu',padding='same'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2,strides=2))
    cnn.add(tf.keras.layers.Flatten())
    cnn.add(tf.keras.layers.Dense(units=512,activation='relu'))
    cnn.add(tf.keras.layers.Dropout(0.5))
    cnn.add(tf.keras.layers.Dense(units=256,activation='relu'))
    cnn.add(tf.keras.layers.Dropout(0.5))
    cnn.add(tf.keras.layers.Dense(units=2,activation='sigmoid'))
    cnn.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    cnn.fit(x=train_data,epochs=25)


    # import keras
    # cnn=keras.models.load_model('test_model_auth_with_drop.h5')


    from keras_preprocessing import image
    import glob
    import numpy as np
    images = []
    # print(glob.glob(test_path))
    for img_path in glob.glob(test_path+'/*'):
        # print(img_path)
        img = image.load_img(img_path,target_size = train_data.target_size)
        img = image.img_to_array(img)
        images.append(img)
    images = np.asarray(images)
    result = cnn.predict(images)

    probab_1 = 0
    for res in result:
        if(res[0]>0.5):
            probab_1+=1
    probab_1/=len(result)
    print('probab_1: ',probab_1)

    probab_2 = 0
    for res in result:
        if(res[1]>0.5):
            probab_2+=1
    probab_2/=len(result)
    print('probab_2: ',probab_2)

    if(probab_1<0.5 and probab_2<0.5):
        final_prediction = 'None'
        return final_prediction

    if(probab_1>probab_2):
        final_prediction = 'User1'
    else: 
        final_prediction = 'User2'
    
    return final_prediction
