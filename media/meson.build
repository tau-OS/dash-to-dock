icondir = join_paths(get_option('datadir'), 'gnome-shell', 'extensions', app_id, 'media')

media_files = [
    'glossy.svg',
    'highlight_stacked_bg_h.svg',
    'highlight_stacked_bg.svg',
    'logo.svg',
    'screenshot.jpg',
]

foreach f : media_files
    install_data(
        f,
        install_dir: icondir,
    )
endforeach