%define name	meld
%define version 1.1.4
%define release %mkrel 3

Summary:	Meld is a GNOME 2 visual diff and merge tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Source1:   	%{name}16.png
Source2:   	%{name}32.png
Source3:   	%{name}48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPL
URL:		http://meld.sourceforge.net/
Group:		File tools
BuildRequires: scrollkeeper
BuildRequires: python-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires:	pygtk2.0-libglade
Requires:	gnome-python
Requires:	gnome-python-canvas
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
BuildArch:	noarch
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3


%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges.
The margins show location of changes for easy navigation, and it also
features a tabbed interface that allows you to open many diffs at once.

%prep
%setup -q

%build
%make prefix=%_prefix libdir=%_datadir

%install
rm -rf ${RPM_BUILD_ROOT} %name.lang
%makeinstall_std prefix=%_prefix libdir=%_datadir

%find_lang %name --with-gnome

# Icons
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

# Install menu entry
install -d ${RPM_BUILD_ROOT}%{_menudir}
cat << EOF > ${RPM_BUILD_ROOT}%{_menudir}/%{name}
?package(%{name}): needs="x11" \
		   section="System/File Tools" \
		   title="Meld" \
		   longtitle="%{summary}" \
		   icon="%{name}.png" \
		   command="%{name}" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


rm -rf %buildroot/usr/var/lib/scrollkeeper

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%{update_menus}
%update_scrollkeeper

%postun
%{clean_menus}
%clean_scrollkeeper

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README* changelog COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/application-registry/*
%{_datadir}/applications/*
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/meld-C.omf
%{_datadir}/pixmaps/*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
