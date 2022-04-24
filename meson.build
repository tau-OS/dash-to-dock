project(
    'tau-dash-to-dock',
    version: '72',
    meson_version: '>= 0.59.0',
    default_options: [ 'warning_level=2', ]
)

app_id = 'dash-to-dock@tauos.co'

sassc = find_program('sassc')
gnome = import('gnome')
i18n = import('i18n')

install_dir = join_paths(get_option('datadir'), 'gnome-shell', 'extensions', app_id)

scss_sources = [
    '_stylesheet.scss',
]

sources = [
    'README.md',
    'COPYING',
    'metadata.json',
    'extension.js',
    'dash.js',
    'docking.js',
    'appIcons.js',
    'appIconIndicators.js',
    'fileManager1API.js',
    'launcherAPI.js',
    'locations.js',
    'windowPreview.js',
    'intellihide.js',
    'prefs.js',
    'theming.js',
    'utils.js',
    'dbusmenuUtils.js',
    'Settings.ui',
    'desktopIconsIntegration.js',
]

foreach f : scss_sources
    custom_target('generate_' + f,
        input: f,
        output: f.replace('_', '').replace('scss', 'css'),
        command: [sassc, '--omit-map-comment', '@INPUT@', '@OUTPUT@'],
        build_by_default: true,
        install: true,
        install_dir: install_dir
    )
endforeach

subdir('schemas')
subdir('po')
subdir('media')

if get_option('prefix') == '/usr'
	gnome.post_install(
        glib_compile_schemas: true,
    )
endif

install_data(
    sources: sources,
    install_dir: install_dir
)
