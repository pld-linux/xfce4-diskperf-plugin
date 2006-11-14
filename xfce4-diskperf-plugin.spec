Summary:	Disk performance Xfce panel plugin
Summary(pl):	Wtyczka wydajno¶ci dysku dla panelu Xfce
Name:		xfce4-diskperf-plugin
Version:	2.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-diskperf-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	be819b14db68369f541a02f9a27e9dc5
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-bug1842.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.3.90.1
BuildRequires:	libxfcegui4-devel >= 4.3.90.1
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.3.90.1
Requires:	xfce4-panel >= 4.3.90.1
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
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
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

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
