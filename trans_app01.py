import cv2


original_face_img = "image/hitoshi.jpg"
# original_face_img = "image/man.png"
original_mask_img = "image/otahuku.png"
def find_face():
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = cv2.imread(original_face_img)
    face_list = cascade.detectMultiScale(img)
    return face_list

def paste_img(face_list):
    x = face_list[0][0]
    y = face_list[0][1]
    w = face_list[0][2]
    h = face_list[0][3]
    face_img = cv2.imread(original_face_img)
    mask_img = cv2.imread(original_mask_img)
    resized_mask_img = cv2.resize(mask_img, dsize=(w, h))
    cv2.imwrite("image/resize_otahuku.png", resized_mask_img)
    face_img[y : h + y, x: w + x] = cv2.imread("image/resize_otahuku.png")
    cv2.imwrite("image/hensin.png", face_img)
    


face_list = find_face()
paste_img(face_list)
