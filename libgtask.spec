Summary:	Implementation of the progress bar simplification system
Summary(pl):	Implementacja systemu upraszczania paska postêpu
Name:		libgtask
Version:	0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtask/%{name}-%{version}.tar.gz
# Source0-md5:	d5a4cb92ab287213fa3beeb0a3c79f3d
URL:		http://gtask.sourceforge.net/
BuildRequires:	glib2-devel >= 2.3.0
BuildRequires:	libxml2-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gTask is an implementation of the progress bar simplification system.
The intent of the project is to create an easy to use framework for
application developers to communication the progress to certain long
running events.

%description -l pl
gTask jest implementacj± systemu upraszczania paska postêpu.
Za³o¿eniem projektu jest stworzenie ³atwej w u¿yciu biblioteki
s³u¿±cej do komunikacji procesów z d³ugo wykonywanymi zadaniami.

%package devel
Summary:	Header files for libgtask library
Summary(pl):	Pliki nag³ówkowe biblioteki libgtask
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.3.0
Requires:	libxml2-devel >= 2.5.0

%description devel
Header files for libgtask library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgtask.

%package static
Summary:	Static libgtask library
Summary(pl):	Statyczna biblioteka libgtask
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libgtask library.

%description static -l pl
Statyczna biblioteka libgtask.

%prep
%setup -q

%build
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
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gtask-0.1
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
