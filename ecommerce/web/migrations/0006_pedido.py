# Generated by Django 3.2 on 2023-10-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_cliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('nro_pedido', models.CharField(max_length=20, null=True)),
                ('monto_total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('estado', models.CharField(choices=[('S', 'SOLICITADO'), ('P', 'PAGADO')], default='S', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.cliente')),
            ],
        ),
    ]
