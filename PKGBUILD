# Script generated with Bloom
pkgdesc="ROS - This package provides .launch files and other tools for calibrating the head-mount cameras to the NEXTAGE Open robot. As of version 0.7.15/March 2017, only Kinect/Xtion is capable (i.e. Ueye cameras, the ones the robot comes with on this head by default, are not yet handled)."
url='http://ros.org/wiki/nextage_calibration'

pkgname='ros-kinetic-nextage-calibration'
pkgver='0.8.4_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-nextage-gazebo'
)

depends=('ros-kinetic-checkerboard-detector'
'ros-kinetic-dynamic-tf-publisher'
'ros-kinetic-freenect-stack'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-gazebo-ros'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-openni2-launch'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-tf'
'ros-kinetic-turtlebot-description'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=nextage_calibration
source=()
md5sums=()

prepare() {
    cp -R $startdir/nextage_calibration $srcdir/nextage_calibration
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

