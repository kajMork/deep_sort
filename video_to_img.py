import cv2 as cv




def main():
    video_import_path = "MOT16/test/videos/MOT16-06.webm"
    img_export_path = "MOT16/test/images/"

    # Load the video
    vidcap = cv.VideoCapture(video_import_path)

    # Save each frame as an image
    count = 1
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv.imwrite(img_export_path + "img%d.jpg" % count, image)
        count += 1
        print('Read a new frame: ', success)

if __name__ == "__main__":
    main()