# This file will be automatically executed by the docker container
from fairness.benchmark import run
from fairness.data.objects.list import add_dataset
from fairness.data.objects.Data import Data
from fairness.preprocess import prepare_data

import pandas as pd

class BankData(Data):
    def __init__(self):
        Data.__init__(self)

    def load_raw_dataset(self):
        data_path = self.get_raw_filename()
        data_frame = pd.read_csv(
            data_path,
            error_bad_lines=False,
            na_values=self.get_missing_val_indicators()
        )
        # Convert the all binary attributes to integers
        data_frame.replace({False: 0, True: 1}, inplace=True)
        return data_frame


class BankA(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-0-['job_and_age']-age >= 35; job: privileged vs. unprivileged-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['job_and_age']
        self.privileged_class_names = [ 1 ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'job_and_age', 'target',
            'campaign', 'cons.conf.idx', 'cons.price.idx', 'contact_cellular', 'contact_telephone', 'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed', 'default_no', 'default_unknown', 'default_yes', 'duration', 'education_basic.4y', 'education_basic.6y', 'education_basic.9y', 'education_high.school', 'education_illiterate', 'education_professional.course', 'education_university.degree', 'education_unknown', 'emp.var.rate', 'euribor3m', 'housing_no', 'housing_unknown', 'housing_yes', 'loan_no', 'loan_unknown', 'loan_yes', 'marital_divorced', 'marital_married', 'marital_single', 'marital_unknown', 'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep', 'nr.employed', 'pdays', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success', 'previous'
        ]
        self.missing_val_indicators = ['?']


class BankB(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-0-['age']-age >= 25 and age < 60-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['age']
        self.privileged_class_names = [ 1 ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'campaign', 'cons.conf.idx', 'cons.price.idx', 'contact_cellular', 'contact_telephone', 'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed', 'default_no', 'default_unknown', 'default_yes', 'duration', 'education_basic.4y', 'education_basic.6y', 'education_basic.9y', 'education_high.school', 'education_illiterate', 'education_professional.course', 'education_university.degree', 'education_unknown', 'emp.var.rate', 'euribor3m', 'housing_no', 'housing_unknown', 'housing_yes', 'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired', 'job_self-employed', 'job_services', 'job_student', 'job_technician', 'job_unemployed', 'job_unknown', 'loan_no', 'loan_unknown', 'loan_yes', 'marital_divorced', 'marital_married', 'marital_single', 'marital_unknown', 'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep', 'nr.employed', 'pdays', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success', 'previous', 'target', 'age'
        ]
        self.missing_val_indicators = ['?']

class BankC(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-0-['age']-age >= 25-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['age']
        self.privileged_class_names = [ 1 ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'campaign', 'cons.conf.idx', 'cons.price.idx', 'contact_cellular', 'contact_telephone', 'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed', 'default_no', 'default_unknown', 'default_yes', 'duration', 'education_basic.4y', 'education_basic.6y', 'education_basic.9y', 'education_high.school', 'education_illiterate', 'education_professional.course', 'education_university.degree', 'education_unknown', 'emp.var.rate', 'euribor3m', 'housing_no', 'housing_unknown', 'housing_yes', 'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired', 'job_self-employed', 'job_services', 'job_student', 'job_technician', 'job_unemployed', 'job_unknown', 'loan_no', 'loan_unknown', 'loan_yes', 'marital_divorced', 'marital_married', 'marital_single', 'marital_unknown', 'month_apr', 'month_aug', 'month_dec', 'month_jul', 'month_jun', 'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep', 'nr.employed', 'pdays', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success', 'previous', 'target', 'age'
        ]
        self.missing_val_indicators = ['?']

class BankD(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-2-['age']-?-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['age']
        self.privileged_class_names = [ 1 ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'balance','campaign','contact_cellular','contact_telephone','contact_unknown','day','default_no','default_yes','duration','education_primary','education_secondary','education_tertiary','education_unknown','housing_no','housing_yes','job_admin.','job_blue-collar','job_entrepreneur','job_housemaid','job_management','job_retired','job_self-employed','job_services','job_student','job_technician','job_unemployed','job_unknown','loan_no','loan_yes','marital_divorced','marital_married','marital_single','month_apr','month_aug','month_dec','month_feb','month_jan','month_jul','month_jun','month_mar','month_may','month_nov','month_oct','month_sep','pdays','poutcome_failure','poutcome_other','poutcome_success','poutcome_unknown','previous','target','age'
        ]
        self.missing_val_indicators = ['?']

class BankE(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-2-['job']-none-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['job']
        self.privileged_class_names = [ "privileged" ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'age','balance','campaign','contact_cellular','contact_telephone','contact_unknown','day','default_no','default_yes','duration','education_primary','education_secondary','education_tertiary','education_unknown','housing_no','housing_yes','loan_no','loan_yes','marital_divorced','marital_married','marital_single','month_apr','month_aug','month_dec','month_feb','month_jan','month_jul','month_jun','month_mar','month_may','month_nov','month_oct','month_sep','pdays','poutcome_failure','poutcome_other','poutcome_success','poutcome_unknown','previous','target','job'
        ]
        self.missing_val_indicators = ['?']

    def load_raw_dataset(self):
        data_path = self.get_raw_filename()
        data_frame = pd.read_csv(
            data_path,
            error_bad_lines=False,
            na_values=self.get_missing_val_indicators()
        )
        # Convert the all binary attributes to integers
        data_frame.replace({False: 0, True: 1}, inplace=True)

        # Turn into priveleged / unprivileged to match paper
        data_frame["job"] = data_frame["job"].replace({
            'management': "privileged",
            'technician': "privileged",
            'admin.': "privileged",
            'self-employed': "privileged",
            'entrepreneur': "privileged",
            'blue-collar': "unprivileged",
            'services': "unprivileged",
            'retired': "unprivileged",
            'unemployed': "unprivileged",
            'housemaid': "unprivileged",
            'student': "unprivileged",
            'unknown': "unprivileged",
        })

        return data_frame

class BankF(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-2-['marital']-marital == married-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['marital']
        self.privileged_class_names = [ 1 ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'age','balance','campaign','contact_cellular','contact_telephone','contact_unknown','day','default_no','default_yes','duration','education_primary','education_secondary','education_tertiary','education_unknown','housing_no','housing_yes','job_admin.','job_blue-collar','job_entrepreneur','job_housemaid','job_management','job_retired','job_self-employed','job_services','job_student','job_technician','job_unemployed','job_unknown','loan_no','loan_yes','month_apr','month_aug','month_dec','month_feb','month_jan','month_jul','month_jun','month_mar','month_may','month_nov','month_oct','month_sep','pdays','poutcome_failure','poutcome_other','poutcome_success','poutcome_unknown','previous','target','marital'
        ]
        self.missing_val_indicators = ['?']


class BankG(BankData):
    def __init__(self):
        BankData.__init__(self)
        self.dataset_name = "ORG-017-DS-2-['marital']-none-full_data"
        self.class_attr = 'target'
        self.positive_class_val = 1
        self.sensitive_attrs = ['marital']
        self.privileged_class_names = [ 'married' ]
        self.categorical_features = [ ]
        self.features_to_keep = [
            'age','balance','campaign','contact_cellular','contact_telephone','contact_unknown','day','default_no','default_yes','duration','education_primary','education_secondary','education_tertiary','education_unknown','housing_no','housing_yes','job_admin.','job_blue-collar','job_entrepreneur','job_housemaid','job_management','job_retired','job_self-employed','job_services','job_student','job_technician','job_unemployed','job_unknown','loan_no','loan_yes','month_apr','month_aug','month_dec','month_feb','month_jan','month_jul','month_jun','month_mar','month_may','month_nov','month_oct','month_sep','pdays','poutcome_failure','poutcome_other','poutcome_success','poutcome_unknown','previous','target','marital'
        ]
        self.missing_val_indicators = ['?']

new_datasets = [
    BankA(),
    BankB(),
    BankC(),
    BankD(),
    BankE(),
    BankF(),
    BankG(),
]

for dataset in new_datasets:
    add_dataset(dataset)

dataset_names = []
for dataset in new_datasets:
    dataset_names.append(dataset.get_dataset_name())

# Preprocess data
prepare_data(dataset_names = dataset_names)

# Run benchmark
run(num_trials = 10, dataset = dataset_names)
