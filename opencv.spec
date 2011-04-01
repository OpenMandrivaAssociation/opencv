Name:		opencv
Version:	2.2.0
Release:	%mkrel 4
Group:		Sciences/Computer science
License:	GPLv2+
Summary:	Open Source Computer Vision library
URL:		http://opencv.willowgarage.com/wiki/
Source:		http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.2/OpenCV-%{version}.tar.bz2
Patch0:		OpenCV-2.0.0-link-v4l2.patch
Patch1:		OpenCV-2.2.0-remove-extra-libs.patch
Patch2:		OpenCV-2.2-nointernal.patch
Patch3:		OpenCV-2.2-numpy.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk2-devel
BuildRequires:	libgstreamer-devel
BuildRequires:	libjasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libunicap-devel
BuildRequires:	libv4l-devel
BuildRequires:	python-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
BuildRequires:	lapack-devel
BuildRequires:	eigen2
BuildRequires:	python-numpy-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions for real time computer vision.

#--------------------------------------------------------------------------------

%define libopencv_core_soname 2
%define libopencv_core %mklibname opencv_core %{libopencv_core_soname}

%package -n %{libopencv_core}
Summary: OpenCV core library
Group: System/Libraries

%description -n %{libopencv_core}
OpenCV core library (basic structures, arithmetics and linear algebra,
DFT, XML and YAML I/O, etc.).

%files -n %{libopencv_core}
%defattr(-,root,root,-)
%_libdir/libopencv_core.so.%{libopencv_core_soname}*

#--------------------------------------------------------------------------------

%define libopencv_imgproc_soname 2
%define libopencv_imgproc %mklibname opencv_imgproc %{libopencv_imgproc_soname}

%package -n %{libopencv_imgproc}
Summary: OpenCV image processing library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}

%description -n %{libopencv_imgproc}
OpenCV image processing library (filter, Gaussian blur, erode, dilate,
resize, remap, etc.).

%files -n %{libopencv_imgproc}
%defattr(-,root,root,-)
%_libdir/libopencv_imgproc.so.%{libopencv_imgproc_soname}*

#--------------------------------------------------------------------------------

%define libopencv_highgui_soname 2
%define libopencv_highgui %mklibname opencv_highgui %{libopencv_highgui_soname}

%package -n %{libopencv_highgui}
Summary: OpenCV GUI and image/video I/O library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}

%description -n %{libopencv_highgui}
OpenCV GUI and image/video I/O library.

%files -n %{libopencv_highgui}
%defattr(-,root,root,-)
%_libdir/libopencv_highgui.so.%{libopencv_highgui_soname}*

#--------------------------------------------------------------------------------

%define libopencv_ml_soname 2
%define libopencv_ml %mklibname opencv_ml %{libopencv_ml_soname}

%package -n %{libopencv_ml}
Summary: OpenCV machine learning model library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}

%description -n %{libopencv_ml}
OpenCV statistical machine learning models (SVM,
decision trees, boosting, etc.).

%files -n %{libopencv_ml}
%defattr(-,root,root,-)
%_libdir/libopencv_ml.so.%{libopencv_ml_soname}*

#--------------------------------------------------------------------------------

%define libopencv_flann_soname 2
%define libopencv_flann %mklibname opencv_flann %{libopencv_flann_soname}

%package -n %{libopencv_flann}
Summary: OpenCV FLANN library
Group: System/Libraries

%description -n %{libopencv_flann}
OpenCV wrappers for the Fast Library for Approximate Neurest Neighbors
(FLANN).

%files -n %{libopencv_flann}
%defattr(-,root,root,-)
%_libdir/libopencv_flann.so.%{libopencv_flann_soname}*

#--------------------------------------------------------------------------------

%define libopencv_calib3d_soname 2
%define libopencv_calib3d %mklibname opencv_calib3d %{libopencv_calib3d_soname}

%package -n %{libopencv_calib3d}
Summary: OpenCV camera calibration library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}

%description -n %{libopencv_calib3d}
OpenCV library for camera calibration, stereo correspondence, and
elements of 3D data processing.

%files -n %{libopencv_calib3d}
%defattr(-,root,root,-)
%_libdir/libopencv_calib3d.so.%{libopencv_calib3d_soname}*

#--------------------------------------------------------------------------------

%define libopencv_features2d_soname 2
%define libopencv_features2d %mklibname opencv_features2d %{libopencv_features2d_soname}

%package -n %{libopencv_features2d}
Summary: OpenCV 2D feature detectors
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}
Requires: %{libopencv_calib3d} = %{version}-%{release}
Requires: %{libopencv_highgui} = %{version}-%{release}
Requires: %{libopencv_flann} = %{version}-%{release}

%description -n %{libopencv_features2d}
OpenCV 2D feature detectors and descriptors (SURF, FAST, etc.).

%files -n %{libopencv_features2d}
%defattr(-,root,root,-)
%_libdir/libopencv_features2d.so.%{libopencv_features2d_soname}*

#--------------------------------------------------------------------------------

%define libopencv_video_soname 2
%define libopencv_video %mklibname opencv_video %{libopencv_video_soname}

%package -n %{libopencv_video}
Summary: OpenCV motion analysis and object tracking library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}

%description -n %{libopencv_video}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n %{libopencv_video}
%defattr(-,root,root,-)
%_libdir/libopencv_video.so.%{libopencv_video_soname}*

#--------------------------------------------------------------------------------

%define libopencv_objdetect_soname 2
%define libopencv_objdetect %mklibname opencv_objdetect %{libopencv_objdetect_soname}

%package -n %{libopencv_objdetect}
Summary: OpenCV motion analysis and object tracking library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}
Requires: %{libopencv_highgui} = %{version}-%{release}

%description -n %{libopencv_objdetect}
OpenCV object detection library (Haar and LBP face detectors, HOG
people detector, etc.).

%files -n %{libopencv_objdetect}
%defattr(-,root,root,-)
%_libdir/libopencv_objdetect.so.%{libopencv_objdetect_soname}*

#--------------------------------------------------------------------------------

%define libopencv_contrib_soname 2
%define libopencv_contrib %mklibname opencv_contrib %{libopencv_contrib_soname}

%package -n %{libopencv_contrib}
Summary: OpenCV contributed code library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}
Requires: %{libopencv_calib3d} = %{version}-%{release}
Requires: %{libopencv_highgui} = %{version}-%{release}

%description -n %{libopencv_contrib}
OpenCV contributed code library.

%files -n %{libopencv_contrib}
%defattr(-,root,root,-)
%_libdir/libopencv_contrib.so.%{libopencv_contrib_soname}*

#--------------------------------------------------------------------------------

%define libopencv_legacy_soname 2
%define libopencv_legacy %mklibname opencv_legacy %{libopencv_legacy_soname}

%package -n %{libopencv_legacy}
Summary: OpenCV legacy library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}
Requires: %{libopencv_calib3d} = %{version}-%{release}
Requires: %{libopencv_highgui} = %{version}-%{release}
Requires: %{libopencv_video} = %{version}-%{release}

%description -n %{libopencv_legacy}
OpenCV library containing obsolete legacy code.

%files -n %{libopencv_legacy}
%defattr(-,root,root,-)
%_libdir/libopencv_legacy.so.%{libopencv_legacy_soname}*

#--------------------------------------------------------------------------------

%package devel
Summary: OpenCV development files
Group: Development/C
Provides: libopencv-devel = %{version}-%{release}
Requires: %{libopencv_core} = %{version}-%{release}
Requires: %{libopencv_imgproc} = %{version}-%{release}
Requires: %{libopencv_highgui} = %{version}-%{release}
Requires: %{libopencv_ml} = %{version}-%{release}
Requires: %{libopencv_features2d} = %{version}-%{release}
Requires: %{libopencv_video} = %{version}-%{release}
Requires: %{libopencv_objdetect} = %{version}-%{release}
Requires: %{libopencv_calib3d} = %{version}-%{release}
Requires: %{libopencv_flann} = %{version}-%{release}
Requires: %{libopencv_contrib} = %{version}-%{release}
Requires: %{libopencv_legacy} = %{version}-%{release}

%description devel
OpenCV development files.

%files devel
%defattr(-,root,root,-)
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/opencv/OpenCVConfig.cmake

#--------------------------------------------------------------------------------

%package -n python-opencv
Summary: OpenCV Python bindings
Group: Development/Python
%py_requires -d

%description -n python-opencv
OpenCV python bindings.

%files -n python-opencv
%defattr(-,root,root,-)
%python_sitearch/*

#--------------------------------------------------------------------------------

%package doc
Summary: OpenCV docs
Group: Books/Computer books

%description doc
OpenCV docs.

%files doc
%defattr(-,root,root,-)
%_datadir/opencv/doc

#--------------------------------------------------------------------------------

%package samples
Summary: OpenCV sample code
Group: Books/Computer books

%description samples
OpenCV sample code.

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
%patch1 -p0 -b .libs
%patch2 -p1 -b .internal
%patch3 -p1 -b .numpy

cp -p 3rdparty/include/cblas.h 3rdparty
cp -p 3rdparty/include/clapack.h 3rdparty
cp -p 3rdparty/include/f2c.h 3rdparty

rm -rf 3rdparty/lapack
rm -rf 3rdparty/zlib
rm -rf 3rdparty/libjasper
rm -rf 3rdparty/libpng
rm -rf 3rdparty/libjpeg
rm -rf 3rdparty/libtiff
rm -rf 3rdparty/ilmimf
rm -rf 3rdparty/include/*

cp -p 3rdparty/cblas.h 3rdparty/include
cp -p 3rdparty/clapack.h 3rdparty/include
cp -p 3rdparty/f2c.h 3rdparty/include

%build
export PYTHONDONTWRITEBYTECODE=
%cmake \
	-DBUILD_EXAMPLES=BOOL:ON \
	-DINSTALL_C_EXAMPLES=BOOL:ON \
	-DINSTALL_PYTHON_EXAMPLES=BOOL:ON \
	-DINSTALL_OCTAVE_EXAMPLES=BOOL:ON \
	-DWITH_FFMPEG=BOOL:ON 
%make

%install
%__rm -rf %{buildroot}
export PYTHONDONTWRITEBYTECODE=
%makeinstall_std -C build

# Since libraries are installed in /usr/lib even when CMAKE_INSTALL_LIBDIR is set,
# the following workaround is needed:
%ifarch x86_64
mv %{buildroot}/usr/lib/ %{buildroot}%{_libdir}
%endif

# Remove GPU library because it requires CUDA:
%__rm -rf %{buildroot}%{_libdir}/libopencv_gpu*

%check
pushd build
# fwang: to be fixed by upstream:
# Some correctness tests occasionally fail; in 99% of cases those
# are known problems in the tests.
# LD_LIBRARY_PATH=%{buildroot}%{_libdir}:`pwd`/lib:%{_libdir} ctest -V
popd

%clean
%__rm -rf %{buildroot}
