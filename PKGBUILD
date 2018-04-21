# Script generated with Bloom
pkgdesc="ROS - A main ROS interface for developers and users of <a href="http://nextage.kawada.jp/en/">Nextage</a> dual-armed robot from Kawada Robotics Inc. Developers can build their own application that takes control over Nextage via this package. Interface for both ROS and <a href="http://openrtm.org/">OpenRTM</a> is provided."
url='http://ros.org/wiki/nextage_ros_bridge'

pkgname='ros-kinetic-nextage-ros-bridge'
pkgver='0.8.4_1'
pkgrel=1
arch=('any')
license=('BSD'
'MIT'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-hironx-ros-bridge>=1.1.13'
'ros-kinetic-nextage-description'
'ros-kinetic-roslint'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-hironx-ros-bridge>=1.1.13'
'ros-kinetic-nextage-description'
'ros-kinetic-stereo-image-proc'
'ros-kinetic-ueye-cam'
)

conflicts=()
replaces=()

_dir=nextage_ros_bridge
source=()
md5sums=()

prepare() {
    cp -R $startdir/nextage_ros_bridge $srcdir/nextage_ros_bridge
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

