Summary:	Practice calculating with fractions
Name:		kbruch
Version:	16.04.1
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
%doc %{_docdir}/HTML/en/kbruch
%{_bindir}/kbruch
%{_datadir}/appdata/org.kde.kbruch.appdata.xml
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

