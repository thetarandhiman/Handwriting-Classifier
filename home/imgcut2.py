def imgcut2():    
    import tensorflow as tf
    import numpy as np
    from keras.preprocessing import image as img
    import math
    from PIL import Image,ImageOps

    source_image_path = "/mnt/d/codes/Handwriting-Classifier/media/User2.png"
    destination_folder_path = "/mnt/d/codes/Handwriting-Classifier/training/imgsep2/"
    image = Image.open(source_image_path)
    
    # fixed_height = 113
    # new_width = None
    length = image.size[1]
    # height_percent = (fixed_height / float(image.size[1]))
    # width_size = int((float(image.size[0]) * float(height_percent)))
    # image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
    image = ImageOps.grayscale(image)
    new_width = image.size[0]
    print(new_width)
    image = img.img_to_array(image)
    print(image.shape)
    # image.save('resized_nearest.jpg')
    
    # image=np.expand_dims(image,axis=0)
    image = [image]
    image = np.array(image)
    print(image.shape)
    patches = tf.image.extract_patches(images=image,
                               sizes=[1, 113, 113, 1],
                               strides=[1, 113, 113, 1],
                               rates=[1, 1, 1, 1],
                               padding='SAME')
    
    # # img = tf.reshape(imgs[0,r],shape=(113,113)).numpy().astype(np.uint8)
    # #             img1 = Image.fromarray(img)
    # #             img1.save('./test_data/train/a/'+str(counter)+'.png')
    # #             counter+=1
    
    for imgs in patches:
        count = 322
        for r in range(1,math.floor(length/113)):
            for c in range(1,math.floor(new_width/113)):
                img = tf.reshape(imgs[r,c],shape=(113,113)).numpy().astype("uint8")
                image1 = Image.fromarray(img)
                image1.save(destination_folder_path+'/'+str(count)+'.png')
                count += 1