import os
from logging.config import fileConfig
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from alembic import context
from logging.config import fileConfig

# --- Load environment variables ---
load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# --- Alembic Config ---
config = context.config

# --- Set database URL dynamically ---
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('POSTGRES_DB')}"
)

# --- Setup logging (optional, for Alembic) ---
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Import your SQLAlchemy Base ---
from database import Base
target_metadata = Base.metadata

# --- Migration functions ---
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# --- Choose mode ---
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
