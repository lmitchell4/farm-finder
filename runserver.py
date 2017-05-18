
""" Module summary:
"""

from catalog import app

############################################################################


if __name__ == "__main__":
  app.secret_key = "super_secret_key"
  app.debug = True
  app.run(host = "0.0.0.0", port = 5000)



# To do: fix oauth2client library problem
# To do: fix broken file structure. It was working before; did some thing 
#         about flask change?