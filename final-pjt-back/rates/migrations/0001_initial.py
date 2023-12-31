# Generated by Django 4.2.4 on 2023-11-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RESULT', models.IntegerField(choices=[(1, '성공'), (2, 'DATA코드 오류'), (3, '인증코드 오류'), (4, '일일제한횟수 마감')])),
                ('CUR_UNIT', models.CharField(max_length=255)),
                ('CUR_NM', models.CharField(max_length=255)),
                ('TTB', models.CharField(max_length=255)),
                ('TTS', models.CharField(max_length=255)),
                ('DEAL_BAS_R', models.CharField(max_length=255)),
                ('BKPR', models.CharField(max_length=255)),
                ('YY_EFEE_R', models.CharField(max_length=255)),
                ('TEN_DD_EFEE_R', models.CharField(max_length=255)),
                ('KFTC_DEAL_BAS_R', models.CharField(max_length=255)),
                ('KFTC_BKPR', models.CharField(max_length=255)),
            ],
        ),
    ]
