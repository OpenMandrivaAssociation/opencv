%bcond_without java
%bcond_without python

# Temporarily until we can build with clang again
%define _disable_lto 1

# (tpg) libomp is already in llvm-devel
%global __requires_exclude 'devel\\(libomp.*\\)'

# Python2 bits are harmful
%global _python_bytecompile_build 0

%define major %(echo %{version} |cut -d. -f1-2)
%define major2 %(echo %{version} |cut -d. -f1)%(echo %{version} |cut -d. -f2)

# (tpg) enable PGO build
%ifnarch riscv64 %{armx}
%bcond_with pgo
%else
%bcond_with pgo
%endif

Summary:	Open Source Computer Vision library
Name:		opencv
Version:	4.10.0
Release:	7
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
BuildRequires:	pkgconfig(libglog)
BuildRequires:	pkgconfig(gflags)
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
BuildRequires:	jdk-current
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

%define libraries core imgcodecs imgproc highgui ml shape flann calib3d features2d superres video objdetect videoio photo stitching wechat_qrcode videostab aruco bgsegm bioinspired ccalib cvv datasets dnn dnn_objdetect dpm face freetype fuzzy hdf hfs img_hash line_descriptor optflow phase_unwrapping plot reg rgbd saliency stereo structured_light surface_matching text tracking viz xfeatures2d ximgproc xobjdetect xphoto alphamat dnn_superres gapi intensity_transform quality rapid mcc ovis sfm signal
%define extra_files_quality %{_datadir}/opencv4/quality

# Removed in 4.10: barcode

%{expand:%(
S[core]="OpenCV core library (basic structures, arithmetics, linear algebra)"
S[barcode]="OpenCV barcode recognition module supporting the EAN13 encoding method"
S[imgproc]="OpenCV image processing library"
D[imgproc]="${S[imgproc]}
(filter, Gaussian blur, erode, dilate, resize, remap, etc.)"
S[highgui]="OpenCV GUI and image/video I/O library"
S[ml]="OpenCV machine learning model library"
D[ml]="OpenCV statistical machine learning models
(SVM, decision trees, boosting, etc.)"
S[flann]="OpenCV FLANN (Fast Library for Approximate Nearest Neighbors) library"
S[calib3d]="OpenCV camera calibration library"
D[calib3d]="OpenCV library for camera calibration, stereo correspondence,
and elements of 3D data processing"
S[features2d]="OpenCV 2D feature detectors"
D[features2d]="OpenCV 2D feature detectors and descriptors
(SURF, FAST, etc.)"
S[superres]="OpenCV super-resolution support"
S[video]="OpenCV motion analysis and object tracking library"
D[video]="${S[video]}
(optical flow, motion templates, background subtraction, etc.)"
S[objdetect]="OpenCV motion analysis and object tracking library"
D[objdetect]="${S[objdetect]}
(Haar and LBP face detectors, HOG people detector, etc.)"
S[videoio]="OpenCV video I/O library"
S[photo]="OpenCV photo library"
S[stitching]="OpenCV stitching pipeline"
D[stitching]="${S[stitching]}
Using this class, it's possible to configure/remove
some steps, i.e. adjust the stitching pipeline according
to the particular needs. All building blocks from the
pipeline are available in the 'detail' namespace, one can
combine and use them separately"
S[wechat_qrcode]="OpenCV WeChat QR code detector module"
D[wechat_qrcode]="${S[wechat_qrcode]}
WeChat QRCode includes two CNN-based models: A object detection model
and a super resolution model. Object detection model is applied to
etect QRCode with the bounding box. super resolution model is applied
to zoom in QRCode when it is small."
S[videostab]="OpenCV video stabilization module"
for i in %{libraries}; do
	S="${S[$i]}"
	[ -z "$S" ] && S="The OpenCV $i library"
	D="${D[$i]}"
	[ -z "$D" ] && D=$S
	cat <<EOF
%%package -n %{mklibname opencv_${i}}
Summary:	$S
Group:		System/Libraries
%%rename	%%{mklibname opencv_${i} 4.7}
Obsoletes:	%%{mklibname opencv_${i} 4.6} < %{EVRD}

%%description -n %{mklibname opencv_${i}}
$D

%%files -n %{mklibname opencv_${i}}
%optional %{_libdir}/libopencv_${i}.so.%{major}*
%optional %{_libdir}/libopencv_${i}.so.%{major2}
%%{?extra_files_${i}:%%{extra_files_${i}}}
EOF
done
)}

%package	devel
Summary:	OpenCV development files
Group:		Development/C
Provides:	opencv-devel = %{EVRD}
%{expand:%(
for i in %{libraries}; do
	echo "Requires: %%{mklibname opencv_${i}} = %{EVRD}"
done
)}
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
# For now this is only static libraries, so we should
# own the directory here too
%dir %{_libdir}/opencv4
%dir %{_libdir}/opencv4/3rdparty
%{_libdir}/opencv4/3rdparty/*.a

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
%if %{with java}
. %{_sysconfdir}/profile.d/90java.sh
%endif

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
