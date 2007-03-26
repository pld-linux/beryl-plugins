Summary:	beryl plugins
Summary(pl.UTF-8):	Wtyczki do beryla
Name:		beryl-plugins
Version:	0.2.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	3d7d13dd42aea48bba5be7cfe6c7f371
Patch0:		%{name}-fsck-patents.patch
URL:		http://beryl-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	dbus-devel >= 0.50
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	glitz-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	beryl-core >= 1:%{version}
Obsoletes:	compiz-quinnstorm-plugins
Obsoletes:	beryl-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
beryl plugins.

%description -l pl.UTF-8
Wtyczki do beryla.

%prep
%setup -q
%patch0 -p1
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{nb_NO,nb}.po
mv -f po/{pl_PL,pl}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{sv_SE,sv}.po

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ca
es
es_AR
fr
hu
it
ja
ko
nb
nl
pl
pt_BR
pt
sv
zh_CN
zh_HK
zh_TW
EOF

%build
%{__glib_gettextize}
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/beryl/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/beryl/*.so
%{_datadir}/beryl/*.png
