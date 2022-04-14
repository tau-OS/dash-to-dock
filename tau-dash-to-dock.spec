%global extdir %{_datadir}/gnome-shell/extensions/dash-to-dock@tauos.co

Summary:        Dock for the GNOME Shell by micxgx@gmail.com, modified for tauOS
Name:           tau-dash-to-dock
# This should match the version in metadata.json
Version:        71
Release:        1.1
License:        GPLv2+
URL:            https://micheleg.github.io/dash-to-dock
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  sassc
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.

Features modifications for tauOS.

%prep
%setup -q

%build
%make_build

%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name

%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{_datadir}/glib-2.0/schemas/*gschema.*

%changelog
* Thu Apr 14 2022 Jamie Murphy <jamie@fyralabs.com> - 71-1.1
- Remove RunningIndicatorDefault due to bugs
- Introduce tauOS Specific Changes
- General improvements

* Sun Apr 3 2022 Jamie Murphy <jamie@fyralabs.com> - 71-1
- Initial Release