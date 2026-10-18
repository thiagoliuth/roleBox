from django.db import migrations


def rename_event_table(apps, schema_editor):
    tables = set(schema_editor.connection.introspection.table_names())
    if "home_eventobase" in tables and "home_evento" not in tables:
        evento = apps.get_model("home", "Evento")
        schema_editor.alter_db_table(evento, "home_eventobase", "home_evento")


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_unify_evento_models"),
    ]

    operations = [
        migrations.RunPython(rename_event_table, migrations.RunPython.noop),
    ]
