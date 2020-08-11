# Generated by Django 3.0.9 on 2020-08-10 12:34

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_employer', models.BooleanField(default=False)),
                ('is_jobseeker', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Architecture/Interior Designing', 'Architecture/Interior Designing'), ('Construction/Engineering', 'Construction/Engineering'), ('Commercial/Logistics', 'Commercial/Logistics'), ('Creative/Graphic/Designing', 'Creative/Graphic/Designing'), ('Hospilaty', 'Hospilaty'), ('NGO/INGO/Social Work', 'NGO/INGO/Social Work'), ('Techng/Education', 'Techng/Education'), ('General MGMT./Administration/Operations', 'General MGMT./Administration/Operations'), ('Healthcare/Pharma/Biotech/Medical', 'Healthcare/Pharma/Biotech/Medical'), ('Human Resources/ Org.Development', 'Human Resources/ Org.Development'), ('Sales/Public Relations', 'Sales/Public Relations'), ('Research and Development', 'Research and Development'), ('Production/Maintenance/Quality', 'Production/Maintenance/Quality'), ('Marketing/Advertisement/Custom service', 'Marketing/Advertisement/Custom service'), ('Legal Services', 'Legal Services'), ('Accounting/Finance', 'Accounting/Finance'), ('Banking/Insurance/Finance Services', 'Banking/Insurance/Finance Services'), ('Fashion/Textile Designing', 'Fashion/Textile Designing'), ('Secretarial/Front Office/Data Entry', 'Secretarial/Front Office/Data Entry'), ('IT & Telecommunication', 'IT & Telecommunication'), ('Productive/Securaty Service', 'Productive/Securaty Service'), ('Journalism/Editor/Media', 'Journalism/Editor/Media'), ('Others', 'Others')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Skill')),
            ],
        ),
        migrations.CreateModel(
            name='JobseekerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('FirstName', models.CharField(max_length=30, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=30, verbose_name='Last Name')),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('DateOffBorth', models.DateField(verbose_name='Date Of Birth')),
                ('MarrigeStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=20, verbose_name='Marrige Status')),
                ('Religion', models.CharField(choices=[('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Sikhism', 'Sikhism'), ('Jainism', 'Jainism'), ('Others', 'Others')], max_length=20)),
                ('PhoneNumber', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('Email', models.EmailField(max_length=30, verbose_name='Email Address')),
                ('Nationality', models.CharField(choices=[('Nepali', 'Nepali'), ('Indian', 'Indian'), ('Chineases', 'Chineases'), ('Others', 'Others')], max_length=30, verbose_name='Nationality')),
                ('CurrentAddress', models.CharField(max_length=100, verbose_name='Current Address')),
                ('PernamentAddress', models.CharField(max_length=100, verbose_name='Pernament Address')),
                ('ProfileImage', models.ImageField(upload_to='Jobseeker/Profile_Pictures', verbose_name='Profile Picture')),
                ('Education', models.CharField(choices=[('Intermidate Level Complete', 'Intermidate Level Complete'), ('Bacholer Running/Complete', 'Bacholer Running/Complete'), ('Master Running/Complete', 'Master Running/Complete'), ('Ph. D. Running/Complete', 'Ph. D. Running/Complete'), ('OTHER', 'OTHER')], max_length=100, verbose_name='Education')),
                ('EducationProgram', models.CharField(max_length=200, verbose_name='Education Program')),
                ('EducationBoard', models.CharField(choices=[('NEB', 'NEB'), ('Tribhuvan Univercity', 'Tribhuvan Univercity'), ('Mid-Westran Univercity', 'Mid-Westran Univercity'), ('Architure and Forestry Univercity', 'Architure and Forestry Univercity'), ('Nepal Open Univercity', 'Nepal Open Univercity'), ('Pokhara Univercity', 'Pokhara Univercity'), ('Nepal Sanskrit Univercity', 'Nepal Sanskrit Univercity'), ('Lumbini Buddhist Univercity', 'Lumbini Buddhist Univercity'), ('Far-Western Univercity', 'Far-Western Univercity'), ('Kathmandu Univercity', 'Kathmandu Univercity'), ('Purbanchal Univercity', 'Purbanchal Univercity'), ('Others', 'Others')], max_length=100, verbose_name='Education Board')),
                ('NameOfInstitute', models.CharField(max_length=200, verbose_name='Name Of Institute')),
                ('WorkingExperience', models.IntegerField(default=0, verbose_name='Working Experience')),
                ('WorkedField', models.CharField(max_length=50, null=True, verbose_name='Worked Related Fields')),
                ('WorkedCompanyName', models.CharField(max_length=200, verbose_name='Worked Company Name')),
                ('WorkedCompanyWebsite', models.URLField(verbose_name='Worked Company Website')),
                ('Language', models.CharField(choices=[('Nepali', 'Nepali'), ('English', 'English'), ('Others', 'Others')], max_length=20)),
                ('AboutMe', ckeditor.fields.RichTextField(verbose_name='About Me')),
                ('Facebook', models.URLField(max_length=100)),
                ('Twitter', models.URLField(max_length=100)),
                ('Instagram', models.URLField(max_length=100)),
                ('UploadCv', models.FileField(upload_to='Jobseeker/CVs', verbose_name='Upload Your CV')),
                ('JobCategory', models.ManyToManyField(to='account.Category', verbose_name='Job Category')),
                ('MySkill', models.ManyToManyField(to='account.Skill', verbose_name='My Skill')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('CompanyName', models.CharField(max_length=30, verbose_name='Company Name')),
                ('CompanyLogo', models.ImageField(upload_to='Employer/Company_Logos', verbose_name='Company Logo')),
                ('CompanyOwnership', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private'), ('Government', 'Government'), ('Others', 'Others')], max_length=30, verbose_name='Company Ownership')),
                ('CompanyWebsite', models.URLField(max_length=100, verbose_name='Company Website')),
                ('CompanyEstablishDate', models.DateField(verbose_name='Company Established Date')),
                ('AboutCompany', ckeditor.fields.RichTextField(null=True, verbose_name='About Company')),
                ('CompanyAddress', models.CharField(max_length=100, verbose_name='Company Address')),
                ('TelNo', models.CharField(max_length=15, verbose_name='TelePhone Number')),
                ('MobileNo', models.CharField(max_length=15, verbose_name='Mobile Number')),
                ('Facebook', models.URLField(max_length=100)),
                ('Twitter', models.URLField(max_length=100)),
                ('Instagram', models.URLField(max_length=100)),
                ('FirstName', models.CharField(max_length=30, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=30, verbose_name='Last Name')),
                ('PhoneNumber', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('Email', models.EmailField(max_length=30)),
                ('CompanyCategory', models.ManyToManyField(to='account.Category', verbose_name='Company Category')),
            ],
        ),
    ]
