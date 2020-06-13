import cv2
import torch
from torchvision.transforms import transforms
from codes_recognizer.network_model import Net


def recognizer(path):
    codes = []
    code = []

    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,)),
                                    ])

    # load nn model
    model = Net()
    model.load_state_dict(torch.load('codes_recognizer/model.pt'))
    model.eval()
    img = cv2.imread(path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)

    ret, im_th = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY_INV)

    ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rects = [cv2.boundingRect(ctr) for ctr in ctrs]

    for rect in rects:
        # Crop image
        crop_img = img[rect[1]:rect[1] + rect[3] + 10, rect[0]:rect[0] + rect[2] + 10, 0]
        # Resize the image
        roi = cv2.resize(crop_img, (28, 28), interpolation=cv2.INTER_CUBIC)
        # roi = cv2.dilate(roi, (3, 3))
        # plt.imshow(roi)
        # plt.show()
        im = transform(roi)
        im = im.view(1, 1, 28, 28)
        with torch.no_grad():
            logps = model(im)
        ps = torch.exp(logps)
        probab = list(ps.numpy()[0])
        code.append(probab.index(max(probab)))


    # cv2.imshow("Code", img)
    # cv2.waitKey()

    return code

