# Object_identification_with_the_camera
This Python code enables object recognition using a camera input. The code takes a video stream using the OpenCV (cv2) library and recognizes the objects using a deep learning model trained on it.
Bu Python kodu, bir kamera girişi kullanarak nesne tanıma yapmayı sağlar. Kod, OpenCV (cv2) kütüphanesini kullanarak bir video akışı alır ve üzerinde eğitilmiş bir derin öğrenme modeli kullanarak nesneleri tanır.
Kodun işleyişini aşağıdaki adımlarla açıklayabiliriz:
1.	cv2 kütüphanesini içe aktarın.
2.	Kamera için giriş ayarlarını yapın. cv2.VideoCapture(0) ile bir video yakalayıcı nesnesi oluşturulur ve set() yöntemi ile görüntü çerçeve genişliği ve yüksekliği ayarlanır.
3.	Eğitilmiş modeli yükleyin. cv2.dnn.readNetFromTensorflow() fonksiyonuyla, TensorFlow'da eğitilmiş bir modelin ağırlıklarını (model.pb) ve yapılandırma dosyasını (model.pbtxt) okuyarak bir derin öğrenme modeli oluşturulur.
4.	Sınıf isimlerini yükleyin. classes.txt dosyasını okuyarak, nesne sınıfı adlarını içeren bir liste oluşturulur.
5.	Sonsuz bir döngü başlatın. Bu döngüde, her bir kare için aşağıdaki adımlar gerçekleştirilir:
a. Görüntüyü alın. cap.read() fonksiyonuyla bir sonraki kareyi (frame) ve dönüş değerini (ret) alırsınız.
b. Görüntü boyutlarını alın. frame.shape özelliği ile görüntünün yüksekliğini, genişliğini ve kanal sayısını elde edersiniz.
c. Girdi görüntüsünü yeniden boyutlandırın. cv2.resize() fonksiyonu ile görüntüyü istenen boyuta (300x300) yeniden boyutlandırırsınız.
d. Girdiyi normalleştirin. cv2.dnn.blobFromImage() fonksiyonunu kullanarak görüntüyü normalize edersiniz. Bu, görüntüyü modele giriş olarak uygun hale getirir.
e. Yapay zeka modeli üzerinde nesne tanıma işlemi yapın. net.setInput() ile modelin girişini ayarlar ve net.forward() ile tahminleri elde edersiniz.
f. Tahminleri işleyin. Tahminlerdeki her bir nesne için güveni (confidence), sınıf kimliğini (class_id) ve sınıf adını (class_name) alırsınız. Ardından, tahmin edilen nesneyi çerçeve üzerinde dikdörtgen kutu ve etiket ile görselleştirirsiniz.
g. Görüntüyü ekranda gösterin. cv2.imshow() ile nesne tanıma sonuçlar



This Python code enables object recognition using a camera input. The code takes a video stream using the OpenCV (cv2) library and recognizes the objects using a deep learning model trained on it.
We can explain the operation of the code with the following steps:
1. Import cv2 library.
2. Configure the input settings for the camera. A video capture object is created with cv2.VideoCapture(0) and the image frame width and height are set with the set() method.
3. Load the trained model. With the cv2.dnn.readNetFromTensorflow() function, a deep learning model is created by reading the weights (model.pb) and configuration file (model.pbtxt) of a model trained in TensorFlow.
4. Upload the class names. By reading the classes.txt file, a list of object class names is generated.
5. Start an endless loop. In this cycle, the following steps are performed for each frame:
a. Get the image. With the cap.read() function you get the next frame (frame) and the return value (ret).
b. Get the image dimensions. With the frame.shape property you get the height, width and number of channels of the image.
c. Resize the input image. With the cv2.resize() function you resize the image to the desired size (300x300).
D. Normalize the input. You normalize the image using the cv2.dnn.blobFromImage() function. This makes the image suitable as an input to the model.
to. Perform object recognition on the artificial intelligence model. With net.setInput() you set the input of the model and with net.forward() you get the predictions.
f. Process the estimates. You get the trust (confidence), class id (class_id) and class name (class_name) for each object in the predictions. Then you visualize the predicted object with the rectangular box and label on the frame.
g. Display the image on the screen. Object recognition results with cv2.imshow()
