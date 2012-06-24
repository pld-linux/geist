# this is NOT relocatable..?
%define	name	geist
%define	ver	0.0.3
%define	rel	1
%define prefix  /usr

Summary: Graphical object-based image editor
Name: %{name}
Version: %{ver}
Release: %{rel}
Copyright: BSD
Group: User Interface/X
URL: http://www.linuxbrit.co.uk/geist.html
Packager: Term <term@kempler.net>
Vendor: Tom Gilbert <gilbertt@linuxbrit.co.uk>
Source: http://linuxbrit.co.uk/downloads/%{name}-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: imlib2 >= 1.0.0
Requires: libxml2-devel >= 2.0
Requires: gtk+-devel >= 1.2.0
Requires: zlib

%description
Geist is an object-based image editor. It provides a simple and flexible
interface for developing still images, based on Imlib2, a fast graphics
library, and GTK+.

%prep
%setup -q

%build
./configure --prefix=%{prefix}
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/share/geist/*
%{prefix}/bin/*
