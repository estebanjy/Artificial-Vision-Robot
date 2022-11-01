import cv2


camara = cv2.VideoCapture(0)
while True:
    _, frame = camara.read()

    Blanco = cv2.inRange(frame, (200,200,200) , (250, 250, 250))

    contorno, _ = cv2.findContours(Blanco.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contorno:
        area = cv2.contourArea(c)
        if area > 3000:
            if len(contorno) != 0:
                d = max(contorno, key=cv2.contourArea)

            M = cv2.moments(d)
            if (M["m00"] == 0):
                M["m00"] = 1
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            cv2.circle(frame, (x, y), 20, (0, 0, 255), 2)
            nuevoContorno = cv2.convexHull(d)

            cv2.drawContours(frame, [nuevoContorno], -1, (255, 0, 0), 3)

    cv2.imshow("original", frame)
    cv2.imshow("BINARIA", Blanco)

    if cv2.waitKey(1) & 0xFF == ord("f"):
        break