import os
from flask import Flask

template_dir = os.path.abspath('./Src/Templates')

app = Flask(__name__,
            template_folder=template_dir,
            static_url_path="/Public",
            static_folder='Public')