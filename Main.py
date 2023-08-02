import tensorflow as tf
import numpy as np

from tkinter import *
import os
from tkinter import filedialog
import cv2
import time
from matplotlib import pyplot as plt
from tkinter import messagebox





def endprogram():
	print ("\nProgram terminated!")
	sys.exit()






def file_sucess():
    global file_success_screen
    file_success_screen = Toplevel(training_screen)
    file_success_screen.title("File Upload Success")
    file_success_screen.geometry("150x100")
    file_success_screen.configure(bg='pink')
    Label(file_success_screen, text="File Upload Success").pack()
    Button(file_success_screen, text='''ok''', font=(
        'Verdana', 15), height="2", width="30").pack()


global ttype

def training():
    global training_screen

    global clicked

    training_screen = Toplevel(main_screen)
    training_screen.title("Training")
    # login_screen.geometry("400x300")
    training_screen.geometry("600x450+650+150")
    training_screen.minsize(120, 1)
    training_screen.maxsize(1604, 881)
    training_screen.resizable(1, 1)
    training_screen.configure()
    # login_screen.title("New Toplevel")



    Label(training_screen, text='''Upload Image ''', background="#d9d9d9", disabledforeground="#a3a3a3",
          foreground="#000000",  width="300", height="2", font=("Calibri", 16)).pack()
    Label(training_screen, text="").pack()


    options = [
        "Citrus_Black_spot",
        "Citrus_canker",
        "Citrus_greening",
        "Citrus_healthy",
        "Citrus_Melanose",
        "Rice_Bacterial_leaf_blight",
        "Rice_Brown_spot",
        "Rice_Leaf_smut",
        "Tomato_Bacterial_spot",
        "Tomato_Early_blight",
        "Tomato_healthy",
        "Tomato_Late_blight",
        "Tomato_Leaf_Mold",
        "Tomato_Septoria_leaf_spot"




    ]

    # datatype of menu text
    clicked = StringVar()


    # initial menu text
    clicked.set("Corn_(maize)_healthy")

    # Create Dropdown menu
    drop = OptionMenu(training_screen, clicked, *options )
    drop.config(width="30")

    drop.pack()

    ttype=clicked.get()

    Button(training_screen, text='''Upload Image''', font=(
        'Verdana', 15), height="2", width="30", command=imgtraining).pack()




def imgtraining():
    name1 = clicked.get()

    print(name1)

    import_file_path = filedialog.askopenfilename()
    import os
    s = import_file_path
    os.path.split(s)
    os.path.split(s)[1]
    splname = os.path.split(s)[1]


    image = cv2.imread(import_file_path)
    #filename = 'Test.jpg'
    filename = 'Data/'+name1+'/'+splname


    cv2.imwrite(filename, image)
    print("After saving image:")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)
    # import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    from PIL import Image, ImageOps

    im = Image.open(import_file_path)
    im_invert = ImageOps.invert(im)
    im_invert.save('lena_invert.jpg', quality=95)
    im = Image.open(import_file_path).convert('RGB')
    im_invert = ImageOps.invert(im)
    im_invert.save('tt.png')
    image2 = cv2.imread('tt.png')
    cv2.imshow("Invert", image2)

    """"-----------------------------------------------"""

    img = image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', img)
    #cv2.imshow('Gray image', gray)
    #dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    dst = cv2.medianBlur(img, 7)
    cv2.imshow("Nosie Removal", dst)




def fulltraining():
    import model as mm








def testing():
    global testing_screen
    testing_screen = Toplevel(main_screen)
    testing_screen.title("Testing")
    # login_screen.geometry("400x300")
    testing_screen.geometry("600x450+650+150")
    testing_screen.minsize(120, 1)
    testing_screen.maxsize(1604, 881)
    testing_screen.resizable(1, 1)
    testing_screen.configure()
    # login_screen.title("New Toplevel")

    Label(testing_screen, text='''Upload Image''', disabledforeground="#a3a3a3",
          foreground="#000000", width="300", height="2",bg='pink', font=("Calibri", 16)).pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Button(testing_screen, text='''Upload Image''', font=(
        'Verdana', 15), height="2", width="30", command=imgtest).pack()


global affect
def imgtest():


    import_file_path = filedialog.askopenfilename()

    image = cv2.imread(import_file_path)
    print(import_file_path)
    filename = 'Output/Out/Test.jpg'
    cv2.imwrite(filename, image)
    print("After saving image:")
    #result()

    #import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

   # file_sucess()

    print("\n*********************\nImage : " + fnm + "\n*********************")
    img = cv2.imread(import_file_path)
    if img is None:
        print('no data')

    img1 = cv2.imread(import_file_path)
    print(img.shape)
    img = cv2.resize(img, ((int)(img.shape[1] / 5), (int)(img.shape[0] / 5)))
    original = img.copy()
    neworiginal = img.copy()
    cv2.imshow('original', img1)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img1S = cv2.resize(img1, (960, 540))

    cv2.imshow('Original image', img1S)
    grayS = cv2.resize(gray, (960, 540))
    cv2.imshow('Gray image', grayS)

    dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
    cv2.imshow("Nosie Removal", dst)

    thresh = 127
    im_bw = cv2.threshold(grayS, thresh, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow("affect Removal", im_bw)
    number_of_black_pix = np.sum(im_bw == 0)
    #print(number_of_black_pix)
    #if(number_of_black_pix<5000):
        #affect =


    result()







def result():
    import warnings
    warnings.filterwarnings('ignore')

    import tensorflow as tf
    classifierLoad = tf.keras.models.load_model('Model/leafmodel.h5')

    import numpy as np
    from keras.preprocessing import image

    test_image = image.load_img('Output/Out/Test.jpg', target_size=(200, 200))
    img1 = cv2.imread('Output/Out/Test.jpg')
    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifierLoad.predict(test_image)

    out = ''
    pre=''
    if result[0][0] == 1:
        print("Citrus_Black_spot")
        out="Citrus_Black_spot"
        pre ="You can reduce your risk by drinking plenty of water and making sure you use less than 2,300 mg of sodium a day"
    elif result[0][1] == 1:
        print("Citrus_canker")
        out="Citrus_canker"
        pre = "Afinitor (Everolimus),Afinitor Disperz (Everolimus)"
    elif result[0][2] == 1:
        print("Citrus_greening")
        out = "Citrus_greening"
        pre = "You can reduce your risk by drinking plenty of water and making sure you use less than 2,300 mg of sodium a day"

    elif result[0][3] == 1:
        print("Citrus_healthy")
        out = "Citrus_healthy"

    elif result[0][4] == 1:
        print("Citrus_Melanose")
        out = "Citrus_Melanose"
        pre = "Use sprays containing organic copper compounds to treat D. citri. Initial application should take place at petal fall, followed by a secondary treatment 6-8 weeks later."

    elif result[0][5] == 1:
        print("Rice_Bacterial_leaf_blight")
        out = "Rice_Bacterial_leaf_blight"
        pre = "Bacterial blight can be severe in susceptible rice varieties under high nitrogen fertilization"

    elif result[0][6] == 1:
        print("Rice_Brown_spot")
        out = "Rice_Brown_spot"
        pre = "Always consider an integrated approach with both preventive measures and biological treatments if available. The best way to prevent the disease is to use fungicides (e.g., iprodione, propiconazole, azoxystrobin, trifloxystrobin) as seed treatments."
    elif result[0][7] == 1:
        print("Rice_Leaf_smut")
        out = "Rice_Leaf_smut"
        pre = "Cleaning up debris at the end of each growing season can prevent spread of leaf smut. Keeping a good nutrient balance is also important,"



    elif result[0][8] == 1:
        print("Tomato_Bacterial_spot")
        out = "Tomato_Bacterial_spot"
        pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
    elif result[0][9] == 1:
        print("Tomato_Early_blight")
        out = "Tomato_Early_blight"
        pre = "Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable"
    elif result[0][10] == 1:
        print("Tomato_healthy")
        out = "Tomato_healthy"

    elif result[0][11] == 1:
        print("Tomato_Late_blight")
        out = "Tomato_Late_blight"
        pre = "Treat seeds with dilute bleach, hydrochloric acid, or hot water to reduce the potential for seedling infection"
    elif result[0][12] == 1:
        print("Tomato_Leaf_Mold")
        out = "Tomato_Leaf_Mold"
        pre = "Apply a fungicide according to the manufacturer’s instructions at the first sign of infectio"
    elif result[0][13] == 1:
        print("Tomato_Septoria_leaf_spot")
        out = "Tomato_Septoria_leaf_spot"
        pre = "One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil)"




    messagebox.showinfo("Result", "Classfication Result : "+str(out))

    messagebox.showinfo("Fertilizer Or Treatment ", "fertilizer  Or Treatment : " + str(pre))





def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title(" Leaf Disease Prediction")

    Label(text=" Leaf Disease Prediction", width="300", height="5", font=("Calibri", 16)).pack()

    Button(text="UploadImage", font=(
        'Verdana', 15), height="2", width="30", command=training, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()
    Button(text="Training", font=(
        'Verdana', 15), height="2", width="30", command=fulltraining, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()
    Button(text="Testing", font=(
        'Verdana', 15), height="2", width="30", command=testing).pack(side=TOP)

    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()

