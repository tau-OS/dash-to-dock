%global extdir %{_datadir}/gnome-shell/extensions/dash-to-dock@tauos.co

Summary:        Dock for the GNOME Shell by micxgx@gmail.com, modified for tauOS
Name:           tau-dash-to-dock
# This should match the version in metadata.json
Version:        72
Release:        12
License:        GPLv2+
URL:            https://micheleg.github.io/dash-to-dock
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  meson
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
%meson
%meson_build

%install
%meson_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{_datadir}/glib-2.0/schemas/*gschema.*

%changelog
* Mon May 2 2022 Lains <lainsce@airmail.cc> - 72-7
- Fix for dock hiding when popupmenu is open
- Implement manual hide
- get_preferred_height/width as 0 if NaN: Sometimes the requested height/width was NaN causing gnome-shell
to log warnings everytime the workspaces view was opened.
- 

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 72-6
- When clicking any app on the Dock, action will be to minimize it

* Wed Apr 27 2022 Lains <lainsce@airmail.cc> - 72-5
- When in Panel Mode, remember icons centered

* Wed Apr 27 2022 Lains <lainsce@airmail.cc> - 72-4
- Remove all options that were in the Basic Settings already

* Wed Apr 27 2022 Lains <lainsce@airmail.cc> - 72-3
- When in Panel Mode, make icons centered

* Sat Apr 23 2022 Jamie Murphy <jamie@fyralabs.com> - 72-2
- Change to Meson

* Sat Apr 23 2022 Jamie Murphy <jamie@fyralabs.com> - 72-1
- Update Settings (Thanks @lainsce)
- General improvements

* Thu Apr 14 2022 Jamie Murphy <jamie@fyralabs.com> - 71-1.1
- Remove RunningIndicatorDefault due to bugs
- Introduce tauOS Specific Changes
- General improvements

* Sun Apr 3 2022 Jamie Murphy <jamie@fyralabs.com> - 71-1
- Initial Release
