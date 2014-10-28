%define		xfce_version	4.11.0

Summary:	freedesktop.org compliant menu implementation
Name:		garcon
Version:	0.3.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://archive.xfce.org/src/libs/garcon/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	853f13fbad4760374a2a889acaa4a6c1
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-gio-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xorg-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
freedesktop.org compliant menu implementation for Xfce.

%package libs
Summary:	garcon library
Group:		Libraries

%description libs
garcon library.

%package devel
Summary:	Development files for garcon library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development files for the garcon library.

%package apidocs
Summary:	garcon API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
garcon API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/desktop-directories/*.directory
%{_sysconfdir}/xdg/menus/xfce-applications.menu

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgarcon-1.so.?
%attr(755,root,root) %ghost %{_libdir}/libgarcon-gtk2-1.so.0
%attr(755,root,root) %{_libdir}/libgarcon-1.so.*.*.*
%attr(755,root,root) %{_libdir}/libgarcon-gtk2-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgarcon-1.so
%attr(755,root,root) %{_libdir}/libgarcon-gtk2-1.so
%{_includedir}/garcon-1
%{_includedir}/garcon-gtk2-1
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

