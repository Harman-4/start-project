# Generated by Django 2.1.3 on 2020-03-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='databaseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Department_Name', models.CharField(max_length=50)),
                ('Programme_Name', models.CharField(max_length=100)),
                ('Student_Status', models.CharField(max_length=5)),
                ('Preference_1', models.CharField(max_length=100)),
                ('Application_Fee', models.DecimalField(decimal_places=1, max_digits=4)),
                ('AppId', models.BigIntegerField()),
                ('EmailId', models.EmailField(max_length=254)),
                ('AltEmailId', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('Submission_Date', models.DateField()),
                ('Payment_Status', models.CharField(max_length=15)),
                ('Gender', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=20)),
                ('PWD', models.SlugField(max_length=5)),
                ('Martial_Status', models.SlugField(max_length=5)),
                ('Mobile_Number', models.BigIntegerField()),
                ('Fathers_Name', models.CharField(max_length=50)),
                ('Mothers_Name', models.CharField(max_length=50)),
                ('Aadhar_Number', models.BigIntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('Preference_2', models.CharField(max_length=100)),
                ('Preference_3', models.CharField(max_length=100)),
                ('Preference_4', models.CharField(max_length=100)),
                ('Institute_Assistantship', models.CharField(max_length=5)),
                ('Financial_Support_Detail', models.CharField(max_length=100)),
                ('Test_Name', models.CharField(max_length=100)),
                ('Year', models.DateField()),
                ('Registration_Id', models.BigIntegerField()),
                ('Discipline', models.CharField(max_length=100)),
                ('Score', models.SmallIntegerField()),
                ('Max_Score', models.SmallIntegerField()),
                ('Valid_Upto', models.DateField()),
                ('Rank', models.BigIntegerField()),
                ('Degree_Name', models.CharField(max_length=100)),
                ('University_Name', models.CharField(max_length=200)),
                ('University_City', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('Institute_Name', models.CharField(max_length=150)),
                ('Year_of_Completion', models.DateField()),
                ('Year_of_Admission', models.DateField()),
                ('Duration', models.SmallIntegerField()),
                ('Rank_in_Institute', models.CharField(max_length=10)),
                ('Result_Status', models.CharField(max_length=20)),
                ('Evaluation_Pattern', models.CharField(max_length=20)),
                ('Grade_Type', models.CharField(max_length=50)),
                ('Sem1_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem1_Maximum_Marks', models.SmallIntegerField()),
                ('Sem1_Percentage', models.CharField(max_length=20)),
                ('Sem2_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem2_Maximum_Marks', models.SmallIntegerField()),
                ('Sem2_Percentage', models.CharField(max_length=20)),
                ('Sem3_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem3_Maximum_Marks', models.SmallIntegerField()),
                ('Sem3_Percentage', models.CharField(max_length=20)),
                ('Sem4_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem4_Maximum_Marks', models.SmallIntegerField()),
                ('Sem4_Percentage', models.CharField(max_length=20)),
                ('Sem5_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem5_Maximum_Marks', models.SmallIntegerField()),
                ('Sem5_Percentage', models.CharField(max_length=20)),
                ('Sem6_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem6_Maximum_Marks', models.SmallIntegerField()),
                ('Sem6_Percentage', models.CharField(max_length=20)),
                ('Sem7_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem7_Maximum_Marks', models.SmallIntegerField()),
                ('Sem7_Percentage', models.CharField(max_length=20)),
                ('Sem8_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Sem8_Maximum_Marks', models.SmallIntegerField()),
                ('Sem8_Percentage', models.CharField(max_length=20)),
                ('Overall_Marks_Obtained', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Overall_Maximum_Marks', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Overall_Percentage', models.DecimalField(decimal_places=3, max_digits=8)),
                ('PE1_Examination', models.CharField(max_length=50)),
                ('PE1_Year', models.DateField()),
                ('PE1_Board', models.CharField(max_length=50)),
                ('PE1_Subjects', models.CharField(max_length=50)),
                ('PE1_Score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE1_MaxScore', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE1_Percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('PE1_Rank', models.CharField(max_length=10)),
                ('PE2_Examination', models.CharField(max_length=50)),
                ('PE2_Year', models.DateField()),
                ('PE2_Board', models.CharField(max_length=50)),
                ('PE2_Subjects', models.CharField(max_length=50)),
                ('PE2_Score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE2_MaxScore', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE2_Percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('PE2_Rank', models.CharField(max_length=10)),
                ('PE3_Examination', models.CharField(max_length=50)),
                ('PE3_Year', models.DateField()),
                ('PE3_Board', models.CharField(max_length=50)),
                ('PE3_Subjects', models.CharField(max_length=50)),
                ('PE3_Score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE3_MaxScore', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PE3_Percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('PE3_Rank', models.CharField(max_length=10)),
                ('ED_Designation', models.CharField(max_length=50)),
                ('ED_Organization', models.CharField(max_length=50)),
                ('ED_From', models.CharField(max_length=50)),
                ('ED_To', models.CharField(max_length=50)),
                ('ED_RolesandResponsibilities', models.CharField(max_length=100)),
                ('ED_Gross_Pay_Monthly', models.CharField(max_length=20)),
                ('P_Papers_Published', models.CharField(max_length=4)),
                ('P_NoofPapersinConference_Proceedings', models.CharField(max_length=4)),
                ('P_NoofPapersinConferenceProceedingsnotPublished', models.CharField(max_length=4)),
                ('P_NoofBookChapters', models.CharField(max_length=4)),
                ('Ref_Name', models.CharField(max_length=30)),
                ('Ref_Organization', models.CharField(max_length=30)),
                ('Ref_EmailId', models.EmailField(max_length=254)),
                ('Ref_Contact_Number', models.BigIntegerField()),
                ('Ref_Address', models.CharField(max_length=50)),
            ],
        ),
    ]
