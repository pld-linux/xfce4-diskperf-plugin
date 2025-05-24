Summary:	Disk performance Xfce panel plugin
Summary(pl.UTF-8):	Wtyczka wydajności dysku dla panelu Xfce
Name:		xfce4-diskperf-plugin
Version:	2.8.0
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-diskperf-plugin/2.8/%{name}-%{version}.tar.xz
# Source0-md5:	042e0b632dffe250c8ebf0f3dfa93100
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-diskperf-plugin
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libdiskperf.so
%{_datadir}/xfce4/panel/plugins/diskperf.desktop
