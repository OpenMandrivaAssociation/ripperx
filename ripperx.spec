%define	name	ripperx
%define	oname	ripperX
%define	version	2.7.0
%define	release	%mkrel 3

Summary:	GTK program to rip CD audio and encode mp3s
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
Requires:	cdparanoia
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libid3-devel
BuildRequires:	desktop-file-utils
Source0:	%{oname}-%{version}.tar.bz2
Source11:	%{oname}-48.png
Source12:	%{oname}-32.png
Source13:	%{oname}-16.png
Patch2:		%{oname}-2.7.0-cdplay-command.patch
Patch3:		ripperX-2.7.0-fix-format-errors.patch
Patch4:		ripperX-2.7.0-fix-linking.patch
URL:		http://sourceforge.net/projects/ripperx/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{oname}
Obsoletes:	%{oname}

%description
GTK program to rip CD audio and encode mp3s. Supports parallel
ripping/encoding, has plugins for cdparanoia, BladeEnc, Lame, 
GoGo, FHG (l3enc and mp3enc), XingMp3enc, 8hz-mp3, and the 
ISO encoder.  Also has support for CDDB and ID3 tags.

%prep
%setup -q -n %{oname}-%{version}
%patch2 -p1
%patch3 -p1
%patch4 -p1

perl -pi -e 's/MultipleArgs=false\n//' ripperX.desktop

%build
%configure
%make


%install
rm -rf %{buildroot}
%makeinstall

install -m644 src/xpms/%{oname}-icon.xpm -D %{buildroot}%{_datadir}/pixmaps/%{oname}-icon.xpm
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications/ \
	--add-category="AudioVideo;Audio;" \
	%{oname}.desktop

#icon
install -m644 %{SOURCE11} -D %{buildroot}/%{_liconsdir}/%{oname}.png
install -m644 %{SOURCE12} -D %{buildroot}/%{_iconsdir}/%{oname}.png
install -m644 %{SOURCE13} -D %{buildroot}/%{_miconsdir}/%{oname}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%{_bindir}/%{oname}*
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_datadir}/pixmaps/%{oname}-icon.xpm
%{_datadir}/applications/%{oname}.desktop
