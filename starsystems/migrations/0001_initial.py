# Generated by Django 4.2.6 on 2024-01-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_id_name', models.TextField(db_column='div_id_NAME')),
                ('name_name', models.TextField(db_column='name_NAME')),
                ('size_int', models.IntegerField(db_column='size_INT')),
                ('prime_color_any', models.TextField(db_column='prime_color_ANY')),
                ('second_color_any', models.TextField(db_column='second_color_ANY')),
                ('shadow_color_any', models.TextField(db_column='shadow_color_ANY')),
                ('shadow_power_int_px', models.IntegerField(db_column='shadow_power_INT_PX')),
                ('orbit_size_int_vmin', models.IntegerField(db_column='orbit_size_INT_VMIN')),
                ('orbit_time_int_s', models.IntegerField(db_column='orbit_time_INT_S')),
            ],
            options={
                'db_table': 'objects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ObjectTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.TextField(db_column='type_NAME')),
            ],
            options={
                'db_table': 'object_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Panels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_id_name', models.TextField(db_column='div_id_NAME')),
            ],
            options={
                'db_table': 'panels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PanelTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_name', models.TextField(db_column='name_NAME')),
                ('args_len_int', models.IntegerField(db_column='args_len_INT')),
            ],
            options={
                'db_table': 'panel_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_name', models.TextField(db_column='name_NAME')),
                ('prime_color_any', models.TextField(blank=True, db_column='prime_color_ANY', null=True)),
                ('second_color_any', models.TextField(blank=True, db_column='second_color_ANY', null=True)),
                ('shadow_color_any', models.TextField(blank=True, db_column='shadow_color_ANY', null=True)),
                ('univ_thumbnail_text_url', models.TextField(blank=True, db_column='univ_thumbnail_TEXT_URL', null=True)),
                ('icon_path_text_url', models.TextField(blank=True, db_column='icon_path_TEXT_URL', null=True)),
                ('short_desc_text', models.TextField(blank=True, db_column='short_desc_TEXT', null=True)),
            ],
            options={
                'db_table': 'systems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ValueRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_plain', models.TextField(blank=True, db_column='title_PLAIN', null=True)),
                ('text_plain', models.TextField(blank=True, db_column='text_PLAIN', null=True)),
                ('img_src_plain', models.TextField(blank=True, db_column='img_src_PLAIN', null=True)),
                ('color_a_plain', models.TextField(blank=True, db_column='color_a_PLAIN', null=True)),
                ('color_b_plain', models.TextField(blank=True, db_column='color_b_PLAIN', null=True)),
                ('color_c_plain', models.TextField(blank=True, db_column='color_c_PLAIN', null=True)),
                ('is_slider_bool', models.TextField(blank=True, db_column='is_slider_BOOL', null=True)),
                ('h_color_a_plain', models.TextField(blank=True, db_column='h_color_a_PLAIN', null=True)),
                ('h_color_b_plain', models.TextField(blank=True, db_column='h_color_b_PLAIN', null=True)),
                ('h_color_c_plain', models.TextField(blank=True, db_column='h_color_c_PLAIN', null=True)),
                ('close_button_bool', models.TextField(blank=True, db_column='close_button_BOOL', null=True)),
                ('extra_args', models.TextField(blank=True, db_column='extra_ARGS', null=True)),
                ('layout_int', models.IntegerField(db_column='layout_INT')),
            ],
            options={
                'db_table': 'value_row',
                'managed': False,
            },
        ),
    ]
