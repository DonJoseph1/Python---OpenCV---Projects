from distutils.command.build_scripts import first_line_re
import cv2, time

first_frame=None

video=cv2.VideoCapture(0)

while True:

    
    check, frame = video.read()


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Applying a  gaussian blur
    gray=cv2.GaussianBlur(gray,(21,21),0)


    #Print gray in 1st iteration
    if first_frame is None:

        first_frame=gray
        #Return to start of while loop, do not go back to beginning of while loop with 'continue'
        continue
   
    delta_frame=cv2.absdiff(first_frame,gray)
    #Creates a tuple
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    #More iterations,  smoother the image
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    #Grab the contours
    (cnts,_) =cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in  cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x,  y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,  y), (x+w, y+h), (0,255,0), 3)
        


    cv2.imshow("Gray_Frame",gray)
    cv2.imshow("Delta_Frame",delta_frame)
    cv2.imshow("Threshold_Frame",thresh_frame)

    #Python waiting for you to  press a key
    key=cv2.waitKey(1)

    if key ==ord('q'):
        break




#Stop Videoq
video.release()
cv2.destroyAllWindowsd

 #1)  cv2.findCountours() finds all regions in our image where there are significant pattern-changes
           # +  changes are calculated by examining "thresh_frame"
           # +  "thresh_frame" represents "what's new inside the camera's view"
           # +  "cnts" is a list-type containing all the changed regions that were recognized

    #  2)  each member of "cnts" is a vector of <cv::Point>-types
           # +  these are simply sub-areas or regions within "thresh_frame"
            #+  our loop assigns to "contour" and we work with one contour region at a time

     # 3)  cv2.contourArea() computes the size/area of the current contour region
            #+  we are ignoring very-small changes (i.e. <10000)
           # +  this should help us filter out anomalies such as shadows or distant light sources, etc.

     # 4)  cv2.boundingRect() computes rectangle-coordinates
           # +  these coordinates enclose the current contour region

    #  5)  cv2.rectangle() draws this rectangle superimposed over our original image
          #  +  the rectangle is drawn upon our "frame" image