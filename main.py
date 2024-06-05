import pandas as pd
import numpy as np
from datetime import datetime

pd.set_option('display.max_columns', 50)

# SPDA - Statin Therapy
# SPDB - Statin Adherence 80%

##TODO
# 1 The first line in the file must be a header row that is an exact match to the name column:
# MemID, Meas, Payer, CE, Event, Epop, Excl, Num, RExcl, RExclD, Age, Gender
# 2 SN3 payer need to change?

# NCQA responses
# 100101 should have 0 in CE, gap in drug coverage?
#   Member 100101 is CE = 0 because they have a gap in enrollment and a gap in pharmacy benefits which counts as
#   two gaps during the measurement year. The allowable gap is only 1 gap of up to 45 days during a year of CE.
# 100241 should have 0 in CE, gap in drug coverage?
#   Member 100241 has a similar scenario. 100101 2020011620220317NYYNNYYYMP N A 100101
#   2022041220221029NYYNNYYYMMON A 100101 2022103020221210NNYNNYYYMMON A 100101 2022121120231231NYYNNYYYMOSN A
# 100290 should be 1 in CE,
#     need to figure out the best way to count only the 45d gap in 2021 and not include 1/1/22 in the gap calculation
#     Member 100290 does not have a gap that exceeds 45 days and only has one so they meet CE criteria.

# Need to f/u on
# 100122 CE, Event should be 1
# 100106 RexclD should be 0, fixed but confirm on
# 100112 Epop should be 0
# 100114 Event should be 1


columns_to_read = ['Value Set Name', 'Code']
excel_df = pd.read_excel('M. HEDIS MY 2022 Volume 2 Value Set Directory 2022-10-12.xlsx',
                         sheet_name='Value Sets to Codes', usecols=columns_to_read)

diabetes_data = excel_df[excel_df["Value Set Name"] == "Diabetes"]  # ICD10 and SNOMED
dm_dx_code_list = diabetes_data["Code"].tolist()

ivd_dx_value_set = excel_df[excel_df["Value Set Name"] == "IVD"]  # ICD10 and SNOMED
ivd_dx_code_list = ivd_dx_value_set["Code"].tolist()

acute_inpatient = excel_df[excel_df["Value Set Name"] == "Acute Inpatient"]  # CPT and SNOMED
acute_inpatient_code_list = acute_inpatient["Code"].tolist()

telehealth_modifier = excel_df[excel_df["Value Set Name"] == "Teheleath Modifier"]  # Modifier
telehealth_modifier_code_list = telehealth_modifier["Code"].tolist()

telehealth_pos = excel_df[excel_df["Value Set Name"] == "Telehealth POS"]  # POS
telehealth_pos_code_list = telehealth_pos["Code"].tolist()

inpatient_stay = excel_df[excel_df["Value Set Name"] == "Inpatient Stay"]  # UBREV
inpatient_stay_code_list = inpatient_stay["Code"].tolist()

nonacute_inpatient_stay = excel_df[excel_df["Value Set Name"] == "Nonacute Inpatient Stay"]  # UBREV and UBTOB
nonacute_inpatient_stay_code_list = nonacute_inpatient_stay["Code"].tolist()

outpatient = excel_df[excel_df["Value Set Name"] == "Outpatient"]  # CPT, HCPCS, SNOMED, UBREV
outpatient_code_list = outpatient["Code"].tolist()

observation = excel_df[excel_df["Value Set Name"] == "Observation"]  # CPT
observation_code_list = observation["Code"].tolist()

telephone_visits = excel_df[excel_df["Value Set Name"] == "Telephone Visits"]  # CPT and SNOMED
telephone_visits_code_list = telephone_visits["Code"].tolist()

online_assessments = excel_df[excel_df["Value Set Name"] == "Online Assessments"]  # CPT and HCPCS
online_assessments_code_list = online_assessments["Code"].tolist()

ed_value_set = excel_df[excel_df["Value Set Name"] == "ED"]  # CPT, SNOMED, UBREV
ed_value_set_code_list = ed_value_set["Code"].tolist()

nonacute_inpatient = excel_df[excel_df["Value Set Name"] == "Nonacute Inpatient"]  # CPT, SNOMED
nonacute_inpatient_code_list = nonacute_inpatient["Code"].tolist()

# Exclusions
mi_value_set = excel_df[excel_df["Value Set Name"] == "MI"]  # ICD10, ICD9, SNOMEd
mi_code_list = mi_value_set["Code"].tolist()

old_mi_value_set = excel_df[excel_df["Value Set Name"] == "Old Myocardial Infarction"]  # ICD10, ICD9, SNOMEd
old_mi_code_list = old_mi_value_set["Code"].tolist()

cabg_value_set = excel_df[excel_df["Value Set Name"] == "CABG"]  # CPT, HCPCS, ICD10, SNOMED
cabg_code_list = cabg_value_set["Code"].tolist()

pci_value_set = excel_df[excel_df["Value Set Name"] == "PCI"]  # CPT, HCPCS, ICD10, SNOMED
pci_code_list = pci_value_set["Code"].tolist()

other_revasc_value_set = excel_df[excel_df["Value Set Name"] == "Other Revascularization"]  # CPT, SNOMED
other_revasc_code_list = other_revasc_value_set["Code"].tolist()

pregnancy_value_set = excel_df[excel_df["Value Set Name"] == "Pregnancy"]  # ICD10 and SNOMED
pregnancy_code_list = pregnancy_value_set["Code"].tolist()

ivf_value_set = excel_df[excel_df["Value Set Name"] == "IVF"]  # HCPCS and SNOMED
ivf_code_list = ivf_value_set["Code"].tolist()

esrd_value_set = excel_df[excel_df["Value Set Name"] == "ESRD Diagnosis"]  # ICD10, ICD9, SNOMED
esrd_code_list = esrd_value_set["Code"].tolist()

dialysis_procedure_value_set = excel_df[excel_df["Value Set Name"] == "Dialysis Procedure"]  # CPT, HCPCS, ICD10, ICD9
dialysis_procedure_code_list = dialysis_procedure_value_set["Code"].tolist()

cirrhosis_value_set = excel_df[excel_df["Value Set Name"] == "Cirrhosis"]  # ICD10, SNOMED
cirrhosis_code_list = cirrhosis_value_set["Code"].tolist()

muscle_pain_value_set = excel_df[excel_df["Value Set Name"] == "Muscular Pain and Disease"]  # ICD10, SNOMED
muscle_pain_code_list = muscle_pain_value_set["Code"].tolist()

pall_care_assessment_value_set = excel_df[excel_df["Value Set Name"] == "Palliative Care Assessment"]  # SNOMED
pall_care_assess_code_list = pall_care_assessment_value_set["Code"].tolist()

pall_care_enc_value_set = excel_df[excel_df["Value Set Name"] == "Palliative Care Encounter"]  # HCPCS, ICD10, SNOMED
pall_care_enc_code_list = pall_care_enc_value_set["Code"].tolist()

pall_care_int_value_set = excel_df[excel_df["Value Set Name"] == "Palliative Care Intervention"]  # SNOMED
pall_care_int_code_list = pall_care_int_value_set["Code"].tolist()

frailty_device_value_set = excel_df[excel_df["Value Set Name"] == "Frailty Device"]  # HCPCS
frailty_device_code_list = frailty_device_value_set["Code"].tolist()

frailty_diagnosis_value_set = excel_df[excel_df["Value Set Name"] == "Frailty Diagnosis"]  # ICD10, SNOMED
frailty_diagnosis_code_list = frailty_diagnosis_value_set["Code"].tolist()

frailty_enc_value_set = excel_df[excel_df["Value Set Name"] == "Frailty Encounter"]  # CPT, HCPCS
frailty_enc_code_list = frailty_enc_value_set["Code"].tolist()

frailty_symptom_value_set = excel_df[excel_df["Value Set Name"] == "Frailty Symptom"]  # ICD10 and SNOMED
frailty_symptom_code_list = frailty_symptom_value_set["Code"].tolist()

advanced_illness_value_set = excel_df[excel_df["Value Set Name"] == "Advanced Illness"]  # ICD10 and SNOMED
advanced_illness_code_list = advanced_illness_value_set["Code"].tolist()

diabetes_exclusions_value_set = excel_df[excel_df["Value Set Name"] == "Diabetes Exclusions"]  # ICD10 and SNOMED
diabetes_exclusions_code_list = diabetes_exclusions_value_set["Code"].tolist()

hospice_encounter_value_set = excel_df[excel_df["Value Set Name"] == "Hospice Encounter"]
hospice_encounter_code_list = hospice_encounter_value_set["Code"].tolist()

hospice_intervention_value_set = excel_df[excel_df["Value Set Name"] == "Hospice Intervention"]
hospice_intervention_code_list = hospice_intervention_value_set["Code"].tolist()

independent_lab_value_set = excel_df[excel_df["Value Set Name"] == "Independent Laboratory"]
independent_lab_code_list = independent_lab_value_set["Code"].tolist()

columns_to_read = ['Medication List Name', 'Code']
medication_list_df = pd.read_excel('HEDIS MY 2022 Medication List Directory 2022-03-31.xlsx', sheet_name='Medication Lists to Codes', usecols=columns_to_read)

dm_meds = medication_list_df[medication_list_df["Medication List Name"] == "Diabetes Medications"]
dm_meds_code_list = dm_meds["Code"].tolist()
dm_meds_code_list = [str(code) for code in dm_meds_code_list]

estrogen_agonist_meds = medication_list_df[medication_list_df["Medication List Name"] == "Estrogen Agonists Medications"]
estrogen_agonist_code_list = estrogen_agonist_meds["Code"].tolist()
estrogen_agonist_code_list = [str(code) for code in estrogen_agonist_code_list]

dementia_meds = medication_list_df[medication_list_df["Medication List Name"] == "Dementia Medications"]
dementia_meds_code_list = dementia_meds["Code"].tolist()
dementia_meds_code_list = [str(code) for code in dementia_meds_code_list]

#High Intensity Statin Therapy
atorvastatin_high_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Atorvastatin High Intensity Medications"]
atorvastatin_high_intensity_code_list = atorvastatin_high_intensity["Code"].tolist()
atorvastatin_high_intensity_code_list = [str(code) for code in atorvastatin_high_intensity_code_list]

amlodipine_atorvastatin_high_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Amlodipine Atorvastatin High Intensity Medications"]
amlodipine_atorvastatin_high_intensity_code_list = amlodipine_atorvastatin_high_intensity["Code"].tolist()
amlodipine_atorvastatin_high_intensity_code_list = [str(code) for code in amlodipine_atorvastatin_high_intensity_code_list]

rosuvastatin_high_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Rosuvastatin High Intensity Medications"]
rosuvastatin_high_intensity_code_list = rosuvastatin_high_intensity["Code"].tolist()
rosuvastatin_high_intensity_code_list = [str(code) for code in rosuvastatin_high_intensity_code_list]

simvastatin_high_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Simvastatin High Intensity Medications"]
simvastatin_high_intensity_code_list = simvastatin_high_intensity["Code"].tolist()
simvastatin_high_intensity_code_list = [str(code) for code in simvastatin_high_intensity_code_list]

ezetimibe_simvastatin_high_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Ezetimibe Simvastatin High Intensity Medications"]
ezetimibe_simvastatin_high_intensity_code_list = ezetimibe_simvastatin_high_intensity["Code"].tolist()
ezetimibe_simvastatin_high_intensity_code_list = [str(code) for code in ezetimibe_simvastatin_high_intensity_code_list]

#Moderate Intensity Statin Therapy
atorvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Atorvastatin Moderate Intensity Medications"]
atorvastatin_mod_intensity_code_list = atorvastatin_mod_intensity["Code"].tolist()
atorvastatin_mod_intensity_code_list = [str(code) for code in atorvastatin_mod_intensity_code_list]

amlodipine_atorvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Amlodipine Atorvastatin Moderate Intensity Medications"]
amlodipine_atorvastatin_mod_intensity_code_list = amlodipine_atorvastatin_mod_intensity["Code"].tolist()
amlodipine_atorvastatin_mod_intensity_code_list = [str(code) for code in amlodipine_atorvastatin_mod_intensity_code_list]

rosuvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Rosuvastatin Moderate Intensity Medications"]
rosuvastatin_mod_intensity_code_list = rosuvastatin_mod_intensity["Code"].tolist()
rosuvastatin_mod_intensity_code_list = [str(code) for code in rosuvastatin_mod_intensity_code_list]
rosuvastatin_mod_intensity_code_list = rosuvastatin_mod_intensity_code_list[1:]

simvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Simvastatin Moderate Intensity Medications"]
simvastatin_mod_intensity_code_list = simvastatin_mod_intensity["Code"].tolist()
simvastatin_mod_intensity_code_list = [str(code) for code in simvastatin_mod_intensity_code_list]

ezetimibe_simvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Ezetimibe Simvastatin Moderate Intensity Medications"]
ezetimibe_simvastatin_mod_intensity_code_list = ezetimibe_simvastatin_mod_intensity["Code"].tolist()
ezetimibe_simvastatin_mod_intensity_code_list = [str(code) for code in ezetimibe_simvastatin_mod_intensity_code_list]

pravastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Pravastatin Moderate Intensity Medications"]
pravastatin_mod_intensity_code_list = pravastatin_mod_intensity["Code"].tolist()
pravastatin_mod_intensity_code_list = [str(code) for code in pravastatin_mod_intensity_code_list]

lovastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Lovastatin Moderate Intensity Medications"]
lovastatin_mod_intensity_code_list = lovastatin_mod_intensity["Code"].tolist()
lovastatin_mod_intensity_code_list = [str(code) for code in lovastatin_mod_intensity_code_list]

fluvastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Fluvastatin Moderate Intensity Medications"]
fluvastatin_mod_intensity_code_list = fluvastatin_mod_intensity["Code"].tolist()
fluvastatin_mod_intensity_code_list = [str(code) for code in fluvastatin_mod_intensity_code_list]

pitavastatin_mod_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Pitavastatin Moderate Intensity Medications"]
pitavastatin_mod_intensity_code_list = pitavastatin_mod_intensity["Code"].tolist()
pitavastatin_mod_intensity_code_list = [str(code) for code in pitavastatin_mod_intensity_code_list]

#Low Intensity Statin Therapy
simvastatin_low_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Simvastatin Low Intensity Medications"]
simvastatin_low_intensity_code_list = simvastatin_low_intensity["Code"].tolist()
simvastatin_low_intensity_code_list = [str(code) for code in simvastatin_low_intensity_code_list]

ezetimibe_simvastatin_low_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Ezetimibe Simvastatin Low Intensity Medications"]
ezetimibe_simvastatin_low_intensity_code_list = ezetimibe_simvastatin_low_intensity["Code"].tolist()
ezetimibe_simvastatin_low_intensity_code_list = [str(code) for code in ezetimibe_simvastatin_low_intensity_code_list]

pravastatin_low_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Pravastatin Low Intensity Medications"]
pravastatin_low_intensity_code_list = pravastatin_low_intensity["Code"].tolist()
pravastatin_low_intensity_code_list = [str(code) for code in pravastatin_low_intensity_code_list]

lovastatin_low_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Lovastatin Low Intensity Medications"]
lovastatin_low_intensity_code_list = lovastatin_low_intensity["Code"].tolist()
lovastatin_low_intensity_code_list = [str(code) for code in lovastatin_low_intensity_code_list]

fluvastatin_low_intensity = medication_list_df[medication_list_df["Medication List Name"] == "Fluvastatin Low Intensity Medications"]
fluvastatin_low_intensity_code_list = fluvastatin_low_intensity["Code"].tolist()
fluvastatin_low_intensity_code_list = [str(code) for code in fluvastatin_low_intensity_code_list]

column_widths = [16,8,8,1,1,1,1,1,1,1,1,3,1,10]

column_data = [[] for _ in range(len(column_widths))]

with open('member-en.txt') as file:
  for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_member = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_member = df_member.rename(columns={'Column_1': 'Member ID'})
df_member = df_member.rename(columns={'Column_2': 'Start Date'})
df_member = df_member.rename(columns={'Column_3': 'Disenrollment Date'})
df_member = df_member.rename(columns={'Column_4': 'Dental'})
df_member = df_member.rename(columns={'Column_5': 'Drug Benefit'})
df_member = df_member.rename(columns={'Column_6': 'Inpt Mental Health Benefit'})
df_member = df_member.rename(columns={'Column_12': 'Payer'})
df_member = df_member.rename(columns={'Column_13': 'Health Plan Employee'})
df_member['Member ID']=df_member['Member ID'].astype(int)
df_member['Start Date'] = pd.to_datetime(df_member['Start Date'], format='%Y%m%d')
df_member['Disenrollment Date'] = pd.to_datetime(df_member['Disenrollment Date'], format='%Y%m%d')
# Calculate the gap in days for each Member ID
df_member['Gap (Days)'] = df_member.groupby('Member ID')['Start Date'].shift(-1) - df_member['Disenrollment Date']
# Convert timedelta to integer days
df_member['Gap (Days)'] = df_member['Gap (Days)'].dt.days

df_member_2022 = df_member[(df_member['Disenrollment Date'] >= '2022-01-01') | (df_member['Start Date'] >= '2022-01-01')]



column_widths = [16, 1, 8, 20, 20, 1, 16, 50, 50, 30, 2, 5, 10, 25, 1, 25,2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

column_data = [[] for _ in range(len(column_widths))]

with open('member-gm.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_member_gm = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_member_gm = df_member_gm.rename(columns={'Column_1': 'Member ID'})
df_member_gm = df_member_gm.rename(columns={'Column_2': 'Gender'})
df_member_gm = df_member_gm.rename(columns={'Column_3': 'DOB'})
df_member_gm['Member ID']=df_member_gm['Member ID'].astype(int)

df_member_gm['DOB'] = pd.to_datetime(df_member_gm['DOB'])
age_in_2022 = datetime(2022, 12, 31)
age = age_in_2022.year - df_member_gm['DOB'].dt.year
is_birthday_passed = (df_member_gm['DOB'].dt.month < age_in_2022.month) | ((df_member_gm['DOB'].dt.month == age_in_2022.month) & (df_member_gm['DOB'].dt.day <= age_in_2022.day))
df_member_gm['Age'] = age - (~is_birthday_passed)

columns_to_drop = [col for col in df_member_gm.columns if col.startswith('Column_')]
df_member_gm.drop(columns=columns_to_drop, inplace=True)

#Filter all members that have active coverage until at least 1/1/21
df_member_active_coverage = df_member[df_member['Disenrollment Date'] >= '2021-01-01']
df_member_gm_age_40_75 = df_member_gm[(df_member_gm['Age'] >= 40) & (df_member_gm['Age'] <= 75)]

df_member_sorted = df_member.sort_values(by=['Member ID', 'Start Date'], ascending=[True, False])
df_member_last_payer = df_member_sorted.drop_duplicates(subset='Member ID', keep='first')
payer_last_df = df_member_last_payer[['Member ID', 'Payer']]

female_members_list = df_member_gm[df_member_gm['Gender'] == 'F']['Member ID'].tolist()

#Filter for Payers (Medicaid, MMP, and all others)
medicaid_filter_df = df_member_last_payer[df_member_last_payer['Payer'].isin(['MD', 'MDE', 'MLI', 'MRB'])]
medicaid_id_list = set(medicaid_filter_df['Member ID'])
mmp_filter_df = df_member_last_payer[df_member_last_payer['Payer'].isin(['MMP'])]
mmp_id_list = set(mmp_filter_df['Member ID'])
other_plans_filter_df = df_member_last_payer[~df_member_last_payer['Payer'].isin(['MD', 'MDE', 'MLI', 'MRB', 'MMP'])]
other_plans_id_list = set(other_plans_filter_df['Member ID'])

df_member_medicaid = df_member_active_coverage[df_member_active_coverage['Member ID'].isin(medicaid_id_list)]
df_member_mmp = df_member_active_coverage[df_member_active_coverage['Member ID'].isin(mmp_id_list)]
df_member_other_plans = df_member_active_coverage[df_member_active_coverage['Member ID'].isin(other_plans_id_list)]

df_member_medicaid.loc[:, 'Gap (Days)'] = df_member_medicaid['Gap (Days)'].fillna(-1)
df_member_mmp.loc[:, 'Gap (Days)'] = df_member_mmp['Gap (Days)'].fillna(-1)
df_member_other_plans.loc[:, 'Gap (Days)'] = df_member_other_plans['Gap (Days)'].fillna(-1)

#Filter all members in medicaid filter that have more than one gap or a gap > 60 days
df_medicaid_with_no_60d_gap = df_member_medicaid.groupby('Member ID').filter(lambda x: (x['Gap (Days)'] <= 60).all())
medicaid_member_ids_to_remove = df_medicaid_with_no_60d_gap.groupby('Member ID').apply(lambda x: (x['Gap (Days)'] > 1).sum() > 1)
medicaid_member_ids_to_remove = medicaid_member_ids_to_remove[medicaid_member_ids_to_remove].index
medicaid_no_gaps_df = df_medicaid_with_no_60d_gap[~df_medicaid_with_no_60d_gap['Member ID'].isin(medicaid_member_ids_to_remove)]
medicaid_ids_no_gaps = medicaid_no_gaps_df['Member ID'].unique().tolist()

#Filter all members in mmp filter for >60 day gap and >45 day gap
mmp_no_gaps_60_df = df_member_mmp.groupby('Member ID').filter(lambda x: (x['Gap (Days)'] <= 60).all())
mmp_60_member_ids_to_remove = mmp_no_gaps_60_df.groupby('Member ID').apply(lambda x: (x['Gap (Days)'] > 1).sum() > 1)
mmp_member_ids_to_remove = mmp_60_member_ids_to_remove[mmp_60_member_ids_to_remove].index
mmp_no_gaps_60_df = mmp_no_gaps_60_df[~mmp_no_gaps_60_df['Member ID'].isin(mmp_60_member_ids_to_remove)]
mmp_ids_no_60_gaps = mmp_no_gaps_60_df['Member ID'].unique().tolist()

mmp_no_gaps_45_df = df_member_mmp.groupby('Member ID').filter(lambda x: (x['Gap (Days)'] <= 45).all())
mmp_45_member_ids_to_remove = mmp_no_gaps_45_df.groupby('Member ID').apply(lambda x: (x['Gap (Days)'] > 1).sum() > 1)
mmp_45_member_ids_to_remove = mmp_45_member_ids_to_remove[mmp_45_member_ids_to_remove].index
mmp_no_gaps_45_df = mmp_no_gaps_45_df[~mmp_no_gaps_45_df['Member ID'].isin(mmp_45_member_ids_to_remove)]
mmp_ids_no_45_gaps = mmp_no_gaps_45_df['Member ID'].unique().tolist()

mmp_ids_gap_45_to_60_days = list(set(mmp_ids_no_60_gaps) - set(mmp_ids_no_45_gaps))
mmp_ids_no_45_gaps = list(set(mmp_ids_no_45_gaps) - set(mmp_ids_gap_45_to_60_days))

mmp_gap_45_to_60_days_df = mmp_no_gaps_60_df[mmp_no_gaps_60_df['Member ID'].isin(mmp_ids_gap_45_to_60_days)]
mmp_ids_gap_45_to_60_days = mmp_gap_45_to_60_days_df['Member ID'].unique().tolist()
mmp_no_gaps_45_df = mmp_no_gaps_45_df[mmp_no_gaps_45_df['Member ID'].isin(mmp_ids_no_45_gaps)]
mmp_ids_no_45_gaps = mmp_no_gaps_45_df['Member ID'].unique().tolist()

#Filter all other plan members that have a gap > 45 days
other_plans_no_gaps_df = df_member_other_plans.groupby('Member ID').filter(lambda x: (x['Gap (Days)'] <= 45).all())
other_plan_member_ids_to_remove = other_plans_no_gaps_df.groupby('Member ID').apply(lambda x: (x['Gap (Days)'] > 1).sum() > 1)
other_plan_member_ids_to_remove = other_plan_member_ids_to_remove[other_plan_member_ids_to_remove].index
other_plans_no_gaps_df = other_plans_no_gaps_df[~other_plans_no_gaps_df['Member ID'].isin(other_plan_member_ids_to_remove)]
other_plans_ids_no_gaps = other_plans_no_gaps_df['Member ID'].unique().tolist()

#Filter all members who have coverage on 12/31/22
plans_no_medical_gaps_df = pd.concat([medicaid_no_gaps_df, mmp_gap_45_to_60_days_df, mmp_no_gaps_45_df, other_plans_no_gaps_df])
plans_no_medical_gaps_df = plans_no_medical_gaps_df.sort_values(by='Member ID', ascending=True)

#Filter for all members with pharmacy benefit during MY 2022, remove all memebrs with >1 pharmacy gaps
#pharmacy_filter = plans_no_medical_gaps_df['Drug Benefit'] == 'Y'
disenrollment_filter = ((plans_no_medical_gaps_df['Disenrollment Date'] >= '2022-01-01') | ((plans_no_medical_gaps_df['Disenrollment Date'] >= '2023-01-01') & (plans_no_medical_gaps_df['Start Date'] >= '2022-01-01')))
#combined_pharmacy_disenrollment_filter = plans_no_medical_gaps_df[pharmacy_filter & disenrollment_filter]


all_plans_active_2022_df = plans_no_medical_gaps_df[disenrollment_filter]
all_plans_with_drug_benefit_df = all_plans_active_2022_df.groupby('Member ID').filter(lambda x: any(x['Drug Benefit'] == 'Y'))



#combined_pharmacy_disenrollment_filter = combined_pharmacy_disenrollment_filter.copy()
#combined_pharmacy_disenrollment_filter.loc[:, 'Pharmacy Gap (Days)'] = combined_pharmacy_disenrollment_filter.groupby('Member ID')['Start Date'].shift(-1) - combined_pharmacy_disenrollment_filter['Disenrollment Date']
#combined_pharmacy_disenrollment_filter.loc[:, 'Pharmacy Gap (Days)'] = combined_pharmacy_disenrollment_filter['Pharmacy Gap (Days)'].dt.days
#combined_pharmacy_disenrollment_filter.loc[:, 'Pharmacy Gap (Days)'] = combined_pharmacy_disenrollment_filter['Pharmacy Gap (Days)'].fillna(-1)

all_plans_with_drug_benefit_df['Pharmacy Gap (Days)'] = (all_plans_with_drug_benefit_df['Disenrollment Date'].apply(lambda x: min(pd.Timestamp('2022-12-31'), x)) - all_plans_with_drug_benefit_df['Start Date']).dt.days
all_plans_with_drug_benefit_df.loc[all_plans_with_drug_benefit_df['Drug Benefit'] == 'Y', 'Pharmacy Gap (Days)'] = -1
all_plans_with_drug_benefit_45_gap_df = all_plans_with_drug_benefit_df[all_plans_with_drug_benefit_df['Pharmacy Gap (Days)'] > 45]
member_ids_with_pharmacy_gap_45_days = all_plans_with_drug_benefit_45_gap_df['Member ID'].tolist()
all_plans_with_drug_benefit_no_45_gap_df = all_plans_with_drug_benefit_df[~all_plans_with_drug_benefit_df['Member ID'].isin(member_ids_with_pharmacy_gap_45_days)]
no_pharmacy_gaps = all_plans_with_drug_benefit_no_45_gap_df.groupby('Member ID').apply(lambda x: (x['Pharmacy Gap (Days)'] > 1).sum() <= 1)
no_pharmacy_gaps_to_keep = no_pharmacy_gaps[no_pharmacy_gaps].index
df_no_pharmacy_gaps = all_plans_with_drug_benefit_df[all_plans_with_drug_benefit_df['Member ID'].isin(no_pharmacy_gaps_to_keep)]
no_pharmacy_gaps_list = df_no_pharmacy_gaps['Member ID'].unique().tolist()



anchor_filter = df_no_pharmacy_gaps[(df_no_pharmacy_gaps['Start Date'] <= '2022-12-31') & (df_no_pharmacy_gaps['Disenrollment Date'] >= '2022-12-31')]

#All members who meet CE
ce_total_list = set(anchor_filter['Member ID'])
medicaid_meets_ce = list(medicaid_id_list.intersection(ce_total_list))
mmp_meets_ce = list(mmp_id_list.intersection(ce_total_list))
other_plans_meets_ce = list(other_plans_id_list.intersection(ce_total_list))
continuous_enrollment_met = medicaid_meets_ce + mmp_meets_ce + other_plans_meets_ce


column_widths = [16,8,8,8,5,2,2,5,5,2,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,1,2,4,4,2,1,10,1,2]

column_data = [[] for _ in range(len(column_widths))]

with open('visit.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_visit = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_visit = df_visit.rename(columns={'Column_1': 'Member ID'})
df_visit = df_visit.rename(columns={'Column_2': 'DOS'})
df_visit['DOS'] = pd.to_datetime(df_visit['DOS'])
df_visit = df_visit.rename(columns={'Column_3': 'Admission Date'})
df_visit = df_visit.rename(columns={'Column_4': 'Discharge Date'})
df_visit = df_visit.rename(columns={'Column_5': 'CPT'})
df_visit = df_visit.rename(columns={'Column_6': 'CPT Mod 1'})
df_visit = df_visit.rename(columns={'Column_7': 'CPT Mod 2'})
df_visit = df_visit.rename(columns={'Column_8': 'HCPCS'})
df_visit = df_visit.rename(columns={'Column_9': 'CPT 2'})
df_visit = df_visit.rename(columns={'Column_10': 'CPT 2 Mod'})
df_visit = df_visit.rename(columns={'Column_11': 'ICD-10 1'})
df_visit = df_visit.rename(columns={'Column_12': 'ICD-10 2'})
df_visit = df_visit.rename(columns={'Column_13': 'ICD-10 3'})
df_visit = df_visit.rename(columns={'Column_14': 'ICD-10 4'})
df_visit = df_visit.rename(columns={'Column_15': 'ICD-10 5'})
df_visit = df_visit.rename(columns={'Column_16': 'ICD-10 6'})
df_visit = df_visit.rename(columns={'Column_17': 'ICD-10 7'})
df_visit = df_visit.rename(columns={'Column_18': 'ICD-10 8'})
df_visit = df_visit.rename(columns={'Column_19': 'ICD-10 9'})
df_visit = df_visit.rename(columns={'Column_20': 'ICD-10 10'})
df_visit = df_visit.rename(columns={'Column_21': 'ICD-10 11'})
df_visit = df_visit.rename(columns={'Column_22': 'ICD-10 12'})
df_visit = df_visit.rename(columns={'Column_23': 'ICD-10 13'})
df_visit = df_visit.rename(columns={'Column_24': 'ICD-10 14'})
df_visit = df_visit.rename(columns={'Column_25': 'ICD-10 15'})
df_visit = df_visit.rename(columns={'Column_26': 'ICD-10 16'})
df_visit = df_visit.rename(columns={'Column_27': 'ICD-10 17'})
df_visit = df_visit.rename(columns={'Column_28': 'ICD-10 18'})
df_visit = df_visit.rename(columns={'Column_29': 'ICD-10 19'})
df_visit = df_visit.rename(columns={'Column_30': 'ICD-10 20'})
df_visit = df_visit.rename(columns={'Column_39': 'UBREV'})
df_visit = df_visit.rename(columns={'Column_40': 'UBTOB'})
df_visit = df_visit.rename(columns={'Column_41': 'CMS Place of Service'})
df_visit = df_visit.rename(columns={'Column_42': 'Claim Status'})
df_visit = df_visit.rename(columns={'Column_44': 'Supplemental Data'})
df_visit['Member ID']=df_visit['Member ID'].astype(int)

# list of columns to check
columns_to_check = ['ICD-10 1', 'ICD-10 2', 'ICD-10 3', 'ICD-10 4', 'ICD-10 5', 'ICD-10 6', 'ICD-10 7', 'ICD-10 8', 'ICD-10 9', 'ICD-10 10',
                    'ICD-10 11', 'ICD-10 12', 'ICD-10 13', 'ICD-10 14', 'ICD-10 15', 'ICD-10 16', 'ICD-10 17', 'ICD-10 18', 'ICD-10 19', 'ICD-10 20']

#All visits during measurement year or year prior
df_visit_2021_2022 = df_visit[(df_visit['DOS'].dt.year == 2021) | (df_visit['DOS'].dt.year == 2022)]
df_visit_2021_2022 = df_visit_2021_2022[~(df_visit_2021_2022['CMS Place of Service'].isin(independent_lab_code_list))] #remove all lab encounters see pg 47 #38
df_visit_2021_2022_no_supp = df_visit_2021_2022[(df_visit_2021_2022['Supplemental Data'] == 'N')]
#All visits during year prior to measurement year
df_visit_2021 = df_visit[(df_visit['DOS'].dt.year == 2021)]
df_visit_2021 = df_visit_2021[~(df_visit_2021['CMS Place of Service'].isin(independent_lab_code_list))]
df_visit_2021_no_supp = df_visit_2021[(df_visit_2021['Supplemental Data'] == 'N')]
#All visits during MY2022
df_visit_2022 = df_visit[(df_visit['DOS'].dt.year == 2022)]
df_visit_2022 = df_visit_2022[~(df_visit_2022['CMS Place of Service'].isin(independent_lab_code_list))]
df_visit_2022_no_supp = df_visit_2022[(df_visit_2022['Supplemental Data'] == 'N')]

# All visits with DM ICD-10 codes; Boolean indexing to filter rows where at least one value in columns_to_check is in dm_dx_code_list
df_visit_dm = df_visit_2021_2022_no_supp[df_visit_2021_2022_no_supp[columns_to_check].apply(lambda row: row.isin(dm_dx_code_list)).any(axis=1)]

#All acute inpatient encounters that have DM dx without telehealth modifiers
df_visit_dm_acute_inpt = df_visit_dm[df_visit_dm['CPT'].isin(acute_inpatient_code_list)]
df_visit_dm_no_tele = df_visit_dm_acute_inpt[~((df_visit_dm_acute_inpt['CPT Mod 1'].isin(telehealth_modifier_code_list)) | (df_visit_dm_acute_inpt['CPT Mod 2'].isin(telehealth_modifier_code_list)))]
df_visit_dm_no_tele = df_visit_dm_no_tele[~((df_visit_dm_no_tele['CPT Mod 1'].isin(telehealth_pos_code_list)) | (df_visit_dm_no_tele['CPT Mod 2'].isin(telehealth_pos_code_list)))]
visit_dm_no_tele_list = df_visit_dm_no_tele['Member ID'].unique().tolist()

#At least one acute inpatient discharge with a dx of DM on discharge claim.
df_visit_dm_inpt_stay = df_visit_dm[df_visit_dm['UBREV'].isin(inpatient_stay_code_list)]
df_visit_dm_acute_inpt_stay = df_visit_dm_inpt_stay[~(df_visit_dm_inpt_stay['UBREV'].isin(nonacute_inpatient_stay_code_list) |
                                                      df_visit_dm_inpt_stay['UBTOB'].isin(nonacute_inpatient_stay_code_list) |
                                                      df_visit_dm_inpt_stay['CPT'].isin(nonacute_inpatient_stay_code_list))]
df_visit_dm_acute_inpt_stay_with_dc_date = df_visit_dm_acute_inpt_stay.dropna(subset=['Discharge Date'])
dm_acute_inpt_stay_with_dc_date_list = df_visit_dm_acute_inpt_stay_with_dc_date['Member ID'].unique().tolist()

#At least two outpatient visits (Outpatient Value Set), observation visits (Observation Value Set),
#telephone visits (Telephone Visits Value Set), e-visits or virtual check-ins (Online Assessments Value Set),
#ED visits (ED Value Set), nonacute inpatient encounters (Nonacute Inpatient Value Set) or
#nonacute inpatient discharges (instructions below; the diagnosis must be on the discharge claim),
#on different dates of service, with a diagnosis of diabetes (Diabetes Value Set). Visit type need not be the same for the two encounters.
df_visit_dm_nonacute_inpt_stay = df_visit_dm_inpt_stay[(df_visit_dm_inpt_stay['UBREV'].isin(nonacute_inpatient_stay_code_list) |
                                                        df_visit_dm_inpt_stay['UBTOB'].isin(nonacute_inpatient_stay_code_list) |
                                                        df_visit_dm_inpt_stay['CPT'].isin(nonacute_inpatient_stay_code_list))]
df_visit_dm_nonacute_inpt_stay_with_dc_date = df_visit_dm_nonacute_inpt_stay.dropna(subset=['Discharge Date'])
df_visit_dm_nonacute_inpt = df_visit_dm[df_visit_dm['CPT'].isin(nonacute_inpatient_code_list)]
df_visit_dm_nonacute_no_tele = df_visit_dm_nonacute_inpt[~((df_visit_dm_nonacute_inpt['CPT Mod 1'].isin(telehealth_modifier_code_list)) | (df_visit_dm_nonacute_inpt['CPT Mod 2'].isin(telehealth_modifier_code_list)) | (df_visit_dm_nonacute_inpt['CMS Place of Service'].isin(telehealth_modifier_code_list)))]
df_visit_dm_nonacute_no_tele = df_visit_dm_nonacute_no_tele[~((df_visit_dm_nonacute_no_tele['CPT Mod 1'].isin(telehealth_pos_code_list)) | (df_visit_dm_nonacute_no_tele['CPT Mod 2'].isin(telehealth_pos_code_list)) | (df_visit_dm_nonacute_no_tele['CMS Place of Service'].isin(telehealth_pos_code_list)))]
df_visit_dm_other_visits = df_visit_dm[df_visit_dm['CPT'].isin(outpatient_code_list) | df_visit_dm['HCPCS'].isin(outpatient_code_list) | df_visit_dm['UBREV'].isin(outpatient_code_list) |
                                       df_visit_dm['CPT'].isin(observation_code_list) |
                                       df_visit_dm['CPT'].isin(telephone_visits_code_list) |
                                       df_visit_dm['CPT'].isin(online_assessments_code_list) | df_visit_dm['HCPCS'].isin(online_assessments_code_list) |
                                       df_visit_dm['CPT'].isin(ed_value_set_code_list) | df_visit_dm['UBREV'].isin(ed_value_set_code_list)]
df_visit_dm_all_nonacute_visits = pd.concat([df_visit_dm_nonacute_inpt_stay_with_dc_date, df_visit_dm_nonacute_no_tele, df_visit_dm_other_visits])

member_id_counts = df_visit_dm_all_nonacute_visits.groupby('Member ID')['DOS'].nunique()
duplicate_member_ids = member_id_counts[member_id_counts >= 2].index.tolist()

encounter_event_met = set(visit_dm_no_tele_list + dm_acute_inpt_stay_with_dc_date_list + duplicate_member_ids)


#Supplemental data may help determine:
#Numerators that are labeled as numerators in the specification. Num
#Optional exclusions. Excl
#Members in hospice and members who have died.
#Eligible-population required exclusions that are labeled as Required Exclusions in the specification. RexclD


column_widths = [16,3,8,11,1,7,1,10,10]

column_data = [[] for _ in range(len(column_widths))]

with open('pharm.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_pharm = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_pharm = df_pharm.rename(columns={'Column_1': 'Member ID'})
df_pharm['Member ID']=df_pharm['Member ID'].astype(int)
df_pharm = df_pharm.rename(columns={'Column_2': 'Days Supply'})
#df_pharm['Days Supply']=df_pharm['Member ID'].astype(int)
df_pharm = df_pharm.rename(columns={'Column_3': 'Rx Fill Date'})
df_pharm['Rx Fill Date'] = pd.to_datetime(df_pharm['Rx Fill Date'])
df_pharm['Refill Due Date'] = (df_pharm['Rx Fill Date'] + pd.to_timedelta(df_pharm['Days Supply'], errors='coerce')).dt.date
df_pharm = df_pharm.rename(columns={'Column_4': 'NDC'})
df_pharm = df_pharm.rename(columns={'Column_5': 'Claim Status'})
df_pharm = df_pharm.rename(columns={'Column_6': 'Quantity Dispensed'})
df_pharm['Quantity Dispensed'] = df_pharm['Quantity Dispensed'].astype(int)
df_pharm = df_pharm.rename(columns={'Column_7': 'Supp Data'})
df_pharm = df_pharm.rename(columns={'Column_8': 'Provider NPI'})
df_pharm = df_pharm.rename(columns={'Column_9': 'Pharmacy NPI'})

df_pharm_event = df_pharm[(df_pharm['NDC'].isin(dm_meds_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2021-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                  (df_pharm['Supp Data'] == 'N')
                 ]

pharm_event_met = df_pharm_event['Member ID'].unique().tolist()

all_event_met = set(list(encounter_event_met) + list(pharm_event_met))


column_widths = [5,8,6,12,7,1,1,8,4,5,1,1,1,1,1,1,1,1,1,1,1,2,1,7,7,2,2,2,8,8,9,9,9,9,8,1,10,8,1,4,7,1,1,3,1,2,1,1,1,3,1,1,
                 8,8,8,8,8,8,8,8,8,8,10,10,11,7,1,7,1,7,8,8,10,10,10,11,2,10,10,7,7,10,10,2,8,2,1,9,9,9,10]

column_data = [[] for _ in range(len(column_widths))]

with open('mmdf1.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf1 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf1 = df_mmdf1.rename(columns={'Column_2': 'Run Date'})
df_mmdf1['Run Date'] = pd.to_datetime(df_mmdf1['Run Date'])
df_mmdf1 = df_mmdf1.rename(columns={'Column_3': 'Payment Date'})
df_mmdf1 = df_mmdf1.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf1['Beneficiary ID'] = df_mmdf1['Beneficiary ID'].astype(int)
df_mmdf1 = df_mmdf1.rename(columns={'Column_14': 'Hospice'})
df_mmdf1 = df_mmdf1.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf1 = df_mmdf1.rename(columns={'Column_48': 'OREC'})

columns_to_drop = [col for col in df_mmdf1.columns if col.startswith('Column_')]
df_mmdf1.drop(columns=columns_to_drop, inplace=True)

with open('mmdf2.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf2 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf2 = df_mmdf2.rename(columns={'Column_2': 'Run Date'})
df_mmdf2['Run Date'] = pd.to_datetime(df_mmdf2['Run Date'])
df_mmdf2 = df_mmdf2.rename(columns={'Column_3': 'Payment Date'})
df_mmdf2 = df_mmdf2.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf2['Beneficiary ID'] = df_mmdf2['Beneficiary ID'].astype(int)
df_mmdf2 = df_mmdf2.rename(columns={'Column_14': 'Hospice'})
df_mmdf2 = df_mmdf2.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf2 = df_mmdf2.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf2.columns if col.startswith('Column_')]
df_mmdf2.drop(columns=columns_to_drop, inplace=True)

with open('mmdf3.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf3 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf3 = df_mmdf3.rename(columns={'Column_2': 'Run Date'})
df_mmdf3['Run Date'] = pd.to_datetime(df_mmdf3['Run Date'])
df_mmdf3 = df_mmdf3.rename(columns={'Column_3': 'Payment Date'})
df_mmdf3 = df_mmdf3.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf3['Beneficiary ID'] = df_mmdf3['Beneficiary ID'].astype(int)
df_mmdf3 = df_mmdf3.rename(columns={'Column_14': 'Hospice'})
df_mmdf3 = df_mmdf3.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf3 = df_mmdf3.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf3.columns if col.startswith('Column_')]
df_mmdf3.drop(columns=columns_to_drop, inplace=True)

with open('mmdf4.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf4 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf4 = df_mmdf4.rename(columns={'Column_2': 'Run Date'})
df_mmdf4['Run Date'] = pd.to_datetime(df_mmdf4['Run Date'])
df_mmdf4 = df_mmdf4.rename(columns={'Column_3': 'Payment Date'})
df_mmdf4 = df_mmdf4.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf4['Beneficiary ID'] = df_mmdf4['Beneficiary ID'].astype(int)
df_mmdf4 = df_mmdf4.rename(columns={'Column_14': 'Hospice'})
df_mmdf4 = df_mmdf4.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf4 = df_mmdf4.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf4.columns if col.startswith('Column_')]
df_mmdf4.drop(columns=columns_to_drop, inplace=True)

with open('mmdf5.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf5 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf5 = df_mmdf5.rename(columns={'Column_2': 'Run Date'})
df_mmdf5['Run Date'] = pd.to_datetime(df_mmdf5['Run Date'])
df_mmdf5 = df_mmdf5.rename(columns={'Column_3': 'Payment Date'})
df_mmdf5 = df_mmdf5.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf5['Beneficiary ID'] = df_mmdf5['Beneficiary ID'].astype(int)
df_mmdf5 = df_mmdf5.rename(columns={'Column_14': 'Hospice'})
df_mmdf5 = df_mmdf5.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf5 = df_mmdf5.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf5.columns if col.startswith('Column_')]
df_mmdf5.drop(columns=columns_to_drop, inplace=True)

with open('mmdf6.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf6 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf6 = df_mmdf6.rename(columns={'Column_2': 'Run Date'})
df_mmdf6['Run Date'] = pd.to_datetime(df_mmdf6['Run Date'])
df_mmdf6 = df_mmdf6.rename(columns={'Column_3': 'Payment Date'})
df_mmdf6 = df_mmdf6.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf6['Beneficiary ID'] = df_mmdf6['Beneficiary ID'].astype(int)
df_mmdf6 = df_mmdf6.rename(columns={'Column_14': 'Hospice'})
df_mmdf6 = df_mmdf6.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf6 = df_mmdf6.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf6.columns if col.startswith('Column_')]
df_mmdf6.drop(columns=columns_to_drop, inplace=True)

with open('mmdf7.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf7 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf7 = df_mmdf7.rename(columns={'Column_2': 'Run Date'})
df_mmdf7['Run Date'] = pd.to_datetime(df_mmdf7['Run Date'])
df_mmdf7 = df_mmdf7.rename(columns={'Column_3': 'Payment Date'})
df_mmdf7 = df_mmdf7.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf7['Beneficiary ID'] = df_mmdf7['Beneficiary ID'].astype(int)
df_mmdf7 = df_mmdf7.rename(columns={'Column_14': 'Hospice'})
df_mmdf7 = df_mmdf7.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf7 = df_mmdf7.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf7.columns if col.startswith('Column_')]
df_mmdf7.drop(columns=columns_to_drop, inplace=True)

with open('mmdf8.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf8 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf8 = df_mmdf8.rename(columns={'Column_2': 'Run Date'})
df_mmdf8['Run Date'] = pd.to_datetime(df_mmdf8['Run Date'])
df_mmdf8 = df_mmdf8.rename(columns={'Column_3': 'Payment Date'})
df_mmdf8 = df_mmdf8.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf8['Beneficiary ID'] = df_mmdf8['Beneficiary ID'].astype(int)
df_mmdf8 = df_mmdf8.rename(columns={'Column_14': 'Hospice'})
df_mmdf8 = df_mmdf8.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf8 = df_mmdf8.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf8.columns if col.startswith('Column_')]
df_mmdf8.drop(columns=columns_to_drop, inplace=True)

with open('mmdf9.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf9 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf9 = df_mmdf9.rename(columns={'Column_2': 'Run Date'})
df_mmdf9['Run Date'] = pd.to_datetime(df_mmdf9['Run Date'])
df_mmdf9 = df_mmdf9.rename(columns={'Column_3': 'Payment Date'})
df_mmdf9 = df_mmdf9.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf9['Beneficiary ID'] = df_mmdf9['Beneficiary ID'].astype(int)
df_mmdf9 = df_mmdf9.rename(columns={'Column_14': 'Hospice'})
df_mmdf9 = df_mmdf9.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf9 = df_mmdf9.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf9.columns if col.startswith('Column_')]
df_mmdf9.drop(columns=columns_to_drop, inplace=True)

with open('mmdf10.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf10 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf10 = df_mmdf10.rename(columns={'Column_2': 'Run Date'})
df_mmdf10['Run Date'] = pd.to_datetime(df_mmdf10['Run Date'])
df_mmdf10 = df_mmdf10.rename(columns={'Column_3': 'Payment Date'})
df_mmdf10 = df_mmdf10.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf10['Beneficiary ID'] = df_mmdf10['Beneficiary ID'].astype(int)
df_mmdf10 = df_mmdf10.rename(columns={'Column_14': 'Hospice'})
df_mmdf10 = df_mmdf10.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf10 = df_mmdf10.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf10.columns if col.startswith('Column_')]
df_mmdf10.drop(columns=columns_to_drop, inplace=True)

with open('mmdf11.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf11 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf11 = df_mmdf11.rename(columns={'Column_2': 'Run Date'})
df_mmdf11['Run Date'] = pd.to_datetime(df_mmdf11['Run Date'])
df_mmdf11 = df_mmdf11.rename(columns={'Column_3': 'Payment Date'})
df_mmdf11 = df_mmdf11.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf11['Beneficiary ID'] = df_mmdf11['Beneficiary ID'].astype(int)
df_mmdf11 = df_mmdf11.rename(columns={'Column_14': 'Hospice'})
df_mmdf11 = df_mmdf11.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf11 = df_mmdf11.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf11.columns if col.startswith('Column_')]
df_mmdf11.drop(columns=columns_to_drop, inplace=True)

with open('mmdf12.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf12 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf12 = df_mmdf12.rename(columns={'Column_2': 'Run Date'})
df_mmdf12['Run Date'] = pd.to_datetime(df_mmdf12['Run Date'])
df_mmdf12 = df_mmdf12.rename(columns={'Column_3': 'Payment Date'})
df_mmdf12 = df_mmdf12.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf12['Beneficiary ID'] = df_mmdf12['Beneficiary ID'].astype(int)
df_mmdf12 = df_mmdf12.rename(columns={'Column_14': 'Hospice'})
df_mmdf12 = df_mmdf12.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf12 = df_mmdf12.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf12.columns if col.startswith('Column_')]
df_mmdf12.drop(columns=columns_to_drop, inplace=True)

with open('mmdf13.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_mmdf13 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_mmdf13 = df_mmdf13.rename(columns={'Column_2': 'Run Date'})
df_mmdf13['Run Date'] = pd.to_datetime(df_mmdf13['Run Date'])
df_mmdf13 = df_mmdf13.rename(columns={'Column_3': 'Payment Date'})
df_mmdf13 = df_mmdf13.rename(columns={'Column_4': 'Beneficiary ID'})
df_mmdf13['Beneficiary ID'] = df_mmdf13['Beneficiary ID'].astype(int)
df_mmdf13 = df_mmdf13.rename(columns={'Column_14': 'Hospice'})
df_mmdf13 = df_mmdf13.rename(columns={'Column_20': 'LTI Flag'})
df_mmdf13 = df_mmdf13.rename(columns={'Column_48': 'OREC'})
columns_to_drop = [col for col in df_mmdf13.columns if col.startswith('Column_')]
df_mmdf13.drop(columns=columns_to_drop, inplace=True)

df_mmdf_all = pd.concat([df_mmdf1, df_mmdf2, df_mmdf3, df_mmdf4, df_mmdf5, df_mmdf6, df_mmdf7, df_mmdf8, df_mmdf9, df_mmdf10, df_mmdf11, df_mmdf12, df_mmdf13])


column_widths = [16,8,20,1,8,20]
column_data = [[] for _ in range(len(column_widths))]
with open('diag.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_diag = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_diag = df_diag.rename(columns={'Column_1': 'Member ID'})
df_diag = df_diag.rename(columns={'Column_2': 'Dx Start Date'})
df_diag = df_diag.rename(columns={'Column_3': 'Dx Code'})
df_diag = df_diag.rename(columns={'Column_4': 'Dx Flag'})
df_diag = df_diag.rename(columns={'Column_5': 'Dx End Date'})
df_diag = df_diag.rename(columns={'Column_6': 'Attribute'})
df_diag['Member ID']=df_diag['Member ID'].astype(int)
df_diag['Dx Start Date'] = pd.to_datetime(df_diag['Dx Start Date'])

df_diag_2021 = df_diag[df_diag['Dx Start Date'].dt.year==2021]
df_diag_2022 = df_diag[df_diag['Dx Start Date'].dt.year==2022]
df_diag_2021_2022 = pd.concat([df_diag_2021, df_diag_2022])


column_widths = [10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

column_data = [[] for _ in range(len(column_widths))]

with open('provider.txt', 'r') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df6 = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df6 = df6.rename(columns={'Column_1': 'Field'})
df6 = df6.rename(columns={'Column_2': 'PCP'})
df6 = df6.rename(columns={'Column_10': 'PA'})
df6 = df6.rename(columns={'Column_11': 'Prescribing Privileges'})
df6 = df6.rename(columns={'Column_13': 'Hospital'})
df6 = df6.rename(columns={'Column_16': 'RN'})


column_widths = [16,8,20,1,20,10,8,1,1,1]
column_data = [[] for _ in range(len(column_widths))]
with open('obs.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_obs = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_obs = df_obs.rename(columns={'Column_1': 'Member ID'})
df_obs = df_obs.rename(columns={'Column_2': 'Obs DOS'})
df_obs['Obs DOS'] = pd.to_datetime(df_obs['Obs DOS'])
df_obs = df_obs.rename(columns={'Column_3': 'Test'})
df_obs = df_obs.rename(columns={'Column_4': 'Test Code Flag'})
df_obs = df_obs.rename(columns={'Column_5': 'Value'})
df_obs = df_obs.rename(columns={'Column_6': 'Units'})
df_obs = df_obs.rename(columns={'Column_7': 'End DOS'})
df_obs = df_obs.rename(columns={'Column_8': 'Status'})
df_obs = df_obs.rename(columns={'Column_9': 'Result Value Flag'})
df_obs = df_obs.rename(columns={'Column_10': 'Type (VS or Lab)'})
df_obs['Member ID']=df_obs['Member ID'].astype(int)

df_obs_2021 = df_obs[df_obs['Obs DOS'].dt.year==2021]
df_obs_2022 = df_obs[df_obs['Obs DOS'].dt.year==2022]
df_obs_2021_2022 = pd.concat([df_obs_2021, df_obs_2022])


column_widths = [16,8,8,11,1,3,8,8,1,4,3]

column_data = [[] for _ in range(len(column_widths))]

with open('pharm-c.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_pharm_c = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_pharm_c = df_pharm_c.rename(columns={'Column_1': 'Member ID'})
df_pharm_c['Member ID']=df_pharm_c['Member ID'].astype(int)


column_widths = [16,8,20,1,8,3]

column_data = [[] for _ in range(len(column_widths))]

with open('proc.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_proc = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_proc = df_proc.rename(columns={'Column_1': 'Member ID'})
df_proc['Member ID']=df_proc['Member ID'].astype(int)
df_proc = df_proc.rename(columns={'Column_2': 'Service Date'})
df_proc['Service Date'] = pd.to_datetime(df_proc['Service Date'])
df_proc = df_proc.rename(columns={'Column_3': 'Procedure Code'})
df_proc = df_proc.rename(columns={'Column_5': 'End Date'})
df_proc = df_proc.rename(columns={'Column_6': 'Service Status'})
df_proc_performed = df_proc[df_proc['Service Status'] == 'EVN']

df_proc_2021 = df_proc_performed[df_proc_performed['Service Date'].dt.year==2021]
df_proc_2022 = df_proc_performed[df_proc_performed['Service Date'].dt.year==2022]
df_proc_2021_2022 = pd.concat([df_proc_2021, df_proc_2022])


column_widths = [16,8,20,1,8,1,10,20,1]

column_data = [[] for _ in range(len(column_widths))]

with open('visit-e.txt') as file:
    for line in file:
        start = 0
        for width_index, width in enumerate(column_widths):
            column_data[width_index].append(line[start:start+width].strip())
            start += width

df_visit_e = pd.DataFrame({f'Column_{i+1}': data for i, data in enumerate(column_data)})
df_visit_e = df_visit_e.rename(columns={'Column_1': 'Member ID'})
df_visit_e = df_visit_e.rename(columns={'Column_2': 'Service Date'})
df_visit_e = df_visit_e.rename(columns={'Column_3': 'Visit Code'})
df_visit_e = df_visit_e.rename(columns={'Column_4': 'Code Flag'})
df_visit_e = df_visit_e.rename(columns={'Column_8': 'Diagnosis Code'})
df_visit_e['Member ID']=df_visit_e['Member ID'].astype(int)
df_visit_e['Service Date']= pd.to_datetime(df_visit_e['Service Date'])

df_visit_e_2022 = df_visit_e[(df_visit_e['Service Date'].dt.year == 2022)]


#Members with CVD: Event in year prior
df_rexcl_mi = df_visit_2021[(df_visit_2021['UBREV'].isin(inpatient_stay_code_list) | df_visit_2021['UBTOB'].isin(inpatient_stay_code_list))]
df_rexcl_mi = df_rexcl_mi[df_rexcl_mi[columns_to_check].apply(lambda row: row.isin(mi_code_list) | row.isin(old_mi_code_list)).any(axis=1)]
df_rexcl_mi = df_rexcl_mi.dropna(subset=['Discharge Date'])
rexcl_mi_list = df_rexcl_mi['Member ID'].unique().tolist()

df_rexcl_cabg = df_visit_2021[df_visit_2021[columns_to_check].apply(lambda row: row.isin(cabg_code_list)).any(axis=1)]
rexcl_cabg_list = df_rexcl_cabg['Member ID'].unique().tolist()

df_rexcl_pci = df_visit_2021[df_visit_2021[columns_to_check].apply(lambda row: row.isin(pci_code_list)).any(axis=1)]
rexcl_pci_list = df_rexcl_pci['Member ID'].unique().tolist()

df_rexcl_other_revasc = df_visit_2021[df_visit_2021[columns_to_check].apply(lambda row: row.isin(other_revasc_code_list)).any(axis=1)]
rexcl_other_revasc_list = df_rexcl_other_revasc['Member ID'].unique().tolist()

#Members with CVD: Diagnosis during both MY and year prior to MY (NEED TO FIX THIS)

df_op_ivd_2021 = df_visit_2021[(df_visit_2021['CPT'].isin(outpatient_code_list)|
                           df_visit_2021['HCPCS'].isin(outpatient_code_list)|
                           df_visit_2021['UBREV'].isin(outpatient_code_list))]
df_op_ivd_2021 = df_op_ivd_2021[df_op_ivd_2021[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
df_op_ivd_2022 = df_visit_2022[(df_visit_2022['CPT'].isin(outpatient_code_list)|
                           df_visit_2022['HCPCS'].isin(outpatient_code_list)|
                           df_visit_2022['UBREV'].isin(outpatient_code_list))]
df_op_ivd_2022 = df_op_ivd_2022[df_op_ivd_2022[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
op_ivd_list_2021 = df_op_ivd_2021['Member ID'].unique().tolist()
op_ivd_list_2022 = df_op_ivd_2022['Member ID'].unique().tolist()
#op_ivd_list = [value for value in op_ivd_list_2021 if value in op_ivd_list_2022]

df_phone_ivd_2021 = df_visit_2021[(df_visit_2021['CPT'].isin(telephone_visits_code_list))]
df_phone_ivd_2021 = df_phone_ivd_2021[df_phone_ivd_2021[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
phone_ivd_list_2021 = df_phone_ivd_2021['Member ID'].unique().tolist()
df_phone_ivd_2022 = df_visit_2022[(df_visit_2022['CPT'].isin(telephone_visits_code_list))]
df_phone_ivd_2022 = df_phone_ivd_2022[df_phone_ivd_2022[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
phone_ivd_list_2022 = df_phone_ivd_2022['Member ID'].unique().tolist()

df_evisit_ivd_2021 = df_visit_2021[(df_visit_2021['CPT'].isin(online_assessments_code_list))]
df_evisit_ivd_2021 = df_evisit_ivd_2021[df_evisit_ivd_2021[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
evisit_ivd_list_2021 = df_evisit_ivd_2021['Member ID'].unique().tolist()
df_evisit_ivd_2022 = df_visit_2022[(df_visit_2022['CPT'].isin(online_assessments_code_list))]
df_evisit_ivd_2022 = df_evisit_ivd_2022[df_evisit_ivd_2022[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
evisit_ivd_list_2022 = df_evisit_ivd_2022['Member ID'].unique().tolist()

df_acute_inpt_2021 = df_visit_2021[df_visit_2021['CPT'].isin(acute_inpatient_code_list)]
df_acute_inpt_nontele_2021 = df_acute_inpt_2021[~((df_acute_inpt_2021['CPT Mod 1'].isin(telehealth_modifier_code_list)) | (df_acute_inpt_2021['CPT Mod 2'].isin(telehealth_modifier_code_list)) | (df_acute_inpt_2021['CMS Place of Service'].isin(telehealth_modifier_code_list)))]
df_acute_inpt_nontele_2021 = df_acute_inpt_nontele_2021[~((df_acute_inpt_nontele_2021['CPT Mod 1'].isin(telehealth_pos_code_list)) | (df_acute_inpt_nontele_2021['CPT Mod 2'].isin(telehealth_pos_code_list)) | (df_acute_inpt_nontele_2021['CMS Place of Service'].isin(telehealth_pos_code_list)))]
df_acute_inpt_nontele_ivd_2021 = df_acute_inpt_nontele_2021[df_acute_inpt_nontele_2021[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
acute_inpt_nontele_ivd_list_2021 = df_acute_inpt_nontele_ivd_2021['Member ID'].unique().tolist()
df_acute_inpt_2022 = df_visit_2022[df_visit_2022['CPT'].isin(acute_inpatient_code_list)]
df_acute_inpt_nontele_2022 = df_acute_inpt_2022[~((df_acute_inpt_2022['CPT Mod 1'].isin(telehealth_modifier_code_list)) | (df_acute_inpt_2022['CPT Mod 2'].isin(telehealth_modifier_code_list)) | (df_acute_inpt_2022['CMS Place of Service'].isin(telehealth_modifier_code_list)))]
df_acute_inpt_nontele_2022 = df_acute_inpt_nontele_2022[~((df_acute_inpt_nontele_2022['CPT Mod 1'].isin(telehealth_pos_code_list)) | (df_acute_inpt_nontele_2022['CPT Mod 2'].isin(telehealth_pos_code_list)) | (df_acute_inpt_nontele_2022['CMS Place of Service'].isin(telehealth_pos_code_list)))]
df_acute_inpt_nontele_ivd_2022 = df_acute_inpt_nontele_2022[df_acute_inpt_nontele_2022[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
acute_inpt_nontele_ivd_list_2022 = df_acute_inpt_nontele_ivd_2022['Member ID'].unique().tolist()

df_acute_inpt_stays_2021 = df_visit_2021[df_visit_2021['UBREV'].isin(inpatient_stay_code_list)]
df_acute_inpt_stays_2021 = df_acute_inpt_stays_2021[~(df_acute_inpt_stays_2021['UBREV'].isin(nonacute_inpatient_stay_code_list))]
df_acute_inpt_stays_dc_2021 = df_acute_inpt_stays_2021.dropna(subset=['Discharge Date'])
df_acute_inpt_stays_dc_ivd_2021 = df_acute_inpt_stays_dc_2021[df_acute_inpt_stays_dc_2021[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
acute_inpt_stays_ivd_list_2021 = df_acute_inpt_stays_dc_ivd_2021['Member ID'].unique().tolist()
df_acute_inpt_stays_2022 = df_visit_2022[df_visit_2022['UBREV'].isin(inpatient_stay_code_list)]
df_acute_inpt_stays_2022 = df_acute_inpt_stays_2022[~(df_acute_inpt_stays_2022['UBREV'].isin(nonacute_inpatient_stay_code_list))]
df_acute_inpt_stays_dc_2022 = df_acute_inpt_stays_2022.dropna(subset=['Discharge Date'])
df_acute_inpt_stays_dc_ivd_2022 = df_acute_inpt_stays_dc_2022[df_acute_inpt_stays_dc_2022[columns_to_check].apply(lambda row: row.isin(ivd_dx_code_list)).any(axis=1)]
acute_inpt_stays_ivd_list_2022 = df_acute_inpt_stays_dc_ivd_2022['Member ID'].unique().tolist()

ivd_2021_list = op_ivd_list_2021 + phone_ivd_list_2021 + evisit_ivd_list_2021 + acute_inpt_nontele_ivd_list_2021 + acute_inpt_stays_ivd_list_2021
ivd_2022_list = op_ivd_list_2022 + phone_ivd_list_2022 + evisit_ivd_list_2022 + acute_inpt_nontele_ivd_list_2022 + acute_inpt_stays_ivd_list_2022
ivd_complete_list = [value for value in ivd_2021_list if value in ivd_2022_list]

#Pregnancy in MY or year prior
df_pregnancy = df_visit_2021_2022[df_visit_2021_2022[columns_to_check].apply(lambda row: row.isin(pregnancy_code_list)).any(axis=1)]
df_pregnancy_females = df_pregnancy[df_pregnancy['Member ID'].isin(female_members_list)]
pregnancy_females_list = df_pregnancy_females['Member ID'].unique().tolist()

#IVF in MY or year prior
df_ivf_visit = df_visit_2021_2022[(df_visit_2021_2022[columns_to_check].apply(lambda row: row.isin(ivf_code_list)).any(axis=1) | df_visit_2021_2022['HCPCS'].isin(ivf_code_list)) ]
df_ivf_proc = df_proc_2021_2022[df_proc_2021_2022['Procedure Code'].isin(ivf_code_list)]
ivf_list = df_ivf_visit['Member ID'].unique().tolist() + df_ivf_proc['Member ID'].unique().tolist()

#Estrogen Agonists Medications in MY or year prior
df_estrogen_agonist_members = df_pharm[(df_pharm['NDC'].isin(estrogen_agonist_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2021-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31')]
estrogen_agonist_member_list = df_estrogen_agonist_members['Member ID'].unique().tolist()

#ESRD or Dialysis in MY or year prior
df_esrd_visit = df_visit_2021_2022[df_visit_2021_2022[columns_to_check].apply(lambda row: row.isin(esrd_code_list)).any(axis=1)]
df_esrd_diag = df_diag[(df_diag['Dx Code'].isin(esrd_code_list)) & ((df_diag['Dx Start Date'].dt.year == 2021) | (df_diag['Dx Start Date'].dt.year == 2022))]
esrd_list = df_esrd_visit['Member ID'].unique().tolist() + df_esrd_diag['Member ID'].unique().tolist()

df_dialysis_procedure_visit = df_visit_2021_2022[df_visit_2021_2022[columns_to_check].apply(lambda row: row.isin(dialysis_procedure_code_list)).any(axis=1)]
df_dialysis_procedure_diag = df_diag[(df_diag['Dx Code'].isin(dialysis_procedure_code_list)) & ((df_diag['Dx Start Date'].dt.year == 2021) | (df_diag['Dx Start Date'].dt.year == 2022))]
df_dialysis_procedure_proc = df_proc_performed[(df_proc_performed['Procedure Code'].isin(dialysis_procedure_code_list)) & ((df_proc_performed['Service Date'].dt.year == 2021) | (df_proc_performed['Service Date'].dt.year == 2022))]
dialysis_procedure_list = df_dialysis_procedure_visit['Member ID'].unique().tolist() + df_dialysis_procedure_diag['Member ID'].unique().tolist() + df_dialysis_procedure_proc['Member ID'].unique().tolist()

#Cirrhosis in MY or year prior
df_cirrhosis_visit = df_visit_2021_2022[df_visit_2021_2022[columns_to_check].apply(lambda row: row.isin(cirrhosis_code_list)).any(axis=1)]
df_cirrhosis_diag = df_diag[(df_diag['Dx Code'].isin(cirrhosis_code_list)) & ((df_diag['Dx Start Date'].dt.year == 2021) | (df_diag['Dx Start Date'].dt.year == 2022))]
cirrhosis_list = df_cirrhosis_visit['Member ID'].unique().tolist() + df_cirrhosis_diag['Member ID'].unique().tolist()

#Muscular Pain and Disease during MY
df_muscle_pain_visit = df_visit_2022[df_visit_2022[columns_to_check].apply(lambda row: row.isin(muscle_pain_code_list)).any(axis=1)]
df_muscle_pain_diag = df_diag[(df_diag['Dx Code'].isin(muscle_pain_code_list)) & ((df_diag['Dx Start Date'].dt.year == 2021))]
muscle_pain_list = df_muscle_pain_visit['Member ID'].unique().tolist() + df_muscle_pain_diag['Member ID'].unique().tolist()

#Hospice during MY (pg 30 in tech spec; HCPCS, SNOMED, and UBREV for Hospice Encounter; CPT, HCPCS, and SNOMED for Hospice Intervention)
df_visit_hospice_encounter = df_visit_2022[df_visit_2022['HCPCS'].isin(hospice_encounter_code_list) | df_visit_2022['UBREV'].isin(hospice_encounter_code_list)]
df_visit_hospice_intervention = df_visit_2022[df_visit_2022['HCPCS'].isin(hospice_intervention_code_list) | df_visit_2022['CPT'].isin(hospice_intervention_code_list)]
df_visit_e_hospice_encounter = df_visit_e_2022[df_visit_e_2022['Visit Code'].isin(hospice_encounter_code_list)]
df_visit_e_hospice_intervention = df_visit_e_2022[df_visit_e_2022['Visit Code'].isin(hospice_intervention_code_list)]
df_mmdf_hospice = df_mmdf_all[(df_mmdf_all['Hospice'] == 'Y') & (df_mmdf_all['Run Date'] >= '2022-01-01') & (df_mmdf_all['Run Date'] <= '2022-12-31')]
hospice_list = df_visit_hospice_encounter['Member ID'].unique().tolist() + df_visit_hospice_intervention['Member ID'].unique().tolist() + df_visit_e_hospice_encounter['Member ID'].unique().tolist() + df_visit_e_hospice_intervention['Member ID'].unique().tolist() + df_mmdf_hospice['Beneficiary ID'].unique().tolist()

#Palliative Care during MY (Palliative Care Assessment - SNOMED, Palliative Care Encounter - HCPCS, ICD10CM, SNOMED; PC Intervention - SNOMED)
#SNOMED most likely in obs.txt
df_obs_2022 = df_obs[(df_obs['Obs DOS'].dt.year == 2022)]
pc_assessment_list = df_obs_2022[df_obs_2022['Test'].isin(pall_care_assess_code_list)]['Member ID'].tolist()

def check_icd10(row):
    return any(value in row.values for value in pall_care_enc_code_list)

df_pc_enc_icd10 = df_visit_2022.apply(check_icd10, axis=1)
pc_enc_icd10_list = df_visit_2022[df_pc_enc_icd10]['Member ID'].tolist()
pc_enc_cpt = df_visit_2022[df_visit_2022['CPT'].isin(pall_care_assess_code_list)]['Member ID'].unique().tolist()
pc_enc_hcpcs = df_visit_2022[df_visit_2022['HCPCS'].isin(pall_care_assess_code_list)]['Member ID'].unique().tolist()
pc_intervention = df_obs_2022[df_obs_2022['Test'].isin(pall_care_int_code_list)]['Member ID'].unique().tolist()

rexcld_list = set(rexcl_mi_list + rexcl_cabg_list + rexcl_pci_list + rexcl_other_revasc_list + ivd_complete_list +
                  pregnancy_females_list + ivf_list + estrogen_agonist_member_list + esrd_list + dialysis_procedure_list +
                  cirrhosis_list + muscle_pain_list + hospice_list + pc_assessment_list +
                  pc_enc_icd10_list + pc_enc_cpt + pc_enc_hcpcs + pc_intervention)


#First, filter out df_member_gm for all members 66 or older as of 12/31 of measurement year
members_66_or_older = df_member_gm[(df_member_gm['Age'] >= 66)]['Member ID'].tolist()

# >=Medicare 66yo or older on 12/31/22 and in I-SNP or LTI
run_date_2022 = df_mmdf_all[df_mmdf_all['Run Date'].dt.year == 2022]
lti_members = run_date_2022[run_date_2022['LTI Flag'] == 'Y']['Beneficiary ID'].unique().tolist()
lti_members_set = set(lti_members)
sn2_members = df_member_2022[df_member_2022['Payer'] == 'SN2']['Member ID'].unique().tolist()
sn2_members_set = set(sn2_members)
members_66_or_older_set = set(members_66_or_older)
sn2_members_66_or_older = list(members_66_or_older_set.intersection(sn2_members_set))

lti_members_66_or_older = list(members_66_or_older_set.intersection(lti_members_set)) #need to use in final_df only if medicare plans

# >=66 yo on 12/31/22, and with frality and advanced illness
#Condition 1
#Frailty Device Value Set (HCPCS), Frailty Diagnosis (ICD10CM and SNOMED), Frailty Encounter (CPT, HCPCS), Frailty Symptom (ICD10, SNOMED)
df_frailty_1 = df_visit_2022_no_supp[((df_visit['HCPCS'].isin(frailty_device_code_list)) | (df_visit['HCPCS'].isin(frailty_enc_code_list)) | (df_visit['CPT'].isin(frailty_enc_code_list)))]
df_frailty_2 = df_visit_2022_no_supp[df_visit_2022_no_supp[columns_to_check].apply(lambda row: row.isin(frailty_diagnosis_code_list)).any(axis=1)]
df_frailty_3 = df_visit_2022_no_supp[df_visit_2022_no_supp[columns_to_check].apply(lambda row: row.isin(frailty_symptom_code_list)).any(axis=1)]
df_frailty = pd.concat([df_frailty_1, df_frailty_2, df_frailty_3])
frailty_list = df_frailty['Member ID'].unique().tolist()

#Condition 2
df_visit_2021_2022_inpt_stay = df_visit_2021_2022_no_supp[df_visit_2021_2022_no_supp['UBREV'].isin(inpatient_stay_code_list)]

# At Least two op, obs, ed, telephone, online assessments, nonacute inpt enc, or nonacute inpt discharges with adv illeness dx
df_adv_illness_op_visits = df_visit_2021_2022_no_supp[df_visit_2021_2022_no_supp['CPT'].isin(outpatient_code_list) |
                                                      df_visit_2021_2022_no_supp['CPT'].isin(observation_code_list) |
                                                      df_visit_2021_2022_no_supp['CPT'].isin(telephone_visits_code_list) |
                                                      df_visit_2021_2022_no_supp['CPT'].isin(online_assessments_code_list) |
                                                      df_visit_2021_2022_no_supp['CPT'].isin(ed_value_set_code_list)]
df_adv_illness_nonacute_inpt_stay = df_visit_2021_2022_inpt_stay[(df_visit_2021_2022_inpt_stay['CPT'].isin(nonacute_inpatient_stay_code_list) |
                                                                  df_visit_2021_2022_inpt_stay['UBTOB'].isin(nonacute_inpatient_stay_code_list) |
                                                                  df_visit_2021_2022_inpt_stay['UBREV'].isin(nonacute_inpatient_stay_code_list))]
df_adv_illness_nonacute_inpt_stay = df_adv_illness_nonacute_inpt_stay.dropna(subset=['Discharge Date'])
df_adv_illness_1 = pd.concat([df_adv_illness_op_visits, df_adv_illness_nonacute_inpt_stay])
df_adv_illness_1 = df_adv_illness_1[df_adv_illness_1[columns_to_check].apply(lambda row: row.isin(advanced_illness_code_list)).any(axis=1)]

member_id_counts = df_adv_illness_1.groupby('Member ID')['DOS'].nunique()
adv_illness_1_list = member_id_counts[member_id_counts >= 2].index.tolist()

#At Least one acute inpt enc with an advanced illness dx
df_adv_illness_2 = df_visit_2021_2022_no_supp[df_visit_2021_2022_no_supp['CPT'].isin(acute_inpatient_code_list)]
df_adv_illness_2 = df_adv_illness_2[df_adv_illness_2[columns_to_check].apply(lambda row: row.isin(advanced_illness_code_list)).any(axis=1)]
adv_illness_2_list = df_adv_illness_2['Member ID'].unique().tolist()

# At least one acute inpatient discharge with an advanced illness dx on dc claim
df_adv_illness_3 = df_visit_2021_2022_inpt_stay[~(df_visit_2021_2022_inpt_stay['UBREV'].isin(nonacute_inpatient_stay_code_list) |
                                                  df_visit_2021_2022_inpt_stay['CPT'].isin(nonacute_inpatient_stay_code_list) |
                                                  df_visit_2021_2022_inpt_stay['UBTOB'].isin(nonacute_inpatient_stay_code_list))]
df_adv_illness_3 = df_adv_illness_3.dropna(subset=['Discharge Date'])
df_adv_illness_3 = df_adv_illness_3[df_adv_illness_3[columns_to_check].apply(lambda row: row.isin(advanced_illness_code_list)).any(axis=1)]
adv_illness_3_list = df_adv_illness_3['Member ID'].unique().tolist()

# A dispensed dementia medication
df_dementia_medication_members = df_pharm[(df_pharm['NDC'].isin(dementia_meds_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2021-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31')]
dementia_medication_members_list = df_dementia_medication_members['Member ID'].unique().tolist()

adv_illness_total_list = set(adv_illness_1_list + adv_illness_2_list + adv_illness_3_list + dementia_medication_members_list)

frailty_and_adv_illness_list = [value for value in frailty_list if value in adv_illness_total_list]

#Final List for rexcl
rexcl_list = set(sn2_members_66_or_older + frailty_and_adv_illness_list)


#df_optional_excl = df_visit_2021_2022[~df_visit_2021_2022.apply(lambda row: any(code in dm_dx_code_list for code in row[1:]) and any(exclusion in diabetes_exclusions_code_list for exclusion in row[1:]), axis=1)]
df_optional_excl_visit = df_visit_2021_2022[
    (~df_visit_2021_2022[columns_to_check].isin(dm_dx_code_list).any(axis=1)) &
    (df_visit_2021_2022[columns_to_check].isin(diabetes_exclusions_code_list).any(axis=1))]
optional_excl_visit_list = df_optional_excl_visit['Member ID'].unique().tolist()

option_excl_diag = df_diag_2021_2022[(df_diag_2021_2022['Dx Code'].isin(diabetes_exclusions_code_list))]
option_excl_diag_list = option_excl_diag['Member ID'].unique().tolist()

optional_excl_met_list = list((set(optional_excl_visit_list) | set(option_excl_diag_list)) - set(all_event_met))


#SPDA
df_atorvastatin_high = df_pharm[(df_pharm['NDC'].isin(atorvastatin_high_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
atorvastatin_high_member_list = df_atorvastatin_high['Member ID'].unique().tolist()

df_amlodipine_atorvastatin_high = df_pharm[(df_pharm['NDC'].isin(amlodipine_atorvastatin_high_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
amlodipine_atorvastatin_high_member_list = df_amlodipine_atorvastatin_high['Member ID'].unique().tolist()

df_rosuvastatin_high = df_pharm[(df_pharm['NDC'].isin(rosuvastatin_high_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
rosuvastatin_high_member_list = df_rosuvastatin_high['Member ID'].unique().tolist()

df_simvastatin_high = df_pharm[(df_pharm['NDC'].isin(simvastatin_high_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
simvastatin_high_member_list = df_simvastatin_high['Member ID'].unique().tolist()

df_ezetimibe_simvastatin_high = df_pharm[(df_pharm['NDC'].isin(ezetimibe_simvastatin_high_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
ezetimibe_simvastatin_high_member_list = df_ezetimibe_simvastatin_high['Member ID'].unique().tolist()

df_atorvastatin_mod = df_pharm[(df_pharm['NDC'].isin(atorvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
atorvastatin_mod_member_list = df_atorvastatin_mod['Member ID'].unique().tolist()

df_amlodipine_atorvastatin_mod = df_pharm[(df_pharm['NDC'].isin(amlodipine_atorvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
amlodipine_atorvastatin_mod_member_list = df_amlodipine_atorvastatin_mod['Member ID'].unique().tolist()

df_rosuvastatin_mod = df_pharm[(df_pharm['NDC'].isin(rosuvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
rosuvastatin_mod_member_list = df_rosuvastatin_mod['Member ID'].unique().tolist()

df_simvastatin_mod = df_pharm[(df_pharm['NDC'].isin(simvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
simvastatin_mod_member_list = df_simvastatin_mod['Member ID'].unique().tolist()

df_ezetimibe_simvastatin_mod = df_pharm[(df_pharm['NDC'].isin(ezetimibe_simvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
ezetimibe_simvastatin_mod_member_list = df_ezetimibe_simvastatin_mod['Member ID'].unique().tolist()

df_pravastatin_mod = df_pharm[(df_pharm['NDC'].isin(pravastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
pravastatin_mod_member_list = df_pravastatin_mod['Member ID'].unique().tolist()

df_lovastatin_mod = df_pharm[(df_pharm['NDC'].isin(lovastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
lovastatin_mod_member_list = df_lovastatin_mod['Member ID'].unique().tolist()

df_fluvastatin_mod = df_pharm[(df_pharm['NDC'].isin(fluvastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
fluvastatin_mod_member_list = df_fluvastatin_mod['Member ID'].unique().tolist()

df_pitavastatin_mod = df_pharm[(df_pharm['NDC'].isin(pitavastatin_mod_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
pitavastatin_mod_member_list = df_pitavastatin_mod['Member ID'].unique().tolist()

df_simvastatin_low = df_pharm[(df_pharm['NDC'].isin(simvastatin_low_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
simvastatin_low_member_list = df_simvastatin_low['Member ID'].unique().tolist()

df_ezetimibe_simvastatin_low = df_pharm[(df_pharm['NDC'].isin(ezetimibe_simvastatin_low_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
ezetimibe_simvastatin_low_member_list = df_ezetimibe_simvastatin_low['Member ID'].unique().tolist()

df_pravastatin_low = df_pharm[(df_pharm['NDC'].isin(pravastatin_low_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
pravastatin_low_member_list = df_pravastatin_low['Member ID'].unique().tolist()

df_lovastatin_low = df_pharm[(df_pharm['NDC'].isin(lovastatin_low_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
lovastatin_low_member_list = df_lovastatin_low['Member ID'].unique().tolist()

df_fluvastatin_low = df_pharm[(df_pharm['NDC'].isin(fluvastatin_low_intensity_code_list)) &
                 (df_pharm['Rx Fill Date'] >= '2022-01-01') &
                 (df_pharm['Rx Fill Date'] <= '2022-12-31') &
                 (df_pharm['Claim Status'] == '1')]
fluvastatin_low_member_list = df_fluvastatin_low['Member ID'].unique().tolist()

spda_numerator = set(atorvastatin_high_member_list + amlodipine_atorvastatin_high_member_list + rosuvastatin_high_member_list + simvastatin_high_member_list +
                     ezetimibe_simvastatin_high_member_list + atorvastatin_mod_member_list + amlodipine_atorvastatin_mod_member_list + rosuvastatin_mod_member_list +
                     simvastatin_mod_member_list + ezetimibe_simvastatin_mod_member_list + pravastatin_mod_member_list + lovastatin_mod_member_list +
                     fluvastatin_mod_member_list + pitavastatin_mod_member_list + simvastatin_low_member_list + ezetimibe_simvastatin_low_member_list +
                     pravastatin_low_member_list + lovastatin_low_member_list + fluvastatin_low_member_list)

#SPDB
df_spdb_fills = pd.concat([df_atorvastatin_high, df_amlodipine_atorvastatin_high, df_rosuvastatin_high, df_simvastatin_high,
                           df_ezetimibe_simvastatin_high, df_atorvastatin_mod, df_amlodipine_atorvastatin_mod, df_rosuvastatin_mod,
                           df_simvastatin_mod, df_ezetimibe_simvastatin_mod, df_pravastatin_mod, df_lovastatin_mod, df_fluvastatin_mod,
                           df_pitavastatin_mod, df_simvastatin_low, df_ezetimibe_simvastatin_low, df_pravastatin_low, df_lovastatin_low,
                           df_fluvastatin_low])

spdb_claims_by_member_id = df_spdb_fills.groupby('Member ID')

total_expected_therapy = {}
total_days_supply_filled = {}

for member_id, claims in spdb_claims_by_member_id:
    first_fill_date = claims['Rx Fill Date'].min()
    expected_therapy_days = (pd.to_datetime('2022-12-31') - first_fill_date).days + 1
    total_expected_therapy[member_id] = expected_therapy_days

    total_supply = 0
    for _, claim in claims.iterrows():
        if pd.Timestamp(claim['Refill Due Date']) > pd.Timestamp('2022-12-31'):
            days_supply = (pd.Timestamp('2022-12-31') - pd.Timestamp(claim['Rx Fill Date'])).days
        else:
            days_supply = int(claim['Days Supply'])
        total_supply += days_supply
    total_days_supply_filled[member_id] = total_supply

spdb_totals_df = pd.DataFrame({
    'Member ID': list(total_expected_therapy.keys()),
    'Total Expected Therapy Days': list(total_expected_therapy.values()),
    'Total Days Supply Filled': list(total_days_supply_filled.values())
})

spdb_totals_df['PDC'] = spdb_totals_df['Total Days Supply Filled'] / spdb_totals_df['Total Expected Therapy Days'].round()

final_spdb_df = pd.merge(df_spdb_fills, spdb_totals_df, on='Member ID', how='left')

meet_spdb_pdc = spdb_totals_df[spdb_totals_df['PDC'] >= 0.8]['Member ID'].tolist()




final_df = pd.DataFrame()

#Generate a list of all Member IDs to include in final dataframe
member_ids_active_coverage = set(df_member_active_coverage['Member ID'])
member_ids_age_40_75 = set(df_member_gm_age_40_75['Member ID'])
common_member_ids = member_ids_active_coverage.intersection(member_ids_age_40_75)
common_member_ids_list = list(common_member_ids)

filtered_df_member_gm = df_member_gm[df_member_gm['Member ID'].isin(common_member_ids_list)]
final_df = pd.DataFrame(columns=['MemID', 'Age', 'Gender'])
final_df['MemID'] = filtered_df_member_gm['Member ID']
final_df['Age'] = filtered_df_member_gm['Age']
final_df['Gender'] = filtered_df_member_gm['Gender']

final_df = final_df.reindex(final_df.index.repeat(2)).reset_index(drop=True)

# Add a new column 'Meas' for Measure IDs right after the 'MemID' column
final_df.insert(1, 'Meas', ['SPDA', 'SPDB'] * (len(final_df) // 2))

final_df = pd.merge(final_df, payer_last_df, left_on='MemID', right_on='Member ID', how='left')
final_df.drop(columns=['Member ID'], inplace=True)
final_df['Payer'] = final_df['Payer'].replace(['SN1', 'SN2'], 'MCR')
final_df['Payer'] = final_df['Payer'].replace(['MD', 'MDE', 'MLI', 'MRB'], 'MCD')

mmp_rows = final_df[final_df['Payer'] == 'MMP']
new_rows = []

# Iterate over the MMP rows
for index, row in mmp_rows.iterrows():
    # Create new rows with 'MCD' and 'MCR' in the 'Payer' column
    new_row_1 = row.copy()
    new_row_1['Payer'] = 'MCD'
    new_row_2 = row.copy()
    new_row_2['Payer'] = 'MCR'
    # Append new rows to the list
    new_rows.extend([new_row_1, new_row_2])

new_rows_df = pd.DataFrame(new_rows)
final_df = pd.concat([final_df, new_rows_df], ignore_index=True)
final_df = final_df[final_df['Payer'] != 'MMP']
final_df.sort_values(by=['MemID', 'Meas'], inplace=True)
final_df.reset_index(drop=True, inplace=True)


# MemID, Meas, Payer, CE, Event, Epop, Excl, Num, RExcl, RExclD, Age, Gender

#Num
final_df['Num'] = 0
final_df.loc[(final_df['Meas'] == 'SPDA') & (final_df['MemID'].isin(spda_numerator)), 'Num'] = 1
final_df.loc[(final_df['Meas'] == 'SPDB') & (final_df['MemID'].isin(meet_spdb_pdc)), 'Num'] = 1

#CE
final_df['CE'] = final_df['MemID'].apply(lambda x: 1 if x in continuous_enrollment_met else 0)

#Event
final_df['Event'] = 0
final_df.loc[(final_df['MemID'].isin(all_event_met)) & (final_df['Meas'] == 'SPDA'), 'Event'] = 1
final_df.loc[(final_df['MemID'].isin(spda_numerator)) & (final_df['Meas'] == 'SPDB'), 'Event'] = 1

#RExclD
final_df['RExclD'] = final_df['MemID'].apply(lambda x: 1 if x in rexcld_list else 0)

#RExcl
medicare_plans = ['MCR', 'MCS', 'MP', 'MC', 'SN1']
#final_df['RExcl'] = final_df['MemID'].apply(lambda x: 1 if x in rexcl_list else 0)
#final_df['RExcl'] = final_df.apply(lambda row: 1 if row['MemID'] in lti_members_66_or_older and row['Payer'] in medicare_plans else 0, axis=1)
final_df['RExcl'] = 0  # Initialize 'RExcl' column with all 0s
final_df.loc[final_df['MemID'].isin(rexcl_list), 'RExcl'] = 1  # Update to 1 if MemID is in rexcl_list
final_df.loc[(final_df['MemID'].isin(lti_members_66_or_older)) & (final_df['Payer'].isin(medicare_plans)), 'RExcl'] = 1  # Update to 1 based on the condition

#Excl
final_df['Excl'] = final_df['MemID'].apply(lambda x: 1 if x in optional_excl_met_list else 0)

#Epop
final_df['Epop'] = 0
HEDIS_payers = ['PPO', 'POS', 'HMO', 'MCR', 'MP', 'MCS', 'MCD', 'CEP'] #SN1, SN2, SN3, MMP?
final_df.loc[(final_df['CE'] == 1) & (final_df['Event'] == 1) & (final_df['RExcl'] == 0) & (final_df['RExclD'] == 0) & (final_df['Payer'].isin(HEDIS_payers)), 'Epop'] = 1

final_df = final_df.reindex(columns=['MemID', 'Meas', 'Payer', 'CE', 'Event', 'Epop', 'Excl', 'Num', 'RExcl', 'RExclD', 'Age', 'Gender'])


final_df.to_csv('output.txt', sep=',', index=False)
import os
os.rename('output.txt', 'output.txt')
