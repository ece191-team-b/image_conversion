import rclpy
import cv_bridge
import os 
from rclpy.node import Node
from sensor_msgs.msg import Image
import message_filters
import cv2
import time

class ImageSubscriber(Node):
    
    def __init__(self):
        super().__init__('image_subscriber')
        # BRUTE FORCE CODE
        image_0_sub = message_filters.Subscriber(self, Image, '/camera/throttle/image_0')
        image_1_sub = message_filters.Subscriber(self, Image, '/camera/throttle/image_1')
        self.bridge = cv_bridge.CvBridge()
        self.image_count = 0 
        self.path = "/home/chengjing/Desktop/lake_test_img"
        
        ts = message_filters.TimeSynchronizer([image_0_sub, image_1_sub], 1)
        ts.registerCallback(self.image_callback)
        
    def image_callback(self, msg_0, msg_1):
        cv_image_0 = self.bridge.imgmsg_to_cv2(msg_0, desired_encoding='bgr8')
        cv_image_1 = self.bridge.imgmsg_to_cv2(msg_1, desired_encoding='bgr8')
        
        cv2.imwrite(os.path.join(self.path, "image_" + str(self.image_count)+".png"), cv2.cvtColor(cv_image_0, cv2.COLOR_BGR2RGB))
        self.image_count += 1
        cv2.imwrite(os.path.join(self.path, "image_" + str(self.image_count)+".png"), cv2.cvtColor(cv_image_1, cv2.COLOR_BGR2RGB))
        self.image_count += 1

def main():
    rclpy.init()
    node = ImageSubscriber()
    rclpy.spin(node)

if __name__ == '__main__':
    main()