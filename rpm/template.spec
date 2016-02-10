Name:           ros-indigo-nextage-gazebo
Version:        0.7.6
Release:        0%{?dist}
Summary:        ROS nextage_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/nextage_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-nextage-description
Requires:       ros-indigo-ros-controllers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-gazebo-ros-control
BuildRequires:  ros-indigo-nextage-description
BuildRequires:  ros-indigo-ros-controllers
BuildRequires:  ros-indigo-rostest

%description
Gazebo simulation for NEXTAGE Open

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
* Tue Feb 09 2016 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.6-0
- Autogenerated by Bloom

* Wed Jan 27 2016 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.5-0
- Autogenerated by Bloom

* Tue Jan 26 2016 TORK <dev@opensource-robotics.tokyo.jp> - 0.7.4-0
- Autogenerated by Bloom

