Summary:	Disk performance XFce panel plugin
Summary(pl):	Wtyczka wydajno¶ci dysku dla panelu XFce
Name:		xfce4-diskperf-plugin
Version:	1.4
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	f22ae9f5ee89094110b7690fa6225b9d
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	libxfce4util-devel >= 3.99
BuildRequires:	libxfcegui4-devel >= 3.99
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99
Requires:	xfce4-panel >= 3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DiskPerf plugin displays disk/partition performance based on the
rsect/wsect data provided by Linux kernels 2.6 or recent 2.4's (at
least 2.4.20 compiled with CONFIG_BLK_STATS turned on, or possibly
older kernel patched with "Disk extended statistics" in
/proc/partitions).

%description -l pl
Wtyczka DiskPerf wy¶wietla wydajno¶æ dysku/partycji bazuj±c na danych
rsect/wsect dostarczanych przez j±dro Linuksa 2.6 lub nowsze 2.4
(conajmniej 2.4.20 skompilowane z w³±czonym CONFIG_BLK_STATS lub
ewentualnie ze starszymi wersjami z dodan± ³at± "rozszerzonych
statystyk dysku" w /proc/partitions).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
