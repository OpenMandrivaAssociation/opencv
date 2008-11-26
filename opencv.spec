Name: opencv
Version: 1.1.0
Release: %mkrel 0.pre1.1
Group: Sound
License: GPLv2+
Summary: A library of programming functions mainly aimed at real time computer vision
URL: http://opencv.willowgarage.com/wiki/
Source: opencv-1.1pre1.tar.gz
BuildRequires: gtk2-devel
BuildRequires: glib-devel
BuildRequires: libgstreamer-devel
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: libjasper-devel
BuildRequires: tiff-devel
BuildRequires: libv4l-devel
BuildRequires: libunicap-devel
BuildRequires: libpng-devel
BuildRequires: swig
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: automake
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real time computer vision.

#--------------------------------------------------------------------------------

%define libcv_soname 2
%define libcv %mklibname cv %{libcv_soname}

%package -n %{libcv}
Summary: OpenCv core library
Group: System/Libraries

%description -n %{libcv}
OpenCv core library

%files -n %{libcv}
%defattr(-,root,root,-)
%_libdir/libcv.so.%{libcv_soname}*

#--------------------------------------------------------------------------------

%define libcvaux_soname 2
%define libcvaux %mklibname cvaux %{libcvaux_soname}

%package -n %{libcvaux}
Summary: OpenCv core library
Group: System/Libraries

%description -n %{libcvaux}
OpenCv core library

%files -n %{libcvaux}
%defattr(-,root,root,-)
%_libdir/libcvaux.so.%{libcvaux_soname}*

#--------------------------------------------------------------------------------

%define libcxcore_soname 2
%define libcxcore %mklibname cxcore %{libcxcore_soname}

%package -n %{libcxcore}
Summary: OpenCv core library
Group: System/Libraries

%description -n %{libcxcore}
OpenCv core library

%files -n %{libcxcore}
%defattr(-,root,root,-)
%_libdir/libcxcore.so.%{libcxcore_soname}*

#--------------------------------------------------------------------------------

%define libml_soname 2
%define libml %mklibname ml %{libml_soname}

%package -n %{libml}
Summary: OpenCv core library
Group: System/Libraries

%description -n %{libml}
OpenCv core library

%files -n %{libml}
%defattr(-,root,root,-)
%_libdir/libml.so.%{libml_soname}*

#--------------------------------------------------------------------------------

%define libhighgui_soname 2
%define libhighgui %mklibname highgui %{libhighgui_soname}

%package -n %{libhighgui}
Summary: OpenCv core library
Group: System/Libraries

%description -n %{libhighgui}
OpenCv core library

%files -n %{libhighgui}
%defattr(-,root,root,-)
%_libdir/libhighgui.so.%{libhighgui_soname}*

#--------------------------------------------------------------------------------

%package devel
Summary: OpenCv development files
Group: Development/C
Provides: libopencv-devel = %version
Requires: %{libcv}
Requires: %{libhighgui}
Requires: %{libcxcore}
Requires: %{libcvaux}

%description devel
OpenCv development files.

%files devel
%defattr(-,root,root,-)
%_libdir/*.a
%_libdir/*.so
%_libdir/*.la
%_includedir/*
%_libdir/pkgconfig/*

#--------------------------------------------------------------------------------

%package -n python-opencv
Summary: OpenCv python bindings
Group: Development/Other

%description -n python-opencv
OpenCv python bindings.

%files -n python-opencv
%defattr(-,root,root,-)
%{py_sitedir}/*

#--------------------------------------------------------------------------------

%package doc
Summary: OpenCv docs
Group: Books/Computer books

%description doc
OpenCv docs.

%files doc
%defattr(-,root,root,-)
%dir %_datadir/opencv
%_datadir/opencv/ChangeLog
%_datadir/opencv/THANKS
%_datadir/opencv/readme.txt
%_datadir/opencv/doc

#--------------------------------------------------------------------------------

%package samples
Summary: OpenCv samples
Group: Books/Computer books

%description samples
OpenCv samples.

%files samples
%defattr(-,root,root,-)
%dir %_datadir/opencv
%_bindir/opencv-createsamples
%_bindir/opencv-haartraining
%_bindir/opencv-performance
%_datadir/opencv/samples
%_datadir/opencv/haarcascades

#--------------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -f -i

%configure2_5x \
    --enable-static=no \
    --with-unicap \
    --with-gstreamer \
    --with-swig

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

