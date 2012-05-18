%define api 2.0
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary: Visual rendering toolkit for real-time applications
Name: nux
Version: 2.12.0
Release: 2
License: LGPL
Group: System/Libraries
Source0: http://launchpad.net/%{name}/1.0/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glewmx)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(libutouch-geis)
BuildRequires:  pkgconfig(ibus-1.0)
#BuildRequires:	gtest-devel
BuildRequires:	gmock-devel
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
%setup -q 

%build
%define _disable_ld_no_undefined 1
%configure2_5x
%make LIBS='-lpthread'

%install
%makeinstall_std

rm -f %{buildroot}/%{_libdir}/*.la

%clean
rm -fr %{buildroot}

%files
%defattr(-, root, root)
%doc README INSTALL COPYING COPYING.gpl TODO AUTHORS NEWS ChangeLog doxygen-include.am doxygen.cfg
%{_libdir}/unity_support_test
%{_datadir}/nux/2.0/UITextures/*
%{_datadir}/nux/2.0/Fonts/*

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*-%{api}.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%{_datadir}/nux/gputests/*.cpp
%{_includedir}/Nux-2.0/Nux/*.h
%{_includedir}/Nux-2.0/Nux/Readme.txt
%{_includedir}/Nux-2.0/NuxImage/*.h
%{_includedir}/Nux-2.0/NuxGraphics/*.h
%{_includedir}/Nux-2.0/NuxCore/*.h
%{_includedir}/Nux-2.0/NuxCore/Character/*.h
%{_includedir}/Nux-2.0/NuxCore/FileManager/*.h
%{_includedir}/Nux-2.0/NuxCore/Math/*.h
%{_includedir}/Nux-2.0/Nux/ProgramFramework/*.h
%{_includedir}/Nux-2.0/NuxCore/TinyXML/*.h
%{_libdir}/*.so
#{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


