# Priscilla Fx

This project is created as an online store and information resource for the Priscilla Fx workshop.

<p align="center">
    <img src="docs/img/0.png" alt="0"/>
</p>

## Deploy

```sh
$ git clone https://github.com/priscilla-it/priscillafx_web
$ cd priscillafx_web
$ docker compose up --build
$ sudo chmod +x start
$ ./start
```

## Database Migration Cheat Sheet

`uv run COMMAND`

| Command                                      | Description                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------------ |
| alembic revision --autogenerate -m 'initial' | Creates a new migration by automatically detecting changes in the models.            |
| alembic upgrade head                         | Applies all unapplied migrations up to the latest version.                           |
| alembic downgrade -1                         | Rolls back the last applied migration.                                               |
| alembic stamp head                           | Marks the database as updated to the latest version without applying actual changes. |
| alembic history                              | Shows the history of applied migrations.                                             |
| alembic current                              | Displays the current version of the database.                                        |

## Struct

<p align="center">
    <img src="docs/img/diagram.svg" alt="diagram" width="1024px"/>
</p>

## Preview

<p align="center">
    <img src="docs/img/1.png" alt="1"/>
    <img src="docs/img/2.png" alt="2"/>
    <img src="docs/img/3.png" alt="3"/>
</p>

## License

Priscilla Fx is licensed under the GPL-3.0 License. You can view the full license text in the [LICENSE](LICENSE) file in the repository.
