def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('clips', 'clips', cache_max_age=3600)

    config.add_route('home', '/')

    config.add_route('async_get', '/async_get')     # async get demo page
    config.add_route('async_get2', '/async_get2')   # async get is performed to this address

    config.add_route('download', '/download')       # download demo page
    config.add_route('download2', '/download2')     # downloadable file is found here

    config.add_route('session', '/session')
    config.add_route('session_push', '/session_push')
    config.add_route('session_clear', '/session_clear')

    config.add_route('shaka','/shaka')
    