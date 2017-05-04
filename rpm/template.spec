Name:           ros-indigo-rtmros-nextage
Version:        0.7.16
Release:        0%{?dist}
Summary:        ROS rtmros_nextage package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rtmros_nextage
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-nextage-calibration
Requires:       ros-indigo-nextage-description
Requires:       ros-indigo-nextage-gazebo
Requires:       ros-indigo-nextage-ik-plugin
Requires:       ros-indigo-nextage-moveit-config
Requires:       ros-indigo-nextage-ros-bridge
BuildRequires:  ros-indigo-catkin

%description
The rtmros_nextage package is a ROS interface for Nextage dual-armed robot from
Kawada Robotics Inc.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Thu May 04 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.16-0
- Autogenerated by Bloom

* Sat Mar 11 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.15-0
- Autogenerated by Bloom

* Tue Feb 21 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.14-0
- Autogenerated by Bloom

* Tue Jan 24 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.13-0
- Autogenerated by Bloom

* Tue Jan 10 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.12-0
- Autogenerated by Bloom

* Sat Nov 05 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.11-0
- Autogenerated by Bloom

* Wed Oct 19 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.10-0
- Autogenerated by Bloom

* Thu Oct 13 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.9-0
- Autogenerated by Bloom

* Fri Jul 01 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.8-0
- Autogenerated by Bloom

* Mon May 16 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.7-0
- Autogenerated by Bloom

* Tue Feb 09 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.6-0
- Autogenerated by Bloom

* Wed Jan 27 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.5-0
- Autogenerated by Bloom

* Tue Jan 26 2016 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.4-0
- Autogenerated by Bloom

* Thu Dec 31 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.3-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Isaac Isao Saito <iisaito@opensource-robotics.tokyo.jp> - 0.7.2-0
- Autogenerated by Bloom

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

