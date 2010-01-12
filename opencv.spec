Name:		opencv
Version:	2.0.0
Release:	%mkrel 2
Group:		Sciences/Computer science
License:	GPLv2+
Summary:	Open Source Computer Vision library
URL:		http://opencv.willowgarage.com/wiki/
Source:		http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.0/OpenCV-%{version}.tar.bz2
Patch0:		OpenCV-2.0.0-link-v4l2.patch
Patch1:		OpenCV-2.0.0-libdir.patch
Patch2:		OpenCV-2.0.0-gcc-4.3.patch
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgstreamer-devel
BuildRequires:	libjasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libunicap-devel
BuildRequires:	libv4l-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions for real time computer vision.

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
Requires: %{libml}

%description devel
OpenCv development files.

%files devel
%defattr(-,root,root,-)
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/opencv/OpenCVConfig.cmake

#--------------------------------------------------------------------------------

%package -n python-opencv
Summary: OpenCv python bindings
Group: Development/Python
%py_requires -d

%description -n python-opencv
OpenCv python bindings.

%files -n python-opencv
%defattr(-,root,root,-)
%python_sitearch/*

#--------------------------------------------------------------------------------

%package doc
Summary: OpenCv docs
Group: Books/Computer books

%description doc
OpenCv docs.

%files doc
%defattr(-,root,root,-)
%_datadir/opencv/doc

#--------------------------------------------------------------------------------

%package samples
Summary: OpenCv samples
Group: Books/Computer books

%description samples
OpenCv samples.

%files samples
%defattr(-,root,root,-)
%{_bindir}/opencv_createsamples
%{_bindir}/opencv_haartraining
%{_bindir}/opencv_performance
%{_bindir}/opencv_traincascade
%dir %_datadir/opencv
%_datadir/opencv/samples
%_datadir/opencv/haarcascades
%_datadir/opencv/lbpcascades
#--------------------------------------------------------------------------------

%prep
%setup -q -n OpenCV-%{version}
%patch0 -p0 -b .v4l2
%patch1 -p0 -b .libdir
%patch2 -p0 -b .gcc43

%build
%cmake \
	-DBUILD_EXAMPLES=BOOL:ON \
	-DINSTALL_C_EXAMPLES=BOOL:ON \
	-DINSTALL_PYTHON_EXAMPLES=BOOL:ON \
	-DINSTALL_OCTAVE_EXAMPLES=BOOL:ON \
	-DWITH_FFMPEG=BOOL:ON
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%check
pushd build
# fwang: to be fixed by upstream:
# Some correctness tests occasionally fail; in 99% of cases those
# are known problems in the tests.
# LD_LIBRARY_PATH=%{buildroot}%{_libdir}:`pwd`/lib:%{_libdir} ctest -V
popd

%clean
%__rm -rf %{buildroot}
