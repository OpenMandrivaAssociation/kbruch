Name: kbruch
Summary: Practice calculating with fractions
Version: 4.7.95
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kbruch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KBruch is a small program to practice calculating with fractions.

%files
%_kde_bindir/kbruch
%_kde_datadir/applications/kde4/kbruch.desktop
%_kde_appsdir/kbruch
%_kde_iconsdir/*/*/apps/kbruch.*
%_kde_datadir/config.kcfg/kbruch.kcfg
%doc README NEWS VERSION AUTHORS ChangeLog TODO COPYING COPYING.DOC
%doc %_kde_docdir/HTML/en/kbruch
%_kde_mandir/man1/kbruch.1.*

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

