Summary:	beryl plugins
Summary(pl):	Wtyczki do beryla
Name:		beryl-plugins
Version:	20061102
Release:	1
License:	GPL/MIT
Group:		X11
#Source0:	http://distfiles.xgl-coffee.org/beryl-plugins/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	9782e45a25f5781a1553c7be879106c2
Patch0:		%{name}-fsck-patents.patch
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
%setup -q -n %{name}
%patch0 -p1

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
%doc AUTHORS README
%dir %{_libdir}/beryl
%attr(755,root,root) %{_libdir}/beryl/*.so
%dir %{_datadir}/beryl
%{_datadir}/beryl/*.png
