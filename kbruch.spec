#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Practice calculating with fractions
Name:		kbruch
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kbruch
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kbruch/-/archive/%{gitbranch}/kbruch-%{gitbranchd}.tar.bz2#/kbruch-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kbruch-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)

%rename plasma6-kbruch

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KBruch is a small program to practice calculating with fractions.

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog TODO
%{_bindir}/kbruch
%{_datadir}/metainfo/org.kde.kbruch.appdata.xml
%{_datadir}/applications/org.kde.kbruch.desktop
%{_datadir}/config.kcfg/kbruch.kcfg
%{_iconsdir}/hicolor/*/apps/kbruch.*[gz]
%{_datadir}/kbruch/pics/*.png
%{_mandir}/man1/kbruch.1*
