Summary:	Practice calculating with fractions
Name:		kbruch
Version:	23.08.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kbruch
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

%description
KBruch is a small program to practice calculating with fractions.

%files -f kbruch.lang
%doc README NEWS AUTHORS ChangeLog TODO
%{_bindir}/kbruch
%{_datadir}/metainfo/org.kde.kbruch.appdata.xml
%{_datadir}/applications/org.kde.kbruch.desktop
%{_datadir}/config.kcfg/kbruch.kcfg
%{_iconsdir}/hicolor/*/apps/kbruch.*[gz]
%{_datadir}/kbruch/pics/*.png
%{_datadir}/kxmlgui5/kbruch/AppMenuWidgetui.rc
%{_datadir}/kxmlgui5/kbruch/FractionRingWidgetui.rc
%{_datadir}/kxmlgui5/kbruch/kbruchui.rc
%{_mandir}/man1/kbruch.1.*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kbruch --with-man --with-html
