Summary:	GTK2-based client for giFT
Summary(pl.UTF-8):   Klient do giFT bazujący na GTK2
Name:		giFToxic
Version:	0.0.9
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/giftoxic/%{name}-%{version}.tar.gz
# Source0-md5:	66fe05d5d34cf08d310886784682136f
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
URL:		http://giftoxic.sourceforge.net/
BuildRequires:	giFT-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
giFToxic is a GTK2-based client for giFT.

%description -l pl.UTF-8
giFToxic jest graficznym klientem dla giFT bazującym na GTK2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
