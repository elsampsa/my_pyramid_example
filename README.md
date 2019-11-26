# Pyramid Playground
*(a notebook mainly for myself)*

## Install

### Prerequisites
```
sudo apt-get install redis-server
```

### Install
```
pip3 install --user -e .
```

### Run
```
pserve --reload development.ini 
```

## Routes & Views

### Main view
```
renders    : home.jinja2 => base.jinja2
route name : home
subaddress : /
view       : views/default.py
```

### Asynchronous GET
- When pressing a button, makes an asynchronous query to the server
- Once the query is done, update the page with new data
```
renders    : async_get.jinja2 => base.jinja2
route name : async_get
subaddress : /async_get
view       : views/default.py
```
- The GET query is done to this address & it returns json:
```
renders    : json
route name : async_get2
subaddress : /async_get2
view       : views/default.py
```

### Download
- Give files to the user for downloading
```
renders    : download.jinja2 => base.jinja2
route name : download
subaddress : /download
view       : views/default.py
```
- File comes from here:
```
renders    : (none)
route name : download2
subaddress : /download2
view       : views/default.py
```

### Session
- Keep session-dependent data
- Each time when user clicks a button, a new entry to the session cache (redis) is created
```
renders    : session.jinja2 => base.jinja2
route name : session
subaddress : /session           ui
subaddress : /session_push      push more data to cache
subaddress : /session_clear     clear all data from cache
view       : views/session.py
```

### Shaka Videoplayer
- Demoes google's shaka dash media player.  See [here](https://shaka-player-demo.appspot.com/docs/api/tutorial-basic-usage.html)
- Shaka's ```dist/shaka-player.compiled*``` dir is copied to ```static/shaka/```
- For generating ```.mpd``` playlist, use shaka packager.  Build instructions are [here](https://github.com/google/shaka-packager/blob/master/docs/source/build_instructions.md)
- ..it uses "gyp" to generate makefiles & build.  Complicated, but the instructions are in that link.  So much work just to generate a few xml files.. :/
- How to use it, see [here](https://google.github.io/shaka-packager/html/tutorials/basic_usage.html)
```
renders    : shaka.jinja2 => base.jinja2
route name : shaka
view       : views/default.py
```
