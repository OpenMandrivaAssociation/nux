%define api 4.0
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Visual rendering toolkit for real-time applications
Name:		nux
Version:	4.0.8
Release:	1
License:	LGPL
Group:		System/Libraries
Source0:	https://launchpad.net/nux/4.0/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:   nux-disable-werror.patch
Patch1:   boost-fix.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(glew)
#BuildRequires:	pkgconfig(glewmx)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(libgeis)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(gmock)
BuildRequires:	boost-devel

Requires:	%{libname} = %{version}-%{release}

%description
Visual rendering toolkit for real-time applications - tools
Nux is a graphical user interface toolkit for applications that mixes OpenGL
hardware acceleration with high quality visual rendering.

%package -n %{libname}
Summary:    Libraries for the nux package
Group:      System/Libraries

%description -n %{libname}
Libraries for nux.

%package -n %{develname}
Summary:    Nux headers and development libraries
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Nux development headers and libraries.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%define _disable_ld_no_undefined 1
# enable-ooengles-20 is the only way to build...
# otherwise we get hundreds of "multiple definition" errors
%configure --enable-opengles-20
%make_build LIBS='-lpthread'

%install
%make_install

rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc README INSTALL COPYING COPYING.gpl TODO AUTHORS NEWS ChangeLog doxygen-include.am doxygen.cfg
%{_libexecdir}/unity_support_test
%{_datadir}/nux/%{api}/UITextures/*
%{_datadir}/nux/%{api}/Fonts/*

%files -n %{libname}
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{develname}
%{_datadir}/nux/gputests/*.cpp
%{_includedir}/Nux-%{api}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

