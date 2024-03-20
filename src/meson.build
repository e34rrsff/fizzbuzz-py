pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'fizzbuzz_py')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
    input: 'fizzbuzz-py.in',
    output: 'fizzbuzz-py',
    configuration: conf,
    install: true,
    install_dir: get_option('bindir')
)

fizzbuzz_py_sources = [
    'main.py',
    'functions.py',
]

install_data(fizzbuzz_py_sources, install_dir: moduledir)
