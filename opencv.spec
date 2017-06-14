%ifnarch %{armx}
%bcond_without	java
%endif
%bcond_without	python

# (tpg) libomp is already in llvm-devel
%define __noautoreq 'devel\\(libomp.*\\)'

%define _disable_ld_no_undefined 1

Summary:	Open Source Computer Vision library
Name:		opencv
Version:	3.2.0
Release:	3
License:	GPLv2+
Group:		Sciences/Computer science
Url:		http://opencv.org/
Source0:	https://github.com/Itseez/opencv/archive/%{name}-%{version}.tar.gz
Source1:	https://github.com/opencv/opencv_contrib/%{name}_contrib-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

Patch1:         opencv-3.2.0-cmake_paths.patch

#Patch2:		opencv-pkgcmake2.patch
#Patch5:		opencv-2.4.8-ts_static.patch
Patch10:	opencv-3.2.0-fix-freetype-module.patch
BuildRequires:	cmake
BuildRequires:	jpeg-devel
BuildRequires:	%{_lib}opencl-devel
BuildRequires:	protobuf-compiler
BuildRequires:	protobuf-devel
%if %{with python}
BuildRequires:	python-numpy-devel
BuildRequires:	python2-numpy-devel
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
%endif
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(lapack)
BuildRequires:	pkgconfig(tesseract)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	hdf5-devel
%if %{with java}
# Java bindings
BuildRequires:	java-devel
BuildRequires:	ant
%endif
# Qt 5.x module
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Widgets)
# Documentation generation
#BuildRequires:	python-sphinx
#BuildRequires:	latex2html

%description
OpenCV (Open Source Computer Vision) is a library of programming
functions for real time computer vision.

#--------------------------------------------------------------------------------

%define libopencv_core_soname 3.2
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

%define libopencv_imgcodecs_soname 3.2
%define libopencv_imgcodecs %mklibname opencv_imgcodecs %{libopencv_imgcodecs_soname}
%define wrongts %mklibname opencv_imgcodecs 2

%package -n	%{libopencv_imgcodecs}
Summary:	OpenCV image codecs library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}
%rename		%{wrongts}

%description -n	%{libopencv_imgcodecs}
OpenCV image codecs library.

#--------------------------------------------------------------------------------

%files -n      %{libopencv_imgcodecs}
%{_libdir}/libopencv_imgcodecs.so.%{libopencv_imgcodecs_soname}*

%define libopencv_imgproc_soname 3.2
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

%define libopencv_highgui_soname 3.2
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

%define libopencv_ml_soname 3.2
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

%define libopencv_shape_soname 3.2
%define libopencv_shape %mklibname opencv_shape %{libopencv_shape_soname}

%package -n	%{libopencv_shape}
Summary:	OpenCV shape library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_shape}
OpenCV shape library.

%files -n	%{libopencv_shape}
%{_libdir}/libopencv_shape.so.%{libopencv_shape_soname}*

#--------------------------------------------------------------------------------

%define libopencv_flann_soname 3.2
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

%define libopencv_calib3d_soname 3.2
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

%define libopencv_features2d_soname 3.2
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

%define libopencv_superres_soname 3.2
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

%define libopencv_video_soname 3.2
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

%define libopencv_objdetect_soname 3.2
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

%define libopencv_videoio_soname 3.2
%define libopencv_videoio %mklibname opencv_videoio %{libopencv_videoio_soname}

%package -n	%{libopencv_videoio}
Summary:	OpenCV videoio library
Group:		System/Libraries
Requires:	%{libopencv_core} = %{EVRD}

%description -n	%{libopencv_videoio}
OpenCV videoio library.

%files -n	%{libopencv_videoio}
%{_libdir}/libopencv_videoio.so.%{libopencv_videoio_soname}*

#--------------------------------------------------------------------------------

%define libopencv_photo_soname 3.2
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

%define libopencv_stitching_soname 3.2
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

%define libopencv_videostab_soname 3.2
%define libopencv_videostab %mklibname opencv_videostab %{libopencv_videostab_soname}

%package -n %{libopencv_videostab}
Summary:	OpenCV Video stabilization
Group:		System/Libraries

%description -n %{libopencv_videostab}
OpenCV Video stabilization module.

%files -n %{libopencv_videostab}
%{_libdir}/libopencv_videostab.so.%{libopencv_videostab_soname}*

#--------------------------------------------------------------------------------

%libpackage opencv_aruco 3.2
%libpackage opencv_bgsegm 3.2
%libpackage opencv_bioinspired 3.2
%libpackage opencv_ccalib 3.2
%libpackage opencv_cvv 3.2
%libpackage opencv_datasets 3.2
%libpackage opencv_dnn 3.2
%libpackage opencv_dpm 3.2
%libpackage opencv_face 3.2
%libpackage opencv_freetype 3.2
%libpackage opencv_fuzzy 3.2
%libpackage opencv_hdf 3.2
%libpackage opencv_line_descriptor 3.2
%libpackage opencv_optflow 3.2
%libpackage opencv_phase_unwrapping 3.2
%libpackage opencv_plot 3.2
%libpackage opencv_reg 3.2
%libpackage opencv_rgbd 3.2
%libpackage opencv_saliency 3.2
%libpackage opencv_stereo 3.2
%libpackage opencv_structured_light 3.2
%libpackage opencv_surface_matching 3.2
%libpackage opencv_text 3.2
%libpackage opencv_tracking 3.2
%libpackage opencv_xfeatures2d 3.2
%libpackage opencv_ximgproc 3.2
%libpackage opencv_xobjdetect 3.2
%libpackage opencv_xphoto 3.2

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
Requires:	%{mklibname opencv_aruco 3.2} = %{EVRD}
Requires:	%{mklibname opencv_bgsegm 3.2} = %{EVRD}
Requires:	%{mklibname opencv_bioinspired 3.2} = %{EVRD}
Requires:	%{mklibname opencv_ccalib 3.2} = %{EVRD}
Requires:	%{mklibname opencv_cvv 3.2} = %{EVRD}
Requires:	%{mklibname opencv_datasets 3.2} = %{EVRD}
Requires:	%{mklibname opencv_dnn 3.2} = %{EVRD}
Requires:	%{mklibname opencv_dpm 3.2} = %{EVRD}
Requires:	%{mklibname opencv_face 3.2} = %{EVRD}
Requires:	%{mklibname opencv_freetype 3.2} = %{EVRD}
Requires:	%{mklibname opencv_fuzzy 3.2} = %{EVRD}
Requires:	%{mklibname opencv_hdf 3.2} = %{EVRD}
Requires:	%{mklibname opencv_line_descriptor 3.2} = %{EVRD}
Requires:	%{mklibname opencv_optflow 3.2} = %{EVRD}
Requires:	%{mklibname opencv_phase_unwrapping 3.2} = %{EVRD}
Requires:	%{mklibname opencv_plot 3.2} = %{EVRD}
Requires:	%{mklibname opencv_reg 3.2} = %{EVRD}
Requires:	%{mklibname opencv_rgbd 3.2} = %{EVRD}
Requires:	%{mklibname opencv_saliency 3.2} = %{EVRD}
Requires:	%{mklibname opencv_stereo 3.2} = %{EVRD}
Requires:	%{mklibname opencv_structured_light 3.2} = %{EVRD}
Requires:	%{mklibname opencv_surface_matching 3.2} = %{EVRD}
Requires:	%{mklibname opencv_text 3.2} = %{EVRD}
Requires:	%{mklibname opencv_tracking 3.2} = %{EVRD}
Requires:	%{mklibname opencv_xfeatures2d 3.2} = %{EVRD}
Requires:	%{mklibname opencv_ximgproc 3.2} = %{EVRD}
Requires:	%{mklibname opencv_xobjdetect 3.2} = %{EVRD}
Requires:	%{mklibname opencv_xphoto 3.2} = %{EVRD}
%if %{with java}
Requires:	%{name}-java = %{EVRD}
%endif
%if %{with python}
Suggests:	python2-%{name} = %{EVRD}
Requires:	python-%{name} = %{EVRD}
%endif

%description	devel
OpenCV development files.

%files		devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%dir %{_libdir}/OpenCV
%{_libdir}/OpenCV/*.cmake

%if %{with python}
#--------------------------------------------------------------------------------
%package -n	python-opencv
Summary:	OpenCV Python bindings
Group:		Development/Python

%description -n	python-opencv
OpenCV python bindings.

%files -n	python-opencv
%{py_platsitedir}/*

#--------------------------------------------------------------------------------
%package -n	python2-opencv
Summary:	OpenCV Python 2.x bindings
Group:		Development/Python

%description -n	python2-opencv
OpenCV python 2.x bindings.

%files -n	python2-opencv
%{py2_platsitedir}/*
%endif

#--------------------------------------------------------------------------------

#%package	doc
#Summary:	OpenCV docs
#Group:		Books/Computer books
#BuildArch:	noarch

#%description	doc
#OpenCV docs.

#%files	doc
#%{_datadir}/OpenCV/doc

#--------------------------------------------------------------------------------

%package	samples
Summary:	OpenCV sample code
Group:		Books/Computer books

%description	samples
OpenCV sample code.

%files		samples
%{_bindir}/opencv_annotation
%{_bindir}/opencv_createsamples
%{_bindir}/opencv_traincascade
%{_bindir}/opencv_visualisation
%{_bindir}/opencv_version
%{_bindir}/opencv_interactive-calibration
%{_bindir}/opencv_waldboost_detector
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
Java bindings for OpenCV.

%files		java
%{_datadir}/OpenCV/java
%endif

%prep
%setup -q -a 1
%apply_patches

# Fix source files having executable permissions
find . -name "*.cpp" -o -name "*.hpp" -o -name "*.h" |xargs chmod 0644
# And scripts lacking them
find . -name "*.sh" |xargs chmod 0755

# remove bundled stuff
rm -rf 3rdparty
sed -i \
	-e '/add_subdirectory(3rdparty)/ d' \
	CMakeLists.txt

# rebuild protobuf files with our version of protobuf
find . -name "*.proto" |while read r; do
	dir=$(dirname $(realpath $r))
	out=${dir/src/misc}
	cd $dir
	protoc --cpp_out=$out $(basename $r)
	cd -
done

%build
%ifarch aarch64
# As of 3.2.0, clang 4.0.1, OpenCV uses NEON intrinsics
# understood only by gcc (v_float16x4 on 64bit)
export CC=gcc
export CXX=g++
%endif

%cmake \
	-DBUILD_EXAMPLES:BOOL=ON \
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
	-DWITH_QT:BOOL=ON \
	-DWITH_CUDA:BOOL=OFF \
	-DWITH_VTK:BOOL=ON \
	-DWITH_OPENMP:BOOL=ON \
	-DENABLE_FAST_MATH:BOOL=ON \
	-DBUILD_PROTOBUF:BOOL=OFF \
%ifnarch x86_64
	-DENABLE_SSE=OFF \
	-DENABLE_SSE2=OFF \
	-DENABLE_SSE3=OFF \
%endif
	-DENABLE_SSSE3=0 \
	-DENABLE_SSE41=0 \
	-DENABLE_SSE42=0 \
	-DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-%{version}/modules

%make VERBOSE=1

%install
%makeinstall_std -C build

# Requesting libraries by filename is just bogus...
sed -i -e 's,\${exec_prefix}/%{_lib}/lib,-l,g;s,\.so,,g;s,\.a,,g' %{buildroot}%{_libdir}/pkgconfig/opencv.pc
