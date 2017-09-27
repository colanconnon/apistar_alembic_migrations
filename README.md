# Alembic migrations for apistar


### To Install this library


```
pip3 install git+https://github.com/colanconnon/apistar_alembic_migrations.git#egg=apistar_alembic_migrations --upgrade
```


### Register the commands


```
from apistar_alembic_migrations import commands


app = App(
    routes=routes,
    settings=settings,
    commands=commands,  
    components=sqlalchemy_backend.components
)
```

### To generation the initial migrations structure

```
apistar initialaize
```


### The following commands will become avaiable


```
apistar initialize

apistar create_revision "message"

apistar upgrade <"revision id" or Head for latest>

apistar downgrade "revision id"

```

### Enabling auto generating of migrations from models

* open your env.py file in your migrations folder

* find the line that contains
```
target_metadata = None
```

* Import your Declartive Base variable and assign the metadata

```
from app import Base
target_metadata = Base.metadata
```