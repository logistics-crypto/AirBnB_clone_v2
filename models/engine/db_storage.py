# models/engine/db_storage.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base

class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and the session"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session"""
        from models import State, City, User, Place, Review, Amenity
        classes = {'State': State, 'City': City, 'User': User,
                   'Place': Place, 'Review': Review, 'Amenity': Amenity}

        objs = {}
        if cls is not None:
            for obj in self.__session.query(classes[cls]):
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls_name, cls in classes.items():
                for obj in self.__session.query(cls):
                    objs[cls_name + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current database session"""
        from models import State, City, User, Place, Review, Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
