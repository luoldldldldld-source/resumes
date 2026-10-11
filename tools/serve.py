"""Local preview with video seeking. Usage: python tools/serve.py --port 8765"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def send_head(self):
        self.remaining = None
        path = Path(self.translate_path(self.path))
        if path.is_file() and self.headers.get('Range'):
            size = path.stat().st_size
            match = re.fullmatch(r'bytes=(\d*)-(\d*)', self.headers['Range'])
            if not match or not any(match.groups()):
                self.send_error(416)
                return None
            a,b = match.groups()
            start = int(a) if a else max(0,size-int(b))
            end = min(int(b),size-1) if a and b else size-1
            if start > end or start >= size:
                self.send_response(416)
                self.send_header('Content-Range',f'bytes */{size}')
                self.send_header('Content-Length','0')
                self.end_headers()
                return None
            file = path.open('rb')
            file.seek(start)
            self.remaining = end-start+1
            self.send_response(206)
            self.send_header('Content-Type',self.guess_type(str(path)))
            self.send_header('Accept-Ranges','bytes')
            self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
            self.send_header('Content-Length',str(self.remaining))
            self.end_headers()
            return file
        return super().send_head()
    def copyfile(self,source,outputfile):
        try:
            if self.remaining is None:
                return super().copyfile(source,outputfile)
            while self.remaining:
                chunk=source.read(min(65536,self.remaining))
                if not chunk: break
                outputfile.write(chunk)
                self.remaining-=len(chunk)
        except (BrokenPipeError,ConnectionResetError,ConnectionAbortedError):
            pass

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=8765)
    args=parser.parse_args()
    print(f'Preview: http://127.0.0.1:{args.port}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
