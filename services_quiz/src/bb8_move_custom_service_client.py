#! /usr/bin/env python

import rospkg
import rospy
# from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_in_square_custom_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square_custom') # Wait for the service client /move_bb8_in_circle to be running
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # Create the connection to the service
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest() # Create an object of type EmptyRequest

move_bb8_in_square_request_object.side = 5.0
move_bb8_in_square_request_object.repetitions = 3

rospy.loginfo("Doing Service Call...")

result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) # Send through the connection the path to the trajectory file to be executed
rospy.loginfo(str(result)) # Print the result given by the service called

rospy.loginfo("END of Service call...")