%define shortver 3.21

Summary:	A visual diff and merge tool targeted at developers
Name:		meld
Version:	3.21.3
Release:	1
Source0:	https://download.gnome.org/sources/%{name}/%{shortver}/%{name}-%{version}.tar.xz
License:	GPLv2+
URL:		http://meldmerge.org/
Group:		File tools
BuildArch:	noarch

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	pkgconfig(python)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils
BuildRequires:	python3dist(distro)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(py3cairo)

Requires:	dbus-x11
Requires:	glib2
Requires:	%{_lib}gtk3_0
Requires:	gtksourceview4
Requires:	python-dbus
Requires:	python-gobject
Requires:	python-cairo
Requires:	python-gi-cairo
Requires:	patch
Requires:	typelib(GtkSource) 
Requires:	%{name}-schemas = %{version}-%{release}

%description
Meld is a visual diff and merge tool targeted at developers. Meld helps you
compare files, directories, and version controlled projects. It provides
two- and three-way comparison of both files and directories, and supports
many version control systems including Git, Mercurial, Bazaar and Subversion.

Meld helps you review code changes, understand patches, and makes enormous
merge conflicts slightly less painful.

%files -f %{name}.lang
%{_bindir}/%{name}
%dir %{py3_puresitedir}/%{name}
%{py3_puresitedir}/%{name}/*
#{py3_puresitedir}/%{name}-%{version}-py*.*.egg-info
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
#{_datadir}/metainfo/org.gnome.%{name}.appdata.xml
#{_datadir}/applications/org.gnome.%{name}.desktop
%{_iconsdir}/*/*/*/
#{_datadir}/mime/packages/org.gnome.%{name}.xml
%{_mandir}/man1/%{name}.1*
%doc NEWS COPYING

#---------------------------------------------------------------------------

%package schemas
Summary:	Gsettings schema files for %{name}
License:	GPLv2+
Group:		File tools
BuildArch:	noarch

%description schemas
This package provides the gsettings schemas for %{name}.

%files schemas
%{_datadir}/glib-2.0/schemas/org.gnome.*.gschema.xml

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

# remove versioned doc directory
rm -fr %{buildroot}%{_docdir}/%{name}-%{version}/

# locales
%find_lang %{name} --with-gnome

#check
#desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

