#!/usr/bin/env python
import logging
from application import app


logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    app.run()
