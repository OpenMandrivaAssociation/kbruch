Name:		kbruch
Summary:	Practice calculating with fractions
Version: 4.9.2
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kbruch
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KBruch is a small program to practice calculating with fractions.

%files
%doc README NEWS VERSION AUTHORS ChangeLog TODO COPYING COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kbruch
%{_kde_bindir}/kbruch
%{_kde_applicationsdir}/kbruch.desktop
%{_kde_appsdir}/kbruch
%{_kde_iconsdir}/*/*/apps/kbruch.*
%{_kde_datadir}/config.kcfg/kbruch.kcfg
%{_kde_mandir}/man1/kbruch.1.*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

