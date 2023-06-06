import boto3
import cv2
from datetime import datetime
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
def get_file(img):
    now = datetime.now()
    image_string = cv2.imencode('.png', img)[1].tostring()

    client = boto3.client('s3')
    client.put_object(
        Bucket='washswat-machine-learning',
        Key='test/' + str(now.strftime('%Y%m%d%H%M%S%f')) + '.png',  # format: '/my_image.png'
        Body=image_string
    )
    # print(datetime.now() - time)
    # 이미지 로컬 저장 cv2.imwrite('./imgs/' + str(now.microsecond) + '.png', img)
