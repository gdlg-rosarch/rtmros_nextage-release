Name:           ros-indigo-nextage-description
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS nextage_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/nextage_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-urdf

%description
As a part of rtmros_nextage package that is a ROS interface for Nextage dual-
armed robot from Kawada Robotics Inc, this package provides its 3D model that
can be used in simulation and MoveIt!-based motion planning tasks.

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
* Tue May 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.6.2-0
- Autogenerated by Bloom

* Mon Mar 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.6.1-0
- Autogenerated by Bloom

* Mon Feb 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.6.0-0
- Autogenerated by Bloom

