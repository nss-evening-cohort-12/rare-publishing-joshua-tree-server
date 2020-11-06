from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from users import get_users_by_email, create_user, get_all_users
from posts import create_post, get_all_posts
from tags import create_tag, get_all_tags
from categories import create_category, get_all_categories

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split('/')
        resource = path_params[1]
        if "?" in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return ( resource, key, value )
        else:
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass
            return (resource, id)
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            ( resource, id ) = parsed
            if resource == 'users':
                if id is not None:
                    pass
                else:
                    response = f"{get_all_users()}"

            elif resource == 'posts':
                if id is not None:
                    pass
                else:
                    response = f"{get_all_posts()}"

            elif resource == 'tags':
                if id is not None:
                    pass
                else:
                    response = f"{get_all_tags()}"

            elif resource == 'categories':
                if id is not None:
                    pass
                else:
                    response = f"{get_all_categories()}"

        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            # Is the resource `customers` and was there a
            # query parameter that specified the customer
            # email as a filtering value?
            if key == "email" and resource == "login":
                response = get_users_by_email(value)
        self.wfile.write(response.encode())        

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        new_object = None

        # I had to change the user to register to can be register from the FrontEnd Client side
        if resource == 'register':
            new_object = create_user(post_body)
        elif resource == 'login':
            new_object = get_users_by_email(post_body['username'], post_body['password'])
            #new_object['valid'] = True
        elif resource == 'new-post':
            new_object = create_post(post_body)
        elif resource == 'new-tag':
            new_object = create_tag(post_body)
        elif resource == 'categories':
            new_category = None
            new_category = create_category(post_body)
            self.wfile.write(f"{new_category}".encode())

        self.wfile.write(f"{new_object}".encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
