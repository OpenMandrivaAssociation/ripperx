%define	name	ripperx
%define	oname	ripperX
%define	version	2.7.0
%define	release	%mkrel 1

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

%build
%configure
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install -m644 src/xpms/%{oname}-icon.xpm -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{oname}-icon.xpm
desktop-file-install --vendor="" \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
	--add-category="AudioVideo;Audio;" \
	%{oname}.desktop

#icon
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT/%{_liconsdir}/%{oname}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT/%{_iconsdir}/%{oname}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT/%{_miconsdir}/%{oname}.png

%post
%{update_menus}

%postun
%{clean_menus}
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%{_bindir}/%{oname}*
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_datadir}/pixmaps/%{oname}-icon.xpm
%{_datadir}/applications/%{oname}.desktop
