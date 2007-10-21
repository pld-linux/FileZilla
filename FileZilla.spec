Summary:	FTP client for X Window
Summary(es.UTF-8):	Cliente FTP para el X Window
Summary(ja.UTF-8):	X Window System 用マルチスレッド FTP クライアント
Summary(pl.UTF-8):	Klient FTP dla X Window
Summary(pt_BR.UTF-8):	Cliente FTP para o X Window
Summary(ru.UTF-8):	FTP клиент для X Window
Summary(uk.UTF-8):	FTP клієнт для X Window
Name:		FileZilla
Version:	3.0.2.1
Release:	0.2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/filezilla/%{name}_%{version}_src.tar.bz2
# Source0-md5:	0182908d3091d19edc511b3a2a6b3e08
URL:		http://filezilla-project.org/
BuildRequires:	wxGTK2-unicode-devel >= 2.8.4
BuildRequires:	wxWidgets-devel >= 2.8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n filezilla-%{version}

%build
%configure \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
#%doc
