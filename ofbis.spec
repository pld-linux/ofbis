Summary:	Framebuffer library
Summary(pl):	Bibliteka obs³uguj±ca framebuffer
Name:		ofbis
Version:	0.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.nocrew.org/pub/osis/ofbis/%{name}-%{version}.tar.gz
# Source0-md5:	51d7ca6ba662da4b2292186575204035
URL:		http://osis.nocrew.org/ofbis/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framebuffer library.

%description -l pl
Biblioteka obs³uguj±ca framebuffer.

%package devel
Summary:	Header files for framebuffer library
Summary(pl):	Pliki nag³ówkowe do biblioteki obs³uguj±cej framebuffer
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for framebuffer library.

%description devel -l pl
Pliki nag³ówkowe do biblioteki obs³uguj±cej framebuffer.

%package static
Summary:	Static framebuffer library
Summary(pl):	Statyczna biblioteka obs³uguj±ca framebuffer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static framebuffer library.

%description static -l pl
Statyczna biblioteka obs³uguj±ca framebuffer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog DESIGN NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/ofbis.doc
%attr(755,root,root) %{_bindir}/ofbis-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/osis
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
