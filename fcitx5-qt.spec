# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%global commit_tag %{nil}

Name:           fcitx5-qt
Version:        5.1.9
# When using a commit_tag (i.e. not %{nil}) add a commit date 
# decoration ~0.yyyyMMdd. to Release number  
Release:        5
Summary:        Qt library and IM module for fcitx5
Group:          Utilities
License:        LGPLv2.1+ BSD-3-Clause
URL:            https://github.com/fcitx/fcitx5-qt/

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        https://github.com/fcitx/fcitx5-qt/archive/%{commit_tag}.tar.gz#/%{name}-%{version}.xz
%else
Source0:        https://github.com/fcitx/fcitx5-qt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildSystem:   cmake
BuildOption:   -DENABLE_QT5=OFF

BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6WaylandGlobalPrivate)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: fcitx5-devel
BuildRequires: gettext

Provides:       fcitx-qt = %{version}
Obsoletes:      fcitx-qt < 5
Obsoletes:      kcm-fcitx <= 0.5.6

%description
Qt library and IM module for fcitx5

%package devel
Summary:	Development package for Qt library and IM module for fcitx5
Requires:	%{name} = %{EVRD}

%description devel
Development package for Qt library and IM module for fcitx5

%files
%license LICENSES/BSD-3-Clause.txt LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_bindir}/%{name}6-immodule-probing
%{_libdir}/libFcitx5Qt6*
%{_libdir}/qt6/plugins/*
%{_libdir}/fcitx5/qt6/*
%{_datadir}/locale/*
%{_datadir}/applications/org.fcitx.%{name}6-gui-wrapper.desktop
%{_libexecdir}/%{name}6-gui-wrapper

%files devel
%{_includedir}/Fcitx5Qt6/*
%{_libdir}/cmake/*
