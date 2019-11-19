def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('async_get', '/async_get')
    config.add_route('async_get2', '/async_get2')

    config.add_route('download', '/download')
    config.add_route('download2', '/download2')

    config.add_route('session', '/session')
    config.add_route('session_push', '/session_push')
    config.add_route('session_clear', '/session_clear')

