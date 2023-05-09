%define _empty_manifest_terminate_build 0
%ifnarch %{armx}
%bcond_without java
%endif
%bcond_without python

# Temporarily until we can build with clang again
%define _disable_lto 1

# (tpg) libomp is already in llvm-devel
%global __requires_exclude 'devel\\(libomp.*\\)'

# Python2 bits are harmful
%global _python_bytecompile_build 0

%define major %(echo %{version} |cut -d. -f1-2)
%define major2 %(echo %{version} |cut -d. -f1)0%(echo %{version} |cut -d. -f2)

# (tpg) enable PGO build
%ifnarch riscv64 %{armx}
%bcond_with pgo
%else
%bcond_with pgo
%endif

Summary:	Open Source Computer Vision library
Name:		opencv
# When updating, please check if patch 12 is still needed
Version:	4.7.0
Release:	4
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://opencv.org/
Source0:	https://github.com/opencv/opencv/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/opencv/opencv_contrib/archive/%{version}/%{name}_contrib-%{version}.tar.gz
Source2:	https://github.com/opencv/ade/archive/v0.1.2a.zip
# TODO Keep in sync with versions downloaded by opencv_contrib/modules/xfeatures2d/cmake/download_boostdesc.cmake
Source3:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_bgm.i
Source4:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_bgm_bi.i
Source5:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_bgm_hd.i
Source6:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_binboost_064.i
Source7:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_binboost_128.i
Source8:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_binboost_256.i
Source9:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/34e4206aef44d50e6bbcd0ab06354b52e7466d26/boostdesc_lbgm.i
Source14:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/8afa57abc8229d611c4937165d20e2a2d9fc5a12/face_landmark_model.dat
Source15:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/b2bfc75f6aea5b1f834ff0f0b865a7c18ff1459f/res10_300x300_ssd_iter_140000.caffemodel
Source16:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_48.i
Source17:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_64.i
Source18:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_80.i
Source19:	https://raw.githubusercontent.com/opencv/opencv_3rdparty/fccf7cd6a4b12079f73bbfb21745f9babcd4eb1d/vgg_generated_120.i
Source100:	%{name}.rpmlintrc

Patch0:		opencv-4.5.5-skip-broken-VTK-check.patch
Patch1:		opencv-4.5.5-GL-linkage.patch
Patch2:		opencv-4.7.0-compile.patch
#Patch2:		opencv-4.6.0-missing-includes.patch
#Patch3:		opencv-4.5.5-hfs-workaround-clang14-bug.patch
#Patch4:		opencv-4.6.0-protobuf-22.1.patch
#Patch5:		opencv-4.6.0-libstdc++13.patch
#Patch6:		opencv-no-downloads-at-buildtime.patch
#Patch1:		opencv-3.4.0-x32-sse.patch
#Patch2:		opencv-3.4-libdir.patch
#Patch3:		opencv-3.4.0-float-vs-float_t.patch
#Patch6:		opencv-pkgcmake2.patch
#Patch7:		opencv-2.4.8-ts_static.patch
#Patch11:	opencv-3.4.0-python3.7.patch
# https://github.com/opencv/opencv/issues/17952
#Patch103:	fix-call-to-implicitly-deleted-default-constructor-of-cv-gimpl-op.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(OpenCL)
BuildRequires:	protobuf-compiler
BuildRequires:	pkgconfig(protobuf)
%if %{with python}
BuildRequires:	python3-numpy-devel >= 1.16.5
BuildRequires:	pkgconfig(python3)
%endif
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(freeglut)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(atlas)
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(tesseract)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	cmake(vtk)
BuildRequires:	cmake(Verdict)
BuildRequires:	cmake(jsoncpp)
BuildRequires:	vtk-python
BuildRequires:	hdf5-devel
BuildRequires:	mesa-opencl-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	cmake(double-conversion)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xt)
%if %{with java}
# Java bindings
BuildRequires:	java-devel java-openjdk java-openjdk-headless
BuildRequires:	ant
%endif
# Qt 6.x module
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	qt6-cmake
BuildRequires:	qmake-qt6
# OVIS module
BuildRequires:	pkgconfig(OGRE) ogre ogre-samples
# Documentation generation
#BuildRequires:	python-sphinx
#BuildRequires:	latex2html

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions for real time computer vision.

#--------------------------------------------------------------------------------

%define libopencv_core_soname %{major}
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
%{_libdir}/libopencv_core.so.%{major2}

#--------------------------------------------------------------------------------
	
%define libopencv_barcode_soname %{major}
%define libopencv_barcode %mklibname opencv_barcode %{libopencv_barcode_soname}

%package -n %{libopencv_barcode}
Summary: OpenCV bar code recognition module
Group: System/Libraries

%description -n %{libopencv_barcode}
Bar code detection and decoding module supporting the EAN13 encoding method.

%files -n %{libopencv_barcode}
%{_libdir}/libopencv_barcode.so.%{libopencv_barcode_soname}{,.*}
%{_libdir}/libopencv_barcode.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_imgcodecs_soname %{major}
%define libopencv_imgcodecs %mklibname opencv_imgcodecs %{libopencv_imgcodecs_soname}
%define wrongts %mklibname opencv_imgcodecs 2

%package -n	%{libopencv_imgcodecs}
Summary:	OpenCV image codecs library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
%rename		%{wrongts}

%description -n	%{libopencv_imgcodecs}
OpenCV image codecs library.

%files -n      %{libopencv_imgcodecs}
%{_libdir}/libopencv_imgcodecs.so.%{libopencv_imgcodecs_soname}*
%{_libdir}/libopencv_imgcodecs.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_imgproc_soname %{major}
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
%{_libdir}/libopencv_imgproc.so.%{major2}*

#--------------------------------------------------------------------------------

%define libopencv_highgui_soname %{major}
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
%{_libdir}/libopencv_highgui.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_ml_soname %{major}
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
%{_libdir}/libopencv_ml.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_shape_soname %{major}
%define libopencv_shape %mklibname opencv_shape %{libopencv_shape_soname}

%package -n	%{libopencv_shape}
Summary:	OpenCV shape library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_shape}
OpenCV shape library.

%files -n	%{libopencv_shape}
%{_libdir}/libopencv_shape.so.%{libopencv_shape_soname}*
%{_libdir}/libopencv_shape.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_flann_soname %{major}
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
%{_libdir}/libopencv_flann.so.%{major2}*

#--------------------------------------------------------------------------------

%define libopencv_calib3d_soname %{major}
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
%{_libdir}/libopencv_calib3d.so.%{major2}*

#--------------------------------------------------------------------------------

%define libopencv_features2d_soname %{major}
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
%{_libdir}/libopencv_features2d.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_superres_soname %{major}
%define libopencv_superres %mklibname opencv_superres %{libopencv_superres_soname}

%package -n	%{libopencv_superres}
Summary:	OpenCV super-resolution support
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_superres}
Super-resolution support for OpenCV.

%files -n	%{libopencv_superres}
%{_libdir}/libopencv_superres.so.%{libopencv_superres_soname}*
%{_libdir}/libopencv_superres.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_video_soname %{major}
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
%{_libdir}/libopencv_video.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_objdetect_soname %{major}
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
%{_libdir}/libopencv_objdetect.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_videoio_soname %{major}
%define libopencv_videoio %mklibname opencv_videoio %{libopencv_videoio_soname}

%package -n	%{libopencv_videoio}
Summary:	OpenCV videoio library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_videoio}
OpenCV videoio library.

%files -n	%{libopencv_videoio}
%{_libdir}/libopencv_videoio.so.%{libopencv_videoio_soname}*
%{_libdir}/libopencv_videoio.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_photo_soname %{major}
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
%{_libdir}/libopencv_photo.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_stitching_soname %{major}
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
%{_libdir}/libopencv_stitching.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_wechat_qrcode_soname %{major}
%define libopencv_wechat_qrcode %mklibname opencv_wechat_qrcode %{libopencv_wechat_qrcode_soname}

%package -n %{libopencv_wechat_qrcode}
Summary: OpenCV WeChat QR code detector module
Group: System/Libraries

%description -n %{libopencv_wechat_qrcode}
WeChat QRCode includes two CNN-based models: A object detection model
and a super resolution model. Object detection model is applied to
etect QRCode with the bounding box. super resolution model is applied
to zoom in QRCode when it is small.
	
%files -n %{libopencv_wechat_qrcode}
%{_libdir}/libopencv_wechat_qrcode.so.%{libopencv_wechat_qrcode_soname}{,.*}
%{_libdir}/libopencv_wechat_qrcode.so.%{major2}

#--------------------------------------------------------------------------------

%define libopencv_videostab_soname %{major}
%define libopencv_videostab %mklibname opencv_videostab %{libopencv_videostab_soname}

%package -n %{libopencv_videostab}
Summary:	OpenCV Video stabilization
Group:		System/Libraries

%description -n %{libopencv_videostab}
OpenCV Video stabilization module.

%files -n %{libopencv_videostab}
%{_libdir}/libopencv_videostab.so.%{libopencv_videostab_soname}*
%{_libdir}/libopencv_videostab.so.%{major2}

#--------------------------------------------------------------------------------
%define cvlibpackage()\
%%package -n %{expand:%%mklibname %{1} %{2} %{?3:%{3}}}\
Summary: The %{1} library, a part of %{name}\
Group: System/Libraries\
%%description -n %{expand:%%mklibname %{1} %{2} %{?3:%{3}}}\
The %{1} library, a part of %{name}\
%%files -n %{expand:%%mklibname %{1} %{2} %{?3:%{3}}}\
%{_libdir}/lib%{1}%{?3:-%{2}}.so.%{?3:%{3}}%{?!3:%{2}}*\
%{_libdir}/lib%{1}%{?3:-%{2}}.so.%{major2}\
%{nil}


%cvlibpackage opencv_aruco %{major}
%cvlibpackage opencv_bgsegm %{major}
%cvlibpackage opencv_bioinspired %{major}
%cvlibpackage opencv_ccalib %{major}
%cvlibpackage opencv_cvv %{major}
%cvlibpackage opencv_datasets %{major}
%cvlibpackage opencv_dnn %{major}
%cvlibpackage opencv_dnn_objdetect %{major}
%cvlibpackage opencv_dpm %{major}
%cvlibpackage opencv_face %{major}
%cvlibpackage opencv_freetype %{major}
%cvlibpackage opencv_fuzzy %{major}
%cvlibpackage opencv_hdf %{major}
%cvlibpackage opencv_hfs %{major}
%cvlibpackage opencv_img_hash %{major}
%cvlibpackage opencv_line_descriptor %{major}
%cvlibpackage opencv_optflow %{major}
%cvlibpackage opencv_phase_unwrapping %{major}
%cvlibpackage opencv_plot %{major}
%cvlibpackage opencv_reg %{major}
%cvlibpackage opencv_rgbd %{major}
%cvlibpackage opencv_saliency %{major}
%cvlibpackage opencv_stereo %{major}
%cvlibpackage opencv_structured_light %{major}
%cvlibpackage opencv_surface_matching %{major}
%cvlibpackage opencv_text %{major}
%cvlibpackage opencv_tracking %{major}
%cvlibpackage opencv_viz %{major}
%cvlibpackage opencv_xfeatures2d %{major}
%cvlibpackage opencv_ximgproc %{major}
%cvlibpackage opencv_xobjdetect %{major}
%cvlibpackage opencv_xphoto %{major}
# Added in 4.x
%cvlibpackage opencv_alphamat %{major}
%cvlibpackage opencv_dnn_superres %{major}
%cvlibpackage opencv_gapi %{major}
%cvlibpackage opencv_intensity_transform %{major}
%cvlibpackage opencv_quality %{major}
%{_datadir}/opencv4/quality
%cvlibpackage opencv_rapid %{major}
# Added in 4.5
%cvlibpackage opencv_mcc %{major}
%cvlibpackage opencv_ovis %{major}

%package	devel
Summary:	OpenCV development files
Group:		Development/C
Provides:	opencv-devel = %{EVRD}
Requires:	%{libopencv_core} = %{EVRD}
Requires:	%{libopencv_imgcodecs} = %{EVRD}
Requires:	%{libopencv_imgproc} = %{EVRD}
Requires:	%{libopencv_highgui} = %{EVRD}
Requires:	%{libopencv_ml} = %{EVRD}
Requires:	%{libopencv_shape} = %{EVRD}
Requires:	%{libopencv_flann} = %{EVRD}
Requires:	%{libopencv_calib3d} = %{EVRD}
Requires:	%{libopencv_features2d} = %{EVRD}
Requires:	%{libopencv_superres} = %{EVRD}
Requires:	%{libopencv_video} = %{EVRD}
Requires:	%{libopencv_objdetect} = %{EVRD}
Requires:	%{libopencv_videoio} = %{EVRD}
Requires:	%{libopencv_photo} = %{EVRD}
Requires:	%{libopencv_stitching} = %{EVRD}
Requires:	%{libopencv_videostab} = %{EVRD}
Requires:	%{mklibname opencv_aruco %{major}} = %{EVRD}
Requires: 	%{libopencv_barcode} = %{EVRD}
Requires:	%{mklibname opencv_bgsegm %{major}} = %{EVRD}
Requires:	%{mklibname opencv_bioinspired %{major}} = %{EVRD}
Requires:	%{mklibname opencv_ccalib %{major}} = %{EVRD}
Requires:	%{mklibname opencv_cvv %{major}} = %{EVRD}
Requires:	%{mklibname opencv_datasets %{major}} = %{EVRD}
Requires:	%{mklibname opencv_dnn %{major}} = %{EVRD}
Requires:	%{mklibname opencv_dnn_objdetect %{major}} = %{EVRD}
Requires:	%{mklibname opencv_dpm %{major}} = %{EVRD}
Requires:	%{mklibname opencv_face %{major}} = %{EVRD}
Requires:	%{mklibname opencv_freetype %{major}} = %{EVRD}
Requires:	%{mklibname opencv_fuzzy %{major}} = %{EVRD}
Requires:	%{mklibname opencv_hdf %{major}} = %{EVRD}
Requires:	%{mklibname opencv_hfs %{major}} = %{EVRD}
Requires:	%{mklibname opencv_img_hash %{major}} = %{EVRD}
Requires:	%{mklibname opencv_line_descriptor %{major}} = %{EVRD}
Requires:	%{mklibname opencv_optflow %{major}} = %{EVRD}
Requires:	%{mklibname opencv_phase_unwrapping %{major}} = %{EVRD}
Requires:	%{mklibname opencv_plot %{major}} = %{EVRD}
Requires:	%{mklibname opencv_reg %{major}} = %{EVRD}
Requires:	%{mklibname opencv_rgbd %{major}} = %{EVRD}
Requires:	%{mklibname opencv_saliency %{major}} = %{EVRD}
Requires:	%{mklibname opencv_stereo %{major}} = %{EVRD}
Requires:	%{mklibname opencv_structured_light %{major}} = %{EVRD}
Requires:	%{mklibname opencv_surface_matching %{major}} = %{EVRD}
Requires:	%{mklibname opencv_text %{major}} = %{EVRD}
Requires:	%{mklibname opencv_tracking %{major}} = %{EVRD}
Requires: 	%{libopencv_wechat_qrcode} = %{EVRD}
Requires:	%{mklibname opencv_viz %{major}} = %{EVRD}
Requires:	%{mklibname opencv_xfeatures2d %{major}} = %{EVRD}
Requires:	%{mklibname opencv_ximgproc %{major}} = %{EVRD}
Requires:	%{mklibname opencv_xobjdetect %{major}} = %{EVRD}
Requires:	%{mklibname opencv_xphoto %{major}} = %{EVRD}
Requires:	%{mklibname opencv_alphamat %{major}} = %{EVRD}
Requires:	%{mklibname opencv_dnn_superres %{major}} = %{EVRD}
Requires:	%{mklibname opencv_gapi %{major}} = %{EVRD}
Requires:	%{mklibname opencv_intensity_transform %{major}} = %{EVRD}
Requires:	%{mklibname opencv_quality %{major}} = %{EVRD}
Requires:	%{mklibname opencv_rapid %{major}} = %{EVRD}
Requires:	%{mklibname opencv_mcc %{major}} = %{EVRD}
Requires:	%{mklibname opencv_ovis %{major}} = %{EVRD}
%if %{with java}
Requires:	%{name}-java = %{EVRD}
%endif
%if %{with python}
Requires:	python-%{name} = %{EVRD}
%endif

%description	devel
OpenCV development files.

%files		devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/cmake/opencv4
%{_libdir}/pkgconfig/opencv4.pc
%dir %{_datadir}/opencv4
%{_datadir}/opencv4/valgrind.supp
%{_datadir}/opencv4/valgrind_3rdparty.supp

%if %{with python}
#--------------------------------------------------------------------------------
%package -n	python-opencv
Summary:	OpenCV Python bindings
Group:		Development/Python

%description -n	python-opencv
OpenCV python bindings.

%files -n	python-opencv
%{_bindir}/setup_vars_opencv4.sh
%ifnarch %{ix86}
%{py_puresitedir}/*
%else
%{python_sitelib}/cv2/*
%endif
%endif

#--------------------------------------------------------------------------------

#%package	doc
#Summary:	OpenCV docs
#Group:		Books/Computer books
#BuildArch:	noarch

#%description	doc
#OpenCV docs.

#%files	doc
#{_datadir}/OpenCV/doc

#--------------------------------------------------------------------------------

%package	samples
Summary:	OpenCV sample code
Group:		Books/Computer books

%description	samples
OpenCV sample code.

%files		samples
%{_bindir}/opencv_annotation
%{_bindir}/opencv_visualisation
%{_bindir}/opencv_version
%{_bindir}/opencv_interactive-calibration
%{_bindir}/opencv_waldboost_detector
%{_bindir}/opencv_model_diagnostics
%{_datadir}/opencv4/samples
%{_datadir}/opencv4/haarcascades
%{_datadir}/opencv4/lbpcascades
#--------------------------------------------------------------------------------

%if %{with java}
%package	java
Summary:	Java bindings for OpenCV
Group:		Sciences/Computer science

%description	java
Java bindings for OpenCV.

%files		java
%{_datadir}/java/opencv4
%endif

%prep
# Intentionally not using %%autosetup so we
# can use %%autopatch later, when additional
# sources have been unpacked
%setup -q -a 1

#patch12 -p1
#patch103 -p1
#cd %{name}_contrib-%{version}
#patch101 -p1
#cd ..

mkdir -p build/downloads/xfeatures2d \
	 build/3rdparty/ade build/.cache/ade \
         build/share/OpenCV/testdata/cv/face/ \
         samples/dnn/face_detector/
cp %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} \
   %{S:9} %{S:16} %{S:17} %{S:18} %{S:19} \
   build/downloads/xfeatures2d/
cp %{S:14} \
   build/share/OpenCV/testdata/cv/face/
cp %{S:15} \
   samples/dnn/face_detector/
cp %{S:2} build/.cache/ade/fa4b3e25167319cb0fa9432ef8281945-v0.1.2a.zip
cd build/3rdparty/ade
tar xf %{S:2}
cd ../../..

%if 0
mkdir -p build/3rdparty/tinydnn
cd build/3rdparty/tinydnn
tar xf %{SOURCE2}
cd -
%endif

%autopatch -p1

# Fix source files having executable permissions
find . -name "*.cpp" -o -name "*.hpp" -o -name "*.h" |xargs chmod 0644
# And scripts lacking them
find . -name "*.sh" |xargs chmod 0755

# rebuild protobuf files with our version of protobuf
find . -name "*.proto" |while read r; do
	dir=$(dirname $(realpath $r))
	out=${dir/src/misc}
	cd $dir
	protoc --cpp_out=$out $(basename $r)
	cd -
done

# Debug misbehaving VTK and Qt6 detection
sed -i -e 's, QUIET,,g' cmake/OpenCVDetectVTK.cmake cmake/OpenCVFindLibsGUI.cmake

%build
%if %{with pgo}
export LD_LIBRARY_PATH="$(pwd)/build/lib"
%cmake \
	-DCMAKE_C_FLAGS="%{optflags} -fprofile-generate" \
	-DCMAKE_C_FLAGS_RELEASE="%{optflags} -fprofile-generate" \
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -fprofile-generate" \
	-DCMAKE_CXX_FLAGS="%{optflags} -fprofile-generate" \
	-DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -fprofile-generate" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -fprofile-generate" \
	-DCMAKE_CXX_STANDARD=20 \
	-DCMAKE_EXE_LINKER_FLAGS="%{build_ldflags} -fprofile-generate" \
	-DCMAKE_SHARED_LINKER_FLAGS="%{build_ldflags} -fprofile-generate" \
	-DCMAKE_MODULE_LINKER_FLAGS="%(echo %{build_ldflags} -fprofile-generate|sed -e 's#-Wl,--no-undefined##')" \
	-DBUILD_DOCS:BOOL=OFF \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DBUILD_opencv_gpu:BOOL=OFF \
	-DINSTALL_C_EXAMPLES:BOOL=OFF \
	-DINSTALL_PYTHON_EXAMPLES:BOOL=OFF \
	-DINSTALL_OCTAVE_EXAMPLES:BOOL=OFF \
	-DPYTHON_PACKAGES_PATH=%{py2_platsitedir} \
	-DWITH_IPP=OFF \
	-DWITH_UNICAP=OFF \
	-DCMAKE_SKIP_RPATH=ON \
	-DWITH_CAROTENE=OFF \
	-DENABLE_PRECOMPILED_HEADERS:BOOL=OFF \
	-DWITH_FFMPEG:BOOL=ON \
	-DWITH_OPENGL:BOOL=ON \
	-DWITH_TIFF:BOOL=ON \
	-DWITH_QT=6 \
	-DWITH_CUDA:BOOL=OFF \
	-DWITH_VTK:BOOL=OFF \
	-DWITH_OPENMP:BOOL=ON \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DENABLE_FAST_MATH:BOOL=ON \
	-DBUILD_PROTOBUF:BOOL=OFF \
	-DBUILD_TESTS=OFF \
%ifarch %{ix86}
	-DCPU_BASELINE=SSE2 \
%endif
%ifarch x86_64
	-DCPU_BASELINE=SSE3 \
	-DCPU_DISPATCH=AVX \
%endif
%ifarch znver1
	-DCPU_BASELINE=SSE4_2 \
	-DCPU_DISPATCH=AVX,AVX2 \
%endif
	-DOPENCV_GENERATE_PKGCONFIG:BOOL=OFF \
	-DWITH_FREETYPE:BOOL=OFF \
	-DWITH_VULKAN:BOOL=OFF \
	-DWITH_VA:BOOL=OFF \
	-DWITH_VA_INTEL:BOOL=OFF \
	-G Ninja

%ninja_build

LD_PRELOAD="./lib/libopencv_imgproc.so.%{major} ./lib/libopencv_imgproc.so" bin/opencv_perf_core ||:
LD_PRELOAD="./lib/libopencv_imgcodecs.so.%{major} ./lib/libopencv_imgcodecs.so" bin/opencv_perf_imgproc ||:
LD_PRELOAD="./lib/libopencv_dnn.so.%{major} ./lib/libopencv_dnn.so" bin/opencv_perf_dnn ||:
LD_PRELOAD="./lib/libopencv_stitching.so.%{major} ./lib/libopencv_stitching.so" bin/opencv_perf_stitching ||:
LD_PRELOAD="./lib/libopencv_features2d.so.%{major} ./lib/libopencv_features2d.so" bin/opencv_perf_features2d ||:
LD_PRELOAD="./lib/libopencv_superres.so.%{major} ./lib/libopencv_superres.so" bin/opencv_perf_superres ||:
unset LD_LIBRARY_PATH
unset LLVM_PROFILE_FILE

llvm-profdata merge --output=%{name}-llvm.profdata $(find ./pgo -name "*.profraw" -type f)
PROFDATA="$(realpath %{name}-llvm.profdata)"
find . -name "*.profraw" -type f -delete
ninja -t clean
cd ..
%endif

%cmake \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DCMAKE_CXX_STANDARD=20 \
%if %{with pgo}
	-DCMAKE_C_FLAGS="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_C_FLAGS_RELEASE="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_CXX_FLAGS="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_EXE_LINKER_FLAGS="%{build_ldflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_SHARED_LINKER_FLAGS="%{build_ldflags} -fprofile-use=$PROFDATA" \
	-DCMAKE_MODULE_LINKER_FLAGS="%(echo %{build_ldflags} -fprofile-use=$PROFDATA" \|sed -e 's#-Wl,--no-undefined##')" \
%endif # " <--- workaround for vim syntax highlighting bug
	-DBUILD_opencv_gpu:BOOL=OFF \
	-DINSTALL_C_EXAMPLES:BOOL=ON \
%if %{with python}
	-DINSTALL_PYTHON_EXAMPLES:BOOL=ON \
%endif
	-DINSTALL_OCTAVE_EXAMPLES:BOOL=ON \
	-DPYTHON_PACKAGES_PATH=%{py2_platsitedir} \
	-DWITH_IPP=OFF \
	-DWITH_UNICAP=OFF \
	-DCMAKE_SKIP_RPATH=ON \
	-DWITH_CAROTENE=OFF \
	-DENABLE_PRECOMPILED_HEADERS:BOOL=OFF \
	-DWITH_FFMPEG:BOOL=ON \
	-DWITH_OPENGL:BOOL=ON \
	-DWITH_TIFF:BOOL=ON \
	-DWITH_QT=6 \
	-DWITH_CUDA:BOOL=OFF \
	-DWITH_VTK:BOOL=ON \
	-DVTK_RENDERING_BACKEND=OpenGL2 \
	-DWITH_OPENMP:BOOL=ON \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DENABLE_FAST_MATH:BOOL=ON \
	-DBUILD_PROTOBUF:BOOL=OFF \
	-DPROTOBUF_UPDATE_FILES=ON \
	-DBUILD_TESTS=OFF \
%ifarch %{ix86}
	-DCPU_BASELINE=SSE2 \
%endif
%ifarch x86_64
	-DCPU_BASELINE=SSE3 \
	-DCPU_DISPATCH=AVX \
%endif
%ifarch znver1
	-DCPU_BASELINE=SSE4_2 \
	-DCPU_DISPATCH=AVX,AVX2 \
%endif
	-DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-%{version}/modules \
	-DOPENCV_GENERATE_PKGCONFIG:BOOL=ON \
	-DWITH_FREETYPE:BOOL=ON \
	-DWITH_VULKAN:BOOL=ON \
	-DWITH_VA:BOOL=ON \
	-DWITH_VA_INTEL:BOOL=ON \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

# (tpg) remove not needed files
rm -rf %{buildroot}%{_datadir}/OpenCV/licenses
rm -rf %{buildroot}%{_datadir}/licenses
