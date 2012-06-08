Name:		opencv
Version:	2.4.0
Release:	2
Group:		Sciences/Computer science
License:	GPLv2+
Summary:	Open Source Computer Vision library
URL:		http://opencv.willowgarage.com/wiki/
Source0:		http://downloads.sourceforge.net/opencvlibrary/OpenCV-%{version}.tar.bz2
Patch0:		OpenCV-2.3.0-link-v4l2.patch
BuildRequires:	cmake
BuildRequires:  pkgconfig(gstreamer-app-0.10)
BuildRequires:  pkgconfig(gstreamer-base-0.10)
BuildRequires:  pkgconfig(gstreamer-video-0.10)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
#BuildRequires:  pkgconfig(libavcodec)
#BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdc1394-2)
#BuildRequires:  pkgconfig(libswscale)
BuildRequires:	libjasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libv4l-devel
BuildRequires:	python-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
BuildRequires:	lapack-devel
BuildRequires:	eigen2
BuildRequires:	python-numpy-devel

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
%_libdir/libopencv_ml.so.%{libopencv_ml_soname}*

#--------------------------------------------------------------------------------

%define libopencv_ts_soname 2
%define libopencv_ts %mklibname opencv_ts %{libopencv_ts_soname}

%package -n %{libopencv_ts}
Summary: OpenCV Base test library
Group: System/Libraries
Requires: %{libopencv_core} = %{version}-%{release}

%description -n %{libopencv_ts}
OpenCV Base test library.

%files -n %{libopencv_ts}
%_libdir/libopencv_ts.so.%{libopencv_ts_soname}*

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
%_libdir/libopencv_legacy.so.%{libopencv_legacy_soname}*

#--------------------------------------------------------------------------------

%define libopencv_nonfree_soname 2
%define libopencv_nonfree %mklibname opencv_nonfree %{libopencv_nonfree_soname}

%package -n %{libopencv_nonfree}
Summary: OpenCV motion analysis and object tracking library
Group: System/Libraries

%description -n %{libopencv_nonfree}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n %{libopencv_nonfree}
%_libdir/libopencv_nonfree.so.%{libopencv_nonfree_soname}*

#--------------------------------------------------------------------------------

%define libopencv_photo_soname 2
%define libopencv_photo %mklibname opencv_photo %{libopencv_photo_soname}

%package -n %{libopencv_photo}
Summary: OpenCV motion analysis and object tracking library
Group: System/Libraries

%description -n %{libopencv_photo}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n %{libopencv_photo}
%_libdir/libopencv_photo.so.%{libopencv_photo_soname}*

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
Requires: %{libopencv_ts} = %{version}-%{release}
Requires: %{libopencv_nonfree} = %{version}-%{release}
Requires: %{libopencv_photo} = %{version}-%{release}

%description devel
OpenCV development files.

%files devel
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/OpenCV/*.cmake

#--------------------------------------------------------------------------------
%package -n python-opencv
Summary: OpenCV Python bindings
Group: Development/Python
%py_requires -d

%description -n python-opencv
OpenCV python bindings.

%files -n python-opencv
#python_sitearch/*
%_libdir/python*/*/*

#--------------------------------------------------------------------------------

%package doc
Summary: OpenCV docs
Group: Books/Computer books
BuildArch:	noarch

%description doc
OpenCV docs.

%files doc
%_datadir/OpenCV/doc

#--------------------------------------------------------------------------------

%package samples
Summary: OpenCV sample code
Group: Books/Computer books

%description samples
OpenCV sample code.

%files samples
%{_bindir}/opencv_createsamples
%{_bindir}/opencv_haartraining
%{_bindir}/opencv_performance
%{_bindir}/opencv_traincascade
%dir %_datadir/opencv
%_datadir/opencv/samples
%_datadir/OpenCV/haarcascades
%_datadir/OpenCV/lbpcascades
#--------------------------------------------------------------------------------

%prep
%setup -q -n OpenCV-%{version}
%patch0 -p0

# Fix source files having executable permissions
find . -name "*.cpp" -o -name "*.hpp" -o -name "*.h" |xargs chmod 0644
# And scripts lacking them
find . -name "*.sh" |xargs chmod 0755

%build
export PYTHONDONTWRITEBYTECODE=
%cmake \
	-DBUILD_EXAMPLES=BOOL:ON \
	-DINSTALL_C_EXAMPLES=BOOL:ON \
	-DINSTALL_PYTHON_EXAMPLES=BOOL:ON \
	-DINSTALL_OCTAVE_EXAMPLES=BOOL:ON \
	-DPYTHON_PACKAGES_PATH=%{python_sitearch} \
	-DWITH_FFMPEG=BOOL:OFF
%make

%install
export PYTHONDONTWRITEBYTECODE=
%makeinstall_std -C build

# Remove GPU library because it requires CUDA:
%__rm -rf %{buildroot}%{_libdir}/libopencv_gpu* %{buildroot}%{_bindir}/opencv_stitching \
%{buildroot}%{_libdir}/libopencv_stitching*  %{buildroot}%{_libdir}/libopencv_videostab*

sed -i -e 's/opencv_gpu;//' -e 's/opencv_videostab;//' -e 's/opencv_stitching;//' %{buildroot}%{_datadir}/OpenCV/OpenCVConfig.cmake
sed -i -e 's,\${exec_prefix}/%_lib/libopencv_gpu.so ,,;s,\${exec_prefix}/%_lib/libopencv_stitching.so ,,;s, \${exec_prefix}/%_lib/libopencv_videostab.so,,' %{buildroot}%{_libdir}/pkgconfig/opencv.pc

# Requesting libraries by filename is just bogus...
sed -i -e 's,\${exec_prefix}/%_lib/lib,-l,g;s,\.so,,g' %{buildroot}%{_libdir}/pkgconfig/opencv.pc
