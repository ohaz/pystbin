from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from app import app, debug, host, port
import views

if __name__ == '__main__':
    if debug:
        app.run(debug=True, port=port, host=host)
    else:
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(port)
        IOLoop.instance().start()
