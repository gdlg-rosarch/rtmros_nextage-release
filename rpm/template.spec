Name:           ros-indigo-nextage-ik-plugin
Version:        0.7.11
Release:        0%{?dist}
Summary:        ROS nextage_ik_plugin package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
IKFast package for NEXTAGE Open

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
* Sat Nov 05 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.11-0
- Autogenerated by Bloom

* Wed Oct 19 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.10-0
- Autogenerated by Bloom

* Thu Oct 13 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.9-0
- Autogenerated by Bloom

* Fri Jul 01 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.8-0
- Autogenerated by Bloom

* Mon May 16 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.7-0
- Autogenerated by Bloom

* Tue Feb 09 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.6-0
- Autogenerated by Bloom

* Wed Jan 27 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.5-0
- Autogenerated by Bloom

* Tue Jan 26 2016 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.4-0
- Autogenerated by Bloom

* Thu Dec 31 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.3-0
- Autogenerated by Bloom

* Mon Nov 02 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.2-0
- Autogenerated by Bloom

* Mon Oct 26 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.1-0
- Autogenerated by Bloom

* Wed Oct 21 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.7.0-0
- Autogenerated by Bloom

* Sat Oct 17 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.6.6-0
- Autogenerated by Bloom

* Fri Oct 16 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.6.5-0
- Autogenerated by Bloom

* Fri Oct 02 2015 IK Fast Plugin Creater <support@opensouce-robotics.tokyo.jp> - 0.6.4-0
- Autogenerated by Bloom

