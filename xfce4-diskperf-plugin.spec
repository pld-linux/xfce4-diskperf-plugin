Summary:	Disk performance Xfce panel plugin
Summary(pl.UTF-8):   Wtyczka wydajności dysku dla panelu Xfce
Name:		xfce4-diskperf-plugin
Version:	2.1.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-diskperf-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	fc74a0c7d2b9486cdb704a072cd72b83
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DiskPerf plugin displays disk/partition performance based on the
rsect/wsect data provided by Linux kernels 2.6 or recent 2.4's (at
least 2.4.20 compiled with CONFIG_BLK_STATS turned on, or possibly
older kernel patched with "Disk extended statistics" in
/proc/partitions).

%description -l pl.UTF-8
Wtyczka DiskPerf wyświetla wydajność dysku/partycji bazując na danych
rsect/wsect dostarczanych przez jądro Linuksa 2.6 lub nowsze 2.4
(conajmniej 2.4.20 skompilowane z włączonym CONFIG_BLK_STATS lub
ewentualnie ze starszymi wersjami z dodaną łatą "rozszerzonych
statystyk dysku" w /proc/partitions).

%prep
%setup -q

%build
%{__intltoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-diskperf-plugin
%{_datadir}/xfce4/panel-plugins/diskperf.desktop
