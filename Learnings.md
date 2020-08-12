### For building apps with opencv on heroku
  1. We have to use https://github.com/heroku/heroku-buildpack-apt this buildpack on heroku
  2. Also, we need to create an Aptfile and add following dependencies to it: libsm6 libxrender1 libfontconfig1 libice6

### setting environment variables for heroku app
  * refer this - https://github.com/MirelaI/flask_heroku_example
