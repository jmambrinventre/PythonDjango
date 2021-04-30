import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dir/sqlite//db.sqlite3'),
    }
}

POSTSGRESSQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'Jemv1840497',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# MYREMOTESQL = {
#      'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          'NAME': 'msCJDTHNpy',
#          'USER': 'msCJDTHNpy',
#          'PASSWORD': 'ypqR2FFP8k',
#          'HOST': 'remotemysql.com',
#          'PORT': '3306'
#     }
# }
# Nombre de usuario: msCJDTHNpy

# Nombre de la base de datos: msCJDTHNpy

# Contraseña: MRvlD4I4pn

# Servidor: remotemysql.com

# Puerto: 3306