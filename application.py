
""" Module summary:
"""

from itemcatalog import application

############################################################################


if __name__ == "__main__":
  application.secret_key = "super_secret_key"
  application.debug = True
  application.run(host = "0.0.0.0", port = 5000)



# To do: fix oauth2client library problem
# To do: fix broken file structure. It was working before; did some thing 
#         about flask change?