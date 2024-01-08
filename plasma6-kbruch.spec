Summary:	Practice calculating with fractions
Name:		plasma6-kbruch
Version:	24.01.85
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kbruch
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kbruch-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)

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
%{_datadir}/kxmlgui6/kbruch/AppMenuWidgetui.rc
%{_datadir}/kxmlgui6/kbruch/FractionRingWidgetui.rc
%{_datadir}/kxmlgui6/kbruch/kbruchui.rc
%{_mandir}/man1/kbruch.1.*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kbruch --with-man --with-html
