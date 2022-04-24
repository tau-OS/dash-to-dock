if get_option('prefix') != '/usr'
    locale_dir = join_paths(get_option('datadir'), 'gnome-shell', 'extensions', app_id, 'locale')
else
    locale_dir = get_option('localedir')
endif

i18n.gettext(
	'dashtodock',
	preset: 'glib',
    install_dir: locale_dir
)