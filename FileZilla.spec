# TODO
# - /usr/share/locale/ca_ES@valencia is needed by FileZilla-3.0.5.2-1.i686
#   (there is probably ca_ES@valencia locale in Debian glibc - merge it)
#   Temporary removed locale...
Summary:	FTP client for X Window
Summary(es.UTF-8):	Cliente FTP para el X Window
Summary(ja.UTF-8):	X Window System 用マルチスレッド FTP クライアント
Summary(pl.UTF-8):	Klient FTP dla X Window
Summary(pt_BR.UTF-8):	Cliente FTP para o X Window
Summary(ru.UTF-8):	FTP клиент для X Window
Summary(uk.UTF-8):	FTP клієнт для X Window
Name:		FileZilla
Version:	3.23.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/filezilla/%{name}_%{version}_src.tar.bz2
# Source0-md5:	5f52629d11a16ed2d547a4b200d3448c
Patch0:		%{name}-desktop.patch
URL:		http://filezilla-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cppunit-devel
BuildRequires:	dbus-devel
BuildRequires:	gettext-tools
BuildRequires:	gnutls-devel >= 3.4.0
BuildRequires:	gtk+2-devel
BuildRequires:	libfilezilla-devel >= 0.9.0
BuildRequires:	libidn-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	nettle-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	pugixml-devel >= 1.6-2
BuildRequires:	systemd-devel
BuildRequires:	wxGTK2-unicode-devel >= 3.0.1
BuildRequires:	wxWidgets-devel >= 3.0.1
BuildRequires:	wxWidgets-utils >= 3.0.1
BuildRequires:	xdg-utils
Requires:	wxWidgets >= 3.0.1
Provides:	filezilla
Obsoletes:	filezilla
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
mv bg{_BG,}.po
mv cs{_CZ,}.po
#mv da{_DK,}.po
#mv et{_EE,}.po
mv fa{_IR,}.po
mv fi{_FI,}.po
mv gl{_ES,}.po
mv he{_IL,}.po
mv hu{_HU,}.po
mv id{_ID,}.po
mv ja{_JP,}.po
mv km{_KH,}.po
mv ko{_KR,}.po
mv lt{_LT,}.po
mv lv{_LV,}.po
mv mk{_MK,}.po
mv nb{_NO,}.po
mv nn{_NO,}.po
mv pl{_PL,}.po
mv pt{_PT,}.po
mv ro{_RO,}.po
mv sk{_SK,}.po
mv sl{_SI,}.po
mv th{_TH,}.po
mv uk{_UA,}.po
mv vi{_VN,}.po
# Temporary - FIXME:
rm -f ca@valencia.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-unicode-config \
	--with-tinyxml=builtin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Temporary - FIXME:
rm -rf \
	$RPM_BUILD_ROOT%{_localedir}/{ca_ES@valencia,co,kab,lo_LA}

%find_lang filezilla

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filezilla.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/filezilla
%attr(755,root,root) %{_bindir}/fzsftp
%attr(755,root,root) %{_bindir}/fzputtygen
%{_datadir}/appdata/filezilla.appdata.xml
%dir %{_datadir}/filezilla
%dir %{_datadir}/filezilla/docs
%{_datadir}/filezilla/docs/*
%dir %{_datadir}/filezilla/resources
%{_datadir}/filezilla/resources/*.png
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
%{_iconsdir}/hicolor/*/apps/filezilla.png
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
