	 # OpenCV kütüphanesi yüklü olmalıdır ve 
	 # nesne tanıma modelinin kullanılacağı uygulamada 
	 # model dosyalarının (model.pb ve model.pbtxt) 
	 # yüklenmesi gerekir. Sınıf isimlerinin 
	 # (classes.txt) yüklenmesi de gerekebilir. 
	 # Bu dosyaların yüklenmesi için uygun yol ve 
	 # dosya adları belirtilmelidir.


import cv2

# Kamera için giriş ayarları
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Nesne tanıma için eğitilmiş modelin yüklenmesi
net = cv2.dnn.readNetFromTensorflow('model.pb', 'model.pbtxt')

# Sınıf isimlerinin yüklenmesi
classes = []
with open('classes.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

while True:
    # Görüntü al
    ret, frame = cap.read()

    # Görüntü boyutlarını al
    height, width, channels = frame.shape

    # Girdi görüntüsünü yeniden boyutlandır
    resized_frame = cv2.resize(frame, (300, 300))

    # Girdiyi normalleştir
    normalized_frame = cv2.dnn.blobFromImage(resized_frame, 0.007843, (300, 300), 127.5)

    # Yapay zeka modeli üzerinde nesne tanıma işlemi yap
    net.setInput(normalized_frame)
    predictions = net.forward()

    # Tahminleri işle
    for i in range(predictions.shape[2]):
        confidence = predictions[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(predictions[0, 0, i, 1])
            class_name = classes[class_id]
            x1 = int(predictions[0, 0, i, 3] * width)
            y1 = int(predictions[0, 0, i, 4] * height)
            x2 = int(predictions[0, 0, i, 5] * width)
            y2 = int(predictions[0, 0, i, 6] * height)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, class_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Görüntüyü ekranda göster
    cv2.imshow('Object Detection', frame)

    # ESC tuşuna basarak çıkış yap
    if cv2.waitKey(1) == 27:
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()




