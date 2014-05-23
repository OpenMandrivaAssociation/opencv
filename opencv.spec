%ifnarch %{arm} %{mips}
%bcond_without	java
%endif

Summary:	Open Source Computer Vision library

Name:		opencv
Version:	2.4.9
Release:	2
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://opencv.org/
Source0:	https://github.com/Itseez/opencv/archive/%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		opencv-2.4.5-link-v4l2.patch
Patch1:         opencv-pkgcmake.patch
Patch2:         opencv-pkgcmake2.patch
#http://code.opencv.org/issues/2720
Patch4:         OpenCV-2.4.4-pillow.patch
Patch5:         opencv-2.4.8-ts_static.patch
# fix/simplify cmake config install location (upstreamable)
# https://bugzilla.redhat.com/1031312
Patch6:         opencv-2.4.7-cmake_paths.patch

BuildRequires:	cmake
BuildRequires:	jpeg-devel
BuildRequires:	%{_lib}opencl-devel
BuildRequires:	python-numpy-devel
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-app-0.10)
BuildRequires:	pkgconfig(gstreamer-base-0.10)
BuildRequires:	pkgconfig(gstreamer-video-0.10)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lapack)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(zlib)
%if %{with java}
# Java bindings
BuildRequires:	java-1.7.0-openjdk-devel
BuildRequires:	ant
%endif
# Qt 4.x module
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtOpenGL)
BuildRequires:	pkgconfig(QtTest)
# Documentation generation
BuildRequires:	python-sphinx
BuildRequires:	latex2html

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions for real time computer vision.

#--------------------------------------------------------------------------------

%define libopencv_core_soname 2.4
%define libopencv_core %mklibname opencv_core %{libopencv_core_soname}
%define wrongcore %mklibname opencv_core 2

%package -n	%{libopencv_core}
Summary:	OpenCV core library

Group:		System/Libraries
%rename		%{wrongcore}

%description -n	%{libopencv_core}
OpenCV core library (basic structures, arithmetics and linear algebra,

%files -n	%{libopencv_core}
%{_libdir}/libopencv_core.so.%{libopencv_core_soname}*

#--------------------------------------------------------------------------------

%define libopencv_ts_soname 2.4
%define libopencv_ts %mklibname opencv_ts %{libopencv_ts_soname}
%define wrongts %mklibname opencv_ts 2

%package -n	%{libopencv_ts}
Summary:	OpenCV Base test library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
%rename		%{wrongts}

%description -n	%{libopencv_ts}
OpenCV Base test library.

#--------------------------------------------------------------------------------

%files -n      %{libopencv_ts}
%{_libdir}/libopencv_ts.so.%{libopencv_ts_soname}*
%define libopencv_imgproc_soname 2.4
%define libopencv_imgproc %mklibname opencv_imgproc %{libopencv_imgproc_soname}
%define wrongimgproc %mklibname opencv_imgproc 2

%package -n	%{libopencv_imgproc}
Summary:	OpenCV image processing library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
%rename		%{wrongimgproc}

%description -n	%{libopencv_imgproc}
OpenCV image processing library (filter, Gaussian blur, erode, dilate,
resize, remap, etc.).

%files -n	%{libopencv_imgproc}
%{_libdir}/libopencv_imgproc.so.%{libopencv_imgproc_soname}*

#--------------------------------------------------------------------------------

%define libopencv_highgui_soname 2.4
%define libopencv_highgui %mklibname opencv_highgui %{libopencv_highgui_soname}
%define wronghighgui %mklibname opencv_highgui 2

%package -n	%{libopencv_highgui}
Summary:	OpenCV GUI and image/video I/O library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
%rename		%{wronghighgui}

%description -n	%{libopencv_highgui}
OpenCV GUI and image/video I/O library.

%files -n	%{libopencv_highgui}
%{_libdir}/libopencv_highgui.so.%{libopencv_highgui_soname}*

#--------------------------------------------------------------------------------

%define libopencv_ml_soname 2.4
%define libopencv_ml %mklibname opencv_ml %{libopencv_ml_soname}
%define wrongml %mklibname opencv_ml 2

%package -n	%{libopencv_ml}
Summary:	OpenCV machine learning model library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
%rename		%{wrongml}

%description -n	%{libopencv_ml}
OpenCV statistical machine learning models (SVM,
decision trees, boosting, etc.).

%files -n	%{libopencv_ml}
%{_libdir}/libopencv_ml.so.%{libopencv_ml_soname}*

#--------------------------------------------------------------------------------

%define libopencv_ocl_soname 2.4
%define libopencv_ocl %mklibname opencv_ocl %{libopencv_ocl_soname}

%package -n	%{libopencv_ocl}
Summary:	OpenCV OCL library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_ocl}
OpenCV OCL library

%files -n	%{libopencv_ocl}
%{_libdir}/libopencv_ocl.so.%{libopencv_ocl_soname}*

#--------------------------------------------------------------------------------

%define libopencv_flann_soname 2.4
%define libopencv_flann %mklibname opencv_flann %{libopencv_flann_soname}
%define wrongflann %mklibname opencv_flann 2

%package -n	%{libopencv_flann}
Summary:	OpenCV FLANN library

Group:		System/Libraries
%rename		%{wrongflann}

%description -n	%{libopencv_flann}
OpenCV wrappers for the Fast Library for Approximate Neurest Neighbors
(FLANN).

%files -n	%{libopencv_flann}
%{_libdir}/libopencv_flann.so.%{libopencv_flann_soname}*

#--------------------------------------------------------------------------------

%define libopencv_calib3d_soname 2.4
%define libopencv_calib3d %mklibname opencv_calib3d %{libopencv_calib3d_soname}
%define wrongcalib3d %mklibname opencv_calib3d 2

%package -n	%{libopencv_calib3d}
Summary:	OpenCV camera calibration library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
%rename		%{wrongcalib3d}

%description -n	%{libopencv_calib3d}
OpenCV library for camera calibration, stereo correspondence, and
elements of 3D data processing.

%files -n	%{libopencv_calib3d}
%{_libdir}/libopencv_calib3d.so.%{libopencv_calib3d_soname}*

#--------------------------------------------------------------------------------

%define libopencv_features2d_soname 2.4
%define libopencv_features2d %mklibname opencv_features2d %{libopencv_features2d_soname}
%define wrongfeatures2d %mklibname opencv_features2d 2

%package -n	%{libopencv_features2d}
Summary:	OpenCV 2D feature detectors

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_calib3d} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
Requires:	%{libopencv_flann} = %{EVRD}
%rename		%{wrongfeatures2d}

%description -n	%{libopencv_features2d}
OpenCV 2D feature detectors and descriptors (SURF, FAST, etc.).

%files -n	%{libopencv_features2d}
%{_libdir}/libopencv_features2d.so.%{libopencv_features2d_soname}*

#--------------------------------------------------------------------------------

%define libopencv_superres_soname 2.4
%define libopencv_superres %mklibname opencv_superres %{libopencv_superres_soname}

%package -n	%{libopencv_superres}
Summary:	OpenCV super-resolution support

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_superres}
Super-resolution support for OpenCV.

%files -n	%{libopencv_superres}
%{_libdir}/libopencv_superres.so.%{libopencv_superres_soname}*

#--------------------------------------------------------------------------------

%define libopencv_video_soname 2.4
%define libopencv_video %mklibname opencv_video %{libopencv_video_soname}
%define wrongvideo %mklibname opencv_video 2

%package -n	%{libopencv_video}
Summary:	OpenCV motion analysis and object tracking library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
%rename		%{wrongvideo}

%description -n	%{libopencv_video}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n	%{libopencv_video}
%{_libdir}/libopencv_video.so.%{libopencv_video_soname}*

#--------------------------------------------------------------------------------

%define libopencv_objdetect_soname 2.4
%define libopencv_objdetect %mklibname opencv_objdetect %{libopencv_objdetect_soname}
%define wrongobjdetect %mklibname opencv_objdetect 2

%package -n	%{libopencv_objdetect}
Summary:	OpenCV motion analysis and object tracking library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
%rename		%{wrongobjdetect}

%description -n	%{libopencv_objdetect}
OpenCV object detection library (Haar and LBP face detectors, HOG
people detector, etc.).

%files -n	%{libopencv_objdetect}
%{_libdir}/libopencv_objdetect.so.%{libopencv_objdetect_soname}*

#--------------------------------------------------------------------------------

%define libopencv_contrib_soname 2.4
%define libopencv_contrib %mklibname opencv_contrib %{libopencv_contrib_soname}
%define wrongcontrib %mklibname opencv_contrib 2

%package -n	%{libopencv_contrib}
Summary:	OpenCV contributed code library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_calib3d} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
%rename		%{wrongcontrib}

%description -n	%{libopencv_contrib}
OpenCV contributed code library.

%files -n	%{libopencv_contrib}
%{_libdir}/libopencv_contrib.so.%{libopencv_contrib_soname}*

#--------------------------------------------------------------------------------

%define libopencv_legacy_soname 2.4
%define libopencv_legacy %mklibname opencv_legacy %{libopencv_legacy_soname}
%define wronglegacy %mklibname opencv_legacy 2

%package -n	%{libopencv_legacy}
Summary:	OpenCV legacy library

Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_calib3d} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
Requires:	%{libopencv_video} = %{EVRD}
%rename		%{wronglegacy}

%description -n	%{libopencv_legacy}
OpenCV library containing obsolete legacy code.

%files -n	%{libopencv_legacy}
%{_libdir}/libopencv_legacy.so.%{libopencv_legacy_soname}*

#--------------------------------------------------------------------------------

%define libopencv_nonfree_soname 2.4
%define libopencv_nonfree %mklibname opencv_nonfree %{libopencv_nonfree_soname}
%define wrongnonfree %mklibname opencv_nonfree 2

%package -n	%{libopencv_nonfree}
Summary:	OpenCV motion analysis and object tracking library

Group:		System/Libraries
%rename		%{wrongnonfree}

%description -n	%{libopencv_nonfree}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n %{libopencv_nonfree}
%{_libdir}/libopencv_nonfree.so.%{libopencv_nonfree_soname}*

#--------------------------------------------------------------------------------

%define libopencv_photo_soname 2.4
%define libopencv_photo %mklibname opencv_photo %{libopencv_photo_soname}
%define wrongphoto %mklibname opencv_photo 2

%package -n	%{libopencv_photo}
Summary:	OpenCV motion analysis and object tracking library

Group:		System/Libraries
%rename		%{wrongphoto}

%description -n	%{libopencv_photo}
OpenCV motion analysis and object tracking library (optical flow,
motion templates, background subtraction, etc.).

%files -n	%{libopencv_photo}
%{_libdir}/libopencv_photo.so.%{libopencv_photo_soname}*

#--------------------------------------------------------------------------------

%define libopencv_stitching_soname 2.4
%define libopencv_stitching %mklibname opencv_stitching %{libopencv_stitching_soname}

%package -n %{libopencv_stitching}
Summary:	OpenCV Stitching Pipeline

Group:		System/Libraries

%description -n %{libopencv_stitching}
This figure illustrates the stitching module pipeline implemented in the
:ocv:class:`Stitcher` class. Using that class it's possible to configure/remove
some steps, i.e. adjust the stitching pipeline according to the particular
needs. All building blocks from the pipeline are available in the ``detail``
namespace, one can combine and use them separately.

%files -n %{libopencv_stitching}
%{_libdir}/libopencv_stitching.so.%{libopencv_stitching_soname}*

#--------------------------------------------------------------------------------

%define libopencv_videostab_soname 2.4
%define libopencv_videostab %mklibname opencv_videostab %{libopencv_videostab_soname}

%package -n %{libopencv_videostab}
Summary:	OpenCV Video stabilization

Group:		System/Libraries

%description -n %{libopencv_videostab}
OpenCV Video stabilization module.

%files -n %{libopencv_videostab}
%{_libdir}/libopencv_videostab.so.%{libopencv_videostab_soname}*

#--------------------------------------------------------------------------------

%package	devel
Summary:	OpenCV development files

Group:		Development/C
Provides:	opencv-devel = %{EVRD}
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_ts} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
Requires:	%{libopencv_ml} = %{EVRD}
Requires:	%{libopencv_ocl} = %{EVRD}
Requires:	%{libopencv_flann} = %{EVRD}
Requires:	%{libopencv_calib3d} = %{EVRD}
Requires:	%{libopencv_features2d} = %{EVRD}
Requires:	%{libopencv_superres} = %{EVRD}
Requires:	%{libopencv_video} = %{EVRD}
Requires:	%{libopencv_objdetect} = %{EVRD}
Requires:	%{libopencv_contrib} = %{EVRD}
Requires:	%{libopencv_legacy} = %{EVRD}
Requires:	%{libopencv_nonfree} = %{EVRD}
Requires:	%{libopencv_photo} = %{EVRD}
Requires:	%{libopencv_stitching} = %{EVRD}
Requires:	%{libopencv_videostab} = %{EVRD}
%if %{with java}
Requires:	%{name}-java = %{EVRD}
%endif
Requires:	python-%{name} = %{EVRD}

%description	devel
OpenCV development files.

%files		devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%dir %{_libdir}/OpenCV
%{_libdir}/OpenCV/*.cmake

#--------------------------------------------------------------------------------
%package -n	python-opencv
Summary:	OpenCV Python bindings

Group:		Development/Python

%description -n	python-opencv
OpenCV python bindings.

%files -n	python-opencv
%{py_platsitedir}/*

#--------------------------------------------------------------------------------

%package	doc
Summary:	OpenCV docs

Group:		Books/Computer books
BuildArch:	noarch

%description	doc
OpenCV docs.

%files	doc
%{_datadir}/OpenCV/doc

#--------------------------------------------------------------------------------

%package	samples
Summary:	OpenCV sample code

Group:		Books/Computer books

%description	samples
OpenCV sample code.

%files		samples
%{_bindir}/opencv_createsamples
%{_bindir}/opencv_haartraining
%{_bindir}/opencv_performance
%{_bindir}/opencv_traincascade
%dir %{_datadir}/OpenCV
%{_datadir}/OpenCV/samples
%{_datadir}/OpenCV/haarcascades
%{_datadir}/OpenCV/lbpcascades
#--------------------------------------------------------------------------------

%if %{with java}
%package	java
Summary:	Java bindings for OpenCV

Group:		Sciences/Computer science

%description	java
Java bindings for OpenCV

%files		java
%{_datadir}/OpenCV/java
%endif

%prep
%setup -q
%apply_patches

# Fix source files having executable permissions
find . -name "*.cpp" -o -name "*.hpp" -o -name "*.h" |xargs chmod 0644
# And scripts lacking them
find . -name "*.sh" |xargs chmod 0755

sed -i 's|\r||g'  samples/c/adaptiveskindetector.cpp

%build
%cmake \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_opencv_gpu:BOOL=OFF \
	-DINSTALL_C_EXAMPLES:BOOL=ON \
	-DINSTALL_PYTHON_EXAMPLES:BOOL=ON \
	-DINSTALL_OCTAVE_EXAMPLES:BOOL=ON \
	-DPYTHON_PACKAGES_PATH=%{py_platsitedir} \
	-DWITH_FFMPEG:BOOL=ON \
	-DWITH_OPENGL:BOOL=ON \
	-DWITH_TIFF:BOOL=ON \
	-DWITH_QT:BOOL=ON \
	-DWITH_CUDA:BOOL=OFF \
	-DENABLE_SSE3=0
%make VERBOSE=1

%install
%makeinstall_std -C build

# Requesting libraries by filename is just bogus...
sed -i -e 's,\${exec_prefix}/%{_lib}/lib,-l,g;s,\.so,,g;s,\.a,,g' %{buildroot}%{_libdir}/pkgconfig/opencv.pc


