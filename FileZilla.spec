# TODO
#	/usr/share/locale/ca_ES@valencia is needed by FileZilla-3.0.5.2-1.i686
#	(there is probably ca_ES@valencia locale in Debian glibc - merge it)
Summary:	FTP client for X Window
Summary(es.UTF-8):	Cliente FTP para el X Window
Summary(ja.UTF-8):	X Window System 用マルチスレッド FTP クライアント
Summary(pl.UTF-8):	Klient FTP dla X Window
Summary(pt_BR.UTF-8):	Cliente FTP para o X Window
Summary(ru.UTF-8):	FTP клиент для X Window
Summary(uk.UTF-8):	FTP клієнт для X Window
Name:		FileZilla
Version:	3.0.5.2
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/filezilla/%{name}_%{version}_src.tar.bz2
# Source0-md5:	9178cfdb2421f27e46be57eeff7b0f7c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locales.patch
URL:		http://filezilla-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.5
BuildRequires:	wxGTK2-unicode-devel >= 2.8.6
BuildRequires:	wxWidgets-devel >= 2.8.6
BuildRequires:	wxWidgets-utils >= 2.8.6
Requires:	wxWidgets >= 2.8.6
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
%patch1 -p1

cd locales
mv bg{_BG,}.po
mv ca{_ES,}.po
mv cs{_CZ,}.po
mv da{_DK,}.po
mv de{_DE,}.po
mv el{_GR,}.po
mv es{_ES,}.po
mv et{_EE,}.po
mv eu{_ES,}.po
mv fi{_FI,}.po
mv fr{_FR,}.po
mv gl{_ES,}.po
mv he{_IL,}.po
mv hu{_HU,}.po
mv id{_ID,}.po
mv it{_IT,}.po
mv ja{_JP,}.po
mv km{_KH,}.po
mv ko{_KR,}.po
mv lt{_LT,}.po
mv lv{_LV,}.po
mv mk{_MK,}.po
mv nb{_NO,}.po
mv nl{_NL,}.po
mv pl{_PL,}.po
mv pt{_PT,}.po
mv ro{_RO,}.po
mv ru{_RU,}.po
mv sk{_SK,}.po
mv sl{_SI,}.po
mv sv{_SE,}.po
mv tr{_TR,}.po

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang filezilla

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filezilla.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/filezilla
%attr(755,root,root) %{_bindir}/fzsftp
%dir %{_datadir}/filezilla
%dir %{_datadir}/filezilla/docs
%{_datadir}/filezilla/docs/*
%dir %{_datadir}/filezilla/resources
%{_datadir}/filezilla/resources/*.png
%{_datadir}/filezilla/resources/*.wav
%{_datadir}/filezilla/resources/*.xml
%{_datadir}/filezilla/resources/*.xrc
%dir %{_datadir}/filezilla/resources/16x16
%{_datadir}/filezilla/resources/16x16/*.png
%dir %{_datadir}/filezilla/resources/32x32
%{_datadir}/filezilla/resources/32x32/*.png
%dir %{_datadir}/filezilla/resources/48x48
%{_datadir}/filezilla/resources/48x48/*.png
%dir %{_datadir}/filezilla/resources/blukis
%dir %{_datadir}/filezilla/resources/blukis/16x16
%{_datadir}/filezilla/resources/blukis/16x16/*.png
%dir %{_datadir}/filezilla/resources/blukis/32x32
%{_datadir}/filezilla/resources/blukis/32x32/*.png
%dir %{_datadir}/filezilla/resources/blukis/48x48
%{_datadir}/filezilla/resources/blukis/48x48/*.png
%dir %{_datadir}/filezilla/resources/cyril
%dir %{_datadir}/filezilla/resources/cyril/16x16
%{_datadir}/filezilla/resources/cyril/16x16/*.png
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
