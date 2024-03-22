#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : ksvg
Version  : 6.0.0
Release  : 2
URL      : https://download.kde.org/stable/frameworks/6.0/ksvg-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/ksvg-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/ksvg-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ksvg-data = %{version}-%{release}
Requires: ksvg-lib = %{version}-%{release}
Requires: ksvg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kirigami-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KSvg
This directory contains the classes making up KSvg, which provides rendering api for Svg files,
and support for the themes used in the Plasma Desktop.

%package data
Summary: data components for the ksvg package.
Group: Data

%description data
data components for the ksvg package.


%package dev
Summary: dev components for the ksvg package.
Group: Development
Requires: ksvg-lib = %{version}-%{release}
Requires: ksvg-data = %{version}-%{release}
Provides: ksvg-devel = %{version}-%{release}
Requires: ksvg = %{version}-%{release}

%description dev
dev components for the ksvg package.


%package lib
Summary: lib components for the ksvg package.
Group: Libraries
Requires: ksvg-data = %{version}-%{release}
Requires: ksvg-license = %{version}-%{release}

%description lib
lib components for the ksvg package.


%package license
Summary: license components for the ksvg package.
Group: Default

%description license
license components for the ksvg package.


%prep
%setup -q -n ksvg-6.0.0
cd %{_builddir}/ksvg-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709391411
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709391411
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksvg
cp %{_builddir}/ksvg-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ksvg/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/ksvg-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksvg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksvg-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksvg/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ksvg/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksvg/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/ksvg-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ksvg/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksvg/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/ksvg/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ksvg/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ksvg/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksvg/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/ksvg/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ksvg/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/ksvg-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ksvg/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/ksvg/corebindingsplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/ksvg/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/ksvg/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/ksvg.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KSvg/KSvg/FrameSvg
/usr/include/KF6/KSvg/KSvg/ImageSet
/usr/include/KF6/KSvg/KSvg/Svg
/usr/include/KF6/KSvg/ksvg/framesvg.h
/usr/include/KF6/KSvg/ksvg/imageset.h
/usr/include/KF6/KSvg/ksvg/ksvg_export.h
/usr/include/KF6/KSvg/ksvg/svg.h
/usr/include/KF6/KSvg/ksvg_version.h
/usr/lib64/cmake/KF6Svg/KF6SvgConfig.cmake
/usr/lib64/cmake/KF6Svg/KF6SvgConfigVersion.cmake
/usr/lib64/cmake/KF6Svg/KF6SvgTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Svg/KF6SvgTargets.cmake
/usr/lib64/libKF6Svg.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF6Svg.so.6
/usr/lib64/libKF6Svg.so.6.0.0
/usr/lib64/qt6/qml/org/kde/ksvg/libcorebindingsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksvg/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ksvg/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/ksvg/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/ksvg/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/ksvg/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/ksvg/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/ksvg/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/ksvg/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/ksvg/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ksvg/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/ksvg/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/ksvg/e712eadfab0d2357c0f50f599ef35ee0d87534cb
