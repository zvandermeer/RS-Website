# Generated by Django 4.0.5 on 2022-06-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_response_q1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='q1',
            field=models.CharField(choices=[('1', 'Reincarnation'), ('2', 'Go to a holy place'), ('3', 'Nothing')], max_length=10, verbose_name='What do you believe happens after you die?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q10',
            field=models.CharField(choices=[('1', 'No specific way'), ('2', 'The heavens and earth were created in six days, and on the seventh day, God rested.'), ('3', 'The God(s) created it and it is just an extension of the God(s)')], max_length=10, verbose_name='How do you think the world/universe was created?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q11',
            field=models.CharField(choices=[('1', 'Through the clergy'), ('2', 'Personal Relationship')], max_length=10, verbose_name='Do you wish to attain spiritual enlightenment through you or religious authorities?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q2',
            field=models.CharField(choices=[('1', 'One (Monotheistic)'), ('2', 'More than one God'), ('3', 'More than one aspect of one God'), ('4', 'None')], max_length=10, verbose_name='How many deities are in your religion?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q3',
            field=models.CharField(choices=[('1', 'Regimented prayer schedule'), ('2', 'Recommended prayer'), ('3', 'Meditation'), ('4', 'Group prayer')], max_length=10, verbose_name='Types And Amount Of Prayer?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q4',
            field=models.CharField(choices=[('1', 'Eating And Drinking Restrictions'), ('2', 'Fasting'), ('3', 'Who you can marry'), ('4', 'No Pre-marital sex'), ('5', 'Virtually None'), ('6', 'No Cutting hair'), ('7', 'Gender Identity/Sexuality')], max_length=10, verbose_name='What kind of rules and restrictions do you find acceptable?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q5',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=10, verbose_name='Do you want to travel/go on a pilgrimage?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q6',
            field=models.CharField(choices=[('1', 'Worships in a building of religious significance of a specific week day each week'), ('2', 'Often happens in a building of religious significance but sometimes happens in an informal setting, on a specific day of the week'), ('3', 'Worship is not on a specific day, or no common gathering place')], max_length=10, verbose_name='Preferred type of meeting place for your religious gatherings'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q7',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=10, verbose_name='Does sitting with people of the opposite sex distract you from the service?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q8',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=10, verbose_name='Do you want your place of worship to open during non-service times for personal prayer?'),
        ),
        migrations.AlterField(
            model_name='response',
            name='q9',
            field=models.CharField(choices=[('1', 'Start showing up'), ('2', 'Specific ritual'), ('3', 'Through birth or a special council')], max_length=10, verbose_name='Preferred method of joining a religion'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
