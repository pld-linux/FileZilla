%bcond_with	storj	# support for Storj decentralized cloud storage provider

%define		libfilezilla_ver	0.37.2
Summary:	FTP client for X Window
Summary(es.UTF-8):	Cliente FTP para el X Window
Summary(ja.UTF-8):	X Window System 用マルチスレッド FTP クライアント
Summary(pl.UTF-8):	Klient FTP dla X Window
Summary(pt_BR.UTF-8):	Cliente FTP para o X Window
Summary(ru.UTF-8):	FTP клиент для X Window
Summary(uk.UTF-8):	FTP клієнт для X Window
Name:		FileZilla
Version:	3.60.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://download.filezilla-project.org/client/%{name}_%{version}_src.tar.bz2
# Source0-md5:	1d5966aaff110b1038f24fd44b563457
Patch0:		%{name}-desktop.patch
URL:		https://filezilla-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	cppunit-devel >= 1.13.0
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	gettext-tools >= 0.11.0
BuildRequires:	gtk+3-devel
BuildRequires:	libfilezilla-devel >= %{libfilezilla_ver}
BuildRequires:	libidn-devel
# -std=c++17
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:2
BuildRequires:	nettle-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	pugixml-devel >= 1.9
BuildRequires:	sqlite3-devel >= 3.7
%{?with_storj:BuildRequires:	storj-uplink-c-devel}
BuildRequires:	wxGTK3-unicode-devel >= 3.0.4
BuildRequires:	wxWidgets-devel >= 3.0.4
BuildRequires:	wxWidgets-utils >= 3.0.4
BuildRequires:	xdg-utils
Requires:	dbus-libs >= 1.2
Requires:	libfilezilla >= %{libfilezilla_ver}
Requires:	nettle >= 3.1
Requires:	pugixml >= 1.9
Requires:	wxGTK3-unicode >= 3.0.4
Provides:	filezilla
Obsoletes:	filezilla < 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FileZilla is a fast and reliable FTP client with lots of useful
features and an intuitive interface.

%description -l pl.UTF-8
FileZilla to szybki i wiarygodny klient FTP z wieloma przydatnymi
opcjami oraz intuicyjnym interfejsem.

%prep
%setup -q -n filezilla-%{version}
%patch0 -p1

cd locales
%{__mv} bg{_BG,}.po
%{__mv} ca{_ES,}@valencia.po
%{__mv} cs{_CZ,}.po
%{__mv} fa{_IR,}.po
%{__mv} fi{_FI,}.po
%{__mv} gl{_ES,}.po
%{__mv} he{_IL,}.po
%{__mv} hu{_HU,}.po
%{__mv} id{_ID,}.po
%{__mv} ja{_JP,}.po
%{__mv} km{_KH,}.po
%{__mv} ko{_KR,}.po
%{__mv} lo{_LA,}.po
%{__mv} lt{_LT,}.po
%{__mv} lv{_LV,}.po
%{__mv} mk{_MK,}.po
%{__mv} nb{_NO,}.po
%{__mv} nn{_NO,}.po
%{__mv} pl{_PL,}.po
%{__mv} pt{_PT,}.po
%{__mv} ro{_RO,}.po
%{__mv} sk{_SK,}.po
%{__mv} sl{_SI,}.po
%{__mv} th{_TH,}.po
%{__mv} uk{_UA,}.po
%{__mv} vi{_VN,}.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	xdgopen=/usr/bin/xdg-open \
	--disable-precomp \
	--with-wx-config=wx-gtk3-unicode-config \
	%{?with_storj:--enable-storj} \
	--with-tinyxml=builtin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfzclient-private.{la,so}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfzclient-commonui-private.{la,so}

# not supported by glibc (as of 2.32)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/co

# Remove oversized icons
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/480x480

%find_lang filezilla

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f filezilla.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/filezilla
%attr(755,root,root) %{_bindir}/fzputtygen
%attr(755,root,root) %{_bindir}/fzsftp
%if %{with storj}
%attr(755,root,root) %{_bindir}/fzstorj
%endif
%attr(755,root,root) %{_libdir}/libfzclient-commonui-private-%{version}.so
%attr(755,root,root) %{_libdir}/libfzclient-private-%{version}.so
%{_datadir}/appdata/filezilla.appdata.xml
%dir %{_datadir}/filezilla
%dir %{_datadir}/filezilla/docs
%{_datadir}/filezilla/docs/*
%dir %{_datadir}/filezilla/resources
%{_datadir}/filezilla/resources/*.wav
%{_datadir}/filezilla/resources/*.xml
%dir %{_datadir}/filezilla/resources/xrc
%{_datadir}/filezilla/resources/xrc/*.xrc
%dir %{_datadir}/filezilla/resources/16x16
%{_datadir}/filezilla/resources/16x16/*.gif
%{_datadir}/filezilla/resources/16x16/*.png
%dir %{_datadir}/filezilla/resources/20x20
%{_datadir}/filezilla/resources/20x20/*.png
%dir %{_datadir}/filezilla/resources/24x24
%{_datadir}/filezilla/resources/24x24/*.png
%dir %{_datadir}/filezilla/resources/32x32
%{_datadir}/filezilla/resources/32x32/*.png
%dir %{_datadir}/filezilla/resources/48x48
%{_datadir}/filezilla/resources/48x48/*.png
%dir %{_datadir}/filezilla/resources/blukis
%{_datadir}/filezilla/resources/blukis/theme.xml
%dir %{_datadir}/filezilla/resources/blukis/16x16
%{_datadir}/filezilla/resources/blukis/16x16/*.png
%dir %{_datadir}/filezilla/resources/blukis/32x32
%{_datadir}/filezilla/resources/blukis/32x32/*.png
%dir %{_datadir}/filezilla/resources/blukis/48x48
%{_datadir}/filezilla/resources/blukis/48x48/*.png
%dir %{_datadir}/filezilla/resources/cyril
%{_datadir}/filezilla/resources/cyril/theme.xml
%dir %{_datadir}/filezilla/resources/cyril/16x16
%{_datadir}/filezilla/resources/cyril/16x16/*.png
%dir %{_datadir}/filezilla/resources/flatzilla
%dir %{_datadir}/filezilla/resources/flatzilla/16x16
%{_datadir}/filezilla/resources/flatzilla/16x16/*.png
%dir %{_datadir}/filezilla/resources/flatzilla/24x24
%{_datadir}/filezilla/resources/flatzilla/24x24/*.png
%dir %{_datadir}/filezilla/resources/flatzilla/32x32
%{_datadir}/filezilla/resources/flatzilla/32x32/*.png
%dir %{_datadir}/filezilla/resources/flatzilla/48x48
%{_datadir}/filezilla/resources/flatzilla/48x48/*.png
%{_datadir}/filezilla/resources/flatzilla/theme.xml
%dir %{_datadir}/filezilla/resources/lone
%{_datadir}/filezilla/resources/lone/theme.xml
%dir %{_datadir}/filezilla/resources/lone/16x16
%{_datadir}/filezilla/resources/lone/16x16/*.png
%dir %{_datadir}/filezilla/resources/lone/32x32
%{_datadir}/filezilla/resources/lone/32x32/*.png
%dir %{_datadir}/filezilla/resources/lone/48x48
%{_datadir}/filezilla/resources/lone/48x48/*.png
%dir %{_datadir}/filezilla/resources/minimal
%{_datadir}/filezilla/resources/minimal/theme.xml
%dir %{_datadir}/filezilla/resources/minimal/16x16
%{_datadir}/filezilla/resources/minimal/16x16/*.png
%dir %{_datadir}/filezilla/resources/minimal/32x32
%{_datadir}/filezilla/resources/minimal/32x32/file.png
%dir %{_datadir}/filezilla/resources/opencrystal
%{_datadir}/filezilla/resources/opencrystal/theme.xml
%dir %{_datadir}/filezilla/resources/opencrystal/16x16
%{_datadir}/filezilla/resources/opencrystal/16x16/*.png
%dir %{_datadir}/filezilla/resources/opencrystal/20x20
%{_datadir}/filezilla/resources/opencrystal/20x20/*.png
%dir %{_datadir}/filezilla/resources/opencrystal/24x24
%{_datadir}/filezilla/resources/opencrystal/24x24/*.png
%dir %{_datadir}/filezilla/resources/opencrystal/32x32
%{_datadir}/filezilla/resources/opencrystal/32x32/*.png
%dir %{_datadir}/filezilla/resources/opencrystal/48x48
%{_datadir}/filezilla/resources/opencrystal/48x48/*.png
%dir %{_datadir}/filezilla/resources/sun
%dir %{_datadir}/filezilla/resources/sun/48x48
%{_datadir}/filezilla/resources/sun/48x48/*.png
%{_datadir}/filezilla/resources/sun/theme.xml
%dir %{_datadir}/filezilla/resources/tango
%dir %{_datadir}/filezilla/resources/tango/16x16
%{_datadir}/filezilla/resources/tango/16x16/*.png
%dir %{_datadir}/filezilla/resources/tango/32x32
%{_datadir}/filezilla/resources/tango/32x32/*.png
%dir %{_datadir}/filezilla/resources/tango/48x48
%{_datadir}/filezilla/resources/tango/48x48/*.png
%{_datadir}/filezilla/resources/tango/theme.xml
%dir %{_datadir}/filezilla/resources/480x480
%{_datadir}/filezilla/resources/480x480/*.png
%dir %{_datadir}/filezilla/resources/classic
%dir %{_datadir}/filezilla/resources/classic/16x16
%{_datadir}/filezilla/resources/classic/16x16/*.png
%{_datadir}/filezilla/resources/classic/theme.xml
%dir %{_datadir}/filezilla/resources/default
%dir %{_datadir}/filezilla/resources/default/480x480
%{_datadir}/filezilla/resources/default/480x480/*.png
%{_datadir}/filezilla/resources/default/theme.xml
%{_iconsdir}/hicolor/*x*/apps/filezilla.png
%{_iconsdir}/hicolor/scalable/apps/filezilla.svg
%{_desktopdir}/filezilla.desktop
%{_pixmapsdir}/filezilla.png
%{_mandir}/man1/filezilla.1*
%{_mandir}/man1/fzputtygen.1*
%{_mandir}/man1/fzsftp.1*
%{_mandir}/man5/fzdefaults.xml.5*
