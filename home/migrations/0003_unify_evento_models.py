from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_categoria_options_alter_evento_options_and_more"),
        ("home", "0002_role"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.DeleteModel(
                    name="Evento",
                ),
            ],
            state_operations=[
                migrations.DeleteModel(
                    name="Evento",
                ),
                migrations.RenameModel(
                    old_name="EventoBase",
                    new_name="Evento",
                ),
            ],
        ),
    ]