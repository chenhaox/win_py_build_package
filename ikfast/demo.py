"""
Created on 2024/6/17 
Author: Hao Chen (chen960216@gmail.com)
"""
from ur_ikfast import URKinematics

ur3e_arm = URKinematics('ur5e')

joint_angles = [-3.1, -1.6, 1.6, -1.6, -1.6, 0.]  # in radians
print("joint angles", joint_angles)

pose_quat = ur3e_arm.forward(joint_angles)
pose_matrix = ur3e_arm.forward(joint_angles, 'matrix')

print("forward() quaternion \n", pose_quat)
print("forward() matrix \n", pose_matrix)

# print("inverse() all", ur3e_arm.inverse(pose_quat, True))
print("inverse() one from quat", ur3e_arm.inverse(pose_quat, False, q_guess=joint_angles))

print("inverse() one from matrix", ur3e_arm.inverse(pose_matrix, False, q_guess=joint_angles))


