Summary:	Practice calculating with fractions
Name:		kbruch
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kbruch
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

%description
KBruch is a small program to practice calculating with fractions.

%files
%doc README NEWS VERSION AUTHORS ChangeLog TODO COPYING COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kbruch
%{_kde_bindir}/kbruch
%{_kde_applicationsdir}/kbruch.desktop
%{_kde_appsdir}/kbruch
%{_kde_iconsdir}/*/*/apps/kbruch.*
%{_kde_datadir}/appdata/kbruch.appdata.xml
%{_kde_datadir}/config.kcfg/kbruch.kcfg
%{_kde_mandir}/man1/kbruch.1.*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

