Summary:	beryl plugins
Summary(pl):	Wtyczki do beryla
Name:		beryl-plugins
Version:	20061004
Release:	1
License:	GPL/MIT
Group:		X11
Source0:	http://distfiles.xgl-coffee.org/beryl-plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	dc12e381efacbdc8f529143fefa8ed43
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	beryl-core-devel >= 0.1.0
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	dbus-devel >= 0.50
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	beryl-core >= 0.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
beryl plugins.

%description -l pl
Wtyczki do beryla.

%prep
%setup -q -n snapshots/%{name}

%build
autoreconf -v --install

%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/beryl/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README debian/changelog
%dir %{_libdir}/beryl
%attr(755,root,root) %{_libdir}/beryl/*.so
%dir %{_datadir}/beryl
%{_datadir}/beryl/*.settings
%{_datadir}/beryl/*.png
%{_datadir}/dbus-1/services/beryl.service
