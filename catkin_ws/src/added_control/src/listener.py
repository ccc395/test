#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):

          while True
      #sets up where the initial velocity and position is not calculated as it cannot be
        if count != 0:
          #if moving forward
          if ((a_state, b_state_old) == (1,0)) or ((a_state,b_state_old) ==(0,1)):
            #declares the direction of travel is forwards
            direction = "+"
            #declares the location of each pulse
            if (a_state, a_state_old, b_state) == (1,0,0)
              pulcount = pulcount + 1
            #calculates the velocity
            vel = (((pulcount/ticks_per_revolution) * 60)/(time - time_old))
          #if moving backward
          elif((a_state,b_state_old == (1,1))) or ((a_state,b_state_old) == (0,0)):
            #declares the direction of travel is reverse
            direction = "-"
            #declares the location of each pulse
            if (a_state, a_state_old, b_state) == (1,0,0)
              pulcount = pulcount + 1
            #calculates the velocity
            vel = (((pulcount/ticks_per_revolution) * 60)/(time - time_old))
          else 
            #stores the values for when there is no pulse or seperate tic
            trash = trash + 1
          #sets the current states as the old states
          a_state = a_state_old
          b_state = b_state_old
        else
          time = time_old
          count = count + 1
          a_state = a_state_old
          b_state = b_state_old      
        self._velocity = direction + vel
        position = velocity * time
    rospy.loginfo(rospy.get_caller_id() + "what I heard is %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

#!/usr/bin/env python
#import rospy
#from std_msgs.msg import String

#def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    
#def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
#    rospy.init_node('listener', anonymous=True)

#    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
#    rospy.spin()

#if __name__ == '__main__':
#    listener()
