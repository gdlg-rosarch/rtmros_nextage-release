Name:           ros-indigo-nextage-ros-bridge
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS nextage_ros_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nextage_ros_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-hironx-ros-bridge >= 1.0.17
Requires:       ros-indigo-nextage-description
Requires:       ros-indigo-ueye-cam
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-hironx-ros-bridge >= 1.0.17
BuildRequires:  ros-indigo-nextage-description
BuildRequires:  ros-indigo-roslint

%description
The nextage_ros_bridge package is a main ROS interface for developers and users
of Nextage dual-armed robot from Kawada Robotics Inc. Developers can build their
own application that takes control over Nextage via this package. Interface for
both ROS and OpenRTM is provided.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Oct 26 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.1-0
- Autogenerated by Bloom

* Wed Oct 21 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.0-0
- Autogenerated by Bloom

* Sat Oct 17 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.6-0
- Autogenerated by Bloom

* Fri Oct 16 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.5-0
- Autogenerated by Bloom

* Fri Oct 02 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.4-0
- Autogenerated by Bloom

* Sat Aug 15 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.3-0
- Autogenerated by Bloom

* Tue May 12 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.2-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.1-0
- Autogenerated by Bloom

* Mon Feb 23 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.6.0-0
- Autogenerated by Bloom

