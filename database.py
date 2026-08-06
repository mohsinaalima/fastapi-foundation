from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./reviews.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    """Create all the tables in defines by SQLModel subclasses."""
    SQLModel.metadata.create_all(engine)

    def get_session():
        """Dependency that provides a database session per request"""
        
    