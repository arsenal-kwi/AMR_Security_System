from setuptools import setup
import os
from glob import glob

package_name = 'initial_and_waypoints_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 스크립트를 설치 대상으로 추가
        (os.path.join('share', package_name, 'scripts'), glob('scripts/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',  # 실제 이름으로 변경
    maintainer_email='your_email@example.com',  # 실제 이메일로 변경
    description='Initial and Waypoints Publisher Node',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 노드 실행을 위한 entry point 추가
            'publish_initial_and_goal = initial_and_waypoints_publisher.publish_initial_and_goal:main'
        ],
    },
)
