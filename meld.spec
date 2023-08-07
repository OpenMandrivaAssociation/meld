%define shortver %(echo %version |cut -d\. -f1-2)

Summary:	A visual diff and merge tool targeted at developers
Name:		meld
Version:	3.22.0
Release:	3
# Use source from gitlab so auto builder can handle it
#Source0:	https://download.gnome.org/sources/meld/%{shortver}/%{name}-%{version}.tar.xz
Source0:	https://gitlab.gnome.org/GNOME/meld/-/archive/%{version}/%{name}-%{version}.tar.bz2
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
Requires:	gtksourceview >= 4
Requires:	python-dbus
Requires:	python-gobject3
Requires:	python-cairo
Requires:	python-gi-cairo
Requires:	patch
Requires:	typelib(GtkSource) >= 4
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
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/metainfo/org.gnome.Meld.appdata.xml
%{_datadir}/applications/org.gnome.Meld.desktop
%{_iconsdir}/*/*/*/
%{_datadir}/mime/packages/org.gnome.Meld.xml
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# remove versioned doc directory
rm -fr %{buildroot}%{_docdir}/%{name}-%{version}/

# locales
%find_lang %{name} --with-gnome

