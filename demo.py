from face_app.face_app import FaceApp

instance = FaceApp("images\src_img.jpg", "images\dst_img.jpg", 'static\images\modefied1.jpg')

instance.run()