%define	oname	ripperX

Summary:	GTK program to rip CD audio and encode mp3s
Name:		ripperx
Version:	2.7.0
Release:	6
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
URL:		https://sourceforge.net/projects/ripperx/
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

%clean

%files
%doc FAQ README README.plugin README.plugin_spec_v0.1 README.plugin_tester TODO CHANGES COPYING BUGS
%{_bindir}/%{oname}*
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_datadir}/pixmaps/%{oname}-icon.xpm
%{_datadir}/applications/%{oname}.desktop


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.7.0-4mdv2010.0
+ Revision: 442753
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.0-3mdv2009.1
+ Revision: 355092
- fix linking
- fir format errors
- fix menu entry

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Funda Wang <fundawang@mandriva.org>
    - Add patch from debian
    - BR id3
    - New version
    - Import ripperx



* Thu Apr 06 2006 Erwan Velu <erwan@seanodes.com> 2.6.7-1mdk
- 2.6.7

* Sun Jun 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.6.6-1mdk
- 2.6.6

* Thu Dec 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6.4-1mdk
- 2.6.4

* Wed Nov 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6.3-1mdk
- 2.6.3

* Sat May 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6.1-1mdk
- 2.6.1

* Wed May 26 2004 Robert Vojta <robert.vojta@mandrake.org> 2.6.0-3mdk
- fixed menu entry (use %%{oname} instead of %%{name})

* Sun Jan 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6.0-2mdk
- fix provides/obsoletes

* Mon Dec 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.6.0-1mdk
- 2.6.0
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- don't bzip2 icons in src.rpm
- cleanups
- no explicit library dependency
- fix buildrequires (lib64..)
- quiet setup

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.5-2mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.5-1mdk
- 2.5

* Thu Sep 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- 2.4

* Fri Jun 14 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.3-2mdk
- BuildRequires
- png icons (out xpm!)
- update URL

* Mon Dec 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.3-1mdk
- 2.3

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2-1mdk
- 2.2

* Thu Apr 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0-1mdk
- added in contribs by Marcel Pol <mpol@gmx.net> :
	- Made rpm for Mandrake
	- Version 2.0 (Jan 09 2000)
	- Added menu-entry

* Mon Jan 03 2000 Dax Kelson <dax@gurulabs.com>
- Version 1.9
- Updated SPEC to use a $RPM_BUILD_ROOT, changelog, docs, and the strip binaries
- Created GNOME ".desktop" file so ripperX shows up on the menu
- Patch so cdparanoia fills files that are group writable, enabling shared directory ripping
