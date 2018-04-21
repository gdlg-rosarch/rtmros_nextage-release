# Script generated with Bloom
pkgdesc="ROS - The rtmros_nextage package is a ROS interface for <a href="http://nextage.kawada.jp/en/">Nextage</a> dual-armed robot from Kawada Robotics Inc."
url='http://ros.org/wiki/rtmros_nextage'

pkgname='ros-kinetic-rtmros-nextage'
pkgver='0.8.4_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-nextage-calibration'
'ros-kinetic-nextage-description'
'ros-kinetic-nextage-gazebo'
'ros-kinetic-nextage-ik-plugin'
'ros-kinetic-nextage-moveit-config'
'ros-kinetic-nextage-ros-bridge'
)

conflicts=()
replaces=()

_dir=rtmros_nextage
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtmros_nextage $srcdir/rtmros_nextage
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

