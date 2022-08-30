import rospy

from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan

class Car_Follower():
    def __init__(self):
        self.sub = rospy.Subscriber("입력받을 LiDAR 토픽 이름", LaserScan, self.callback)

        self.pub = rospy.Publisher("발행할 토픽 이름", AckermannDriveStamped, queue_size=1)


    def callback(self, msg):
        '''
        콜백의 해당 부분에서 LiDAR 데이터를 바탕으로 차량의 조향, 속도를 판단한 뒤, 아래의 steering_angle, speed에 값을 넣으면 됨.
        '''

        ackermann_data = AckermannDriveStamped()

        ackermann_data.steering_angle = 0.0 # 조향각 지정
        ackermann_data.speed = 0.0 # 속도 지정


if __name__ == '__main__':
    rospy.init_node("Car_Follwer")
    run = Car_Follower()
    rospy.spin()