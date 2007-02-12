Summary:	Framebuffer library
Summary(pl.UTF-8):   Biblioteka obsługująca framebuffer
Name:		ofbis
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.nocrew.org/pub/osis/ofbis/%{name}-%{version}.tar.gz
# Source0-md5:	172a671629d505d377ca78ec30849f15
URL:		http://osis.nocrew.org/ofbis/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framebuffer library.

%description -l pl.UTF-8
Biblioteka obsługująca framebuffer.

%package devel
Summary:	Header files for framebuffer library
Summary(pl.UTF-8):   Pliki nagłówkowe do biblioteki obsługującej framebuffer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for framebuffer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki obsługującej framebuffer.

%package static
Summary:	Static framebuffer library
Summary(pl.UTF-8):   Statyczna biblioteka obsługująca framebuffer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static framebuffer library.

%description static -l pl.UTF-8
Statyczna biblioteka obsługująca framebuffer.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
