Summary:	Graphical object-based image editor
Summary(pl):	Graficzny, bazuj±cy na obiektach edytor obrazków
Name:		geist
Version:	0.0.3
Release:	1
License:	BSD
Vendor:		Tom Gilbert <gilbertt@linuxbrit.co.uk>
Group:		X11/Applications/Graphics
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	16cc0769138481e9ca3c049d6e2b4d79
URL:		http://www.linuxbrit.co.uk/geist.html
Requires:	gtk+-devel >= 1.2.0
Requires:	imlib2 >= 1.0.0
Requires:	libxml2-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Geist is an object-based image editor. It provides a simple and
flexible interface for developing still images, based on Imlib2, a
fast graphics library, and GTK+.

%description -l pl
Geist jest bazuj±cym na obiektach edytorem obrazków. Daje prosty i
elastyczny interfejs do tworzenia nieruchomych obrazów, bazuj±cy
na szybkiej bibliotece graficznej Imlib2 oraz GTK+.

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/geist
