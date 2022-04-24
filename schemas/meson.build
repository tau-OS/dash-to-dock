if get_option('prefix') != '/usr'
	schema_dir = join_paths(get_option('datadir'), 'gnome-shell', 'extensions', app_id, 'schemas')
else
	schema_dir = join_paths(get_option('datadir'), 'glib-2.0/schemas')
endif

install_data(
	'org.gnome.shell.extensions.dash-to-dock.gschema.xml',
  	install_dir: schema_dir
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  	test('Validate schema file', compile_schemas,
    		args: ['--strict', '--dry-run', meson.current_source_dir()]
  	)
endif

install_data(
	'org.gnome.shell.extensions.dash-to-dock.gschema.override',
  	install_dir: schema_dir
)

if get_option('prefix') != '/usr'
	run_command(compile_schemas, '--strict', meson.current_source_dir())
	install_data(
		'gschemas.compiled',
		install_dir: schema_dir
	)
endif