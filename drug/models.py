from django.db import models
from django.conf import settings
from django.urls import include, path
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import connection

# Create your models here.
class Opioids(models.Model):
    drugname = models.CharField(db_column='DrugName', max_length=50, primary_key=True)  # Field name made lowercase.
    isopioid = models.IntegerField(db_column='IsOpioid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opioids'


class Overdoses(models.Model):
    field_state_field = models.CharField(db_column='_State_', max_length=50, primary_key=True)  # Field name made lowercase. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_population_field = models.CharField(db_column='_Population_', max_length=50)  # Field name made lowercase. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_deaths_field = models.CharField(db_column='_Deaths_', max_length=50)  # Field name made lowercase. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_abbrev_field = models.CharField(db_column='_Abbrev_', max_length=50)  # Field name made lowercase. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'overdoses'


class PrescriberInfo(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=50)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=50)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    credentials = models.CharField(db_column='Credentials', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specialty = models.CharField(db_column='Specialty', max_length=100)  # Field name made lowercase.
    opioid_prescriber = models.IntegerField(db_column='Opioid_Prescriber')  # Field name made lowercase.
    totalprescriptions = models.IntegerField(db_column='TotalPrescriptions')  # Field name made lowercase.
    abilify = models.IntegerField(db_column='ABILIFY')  # Field name made lowercase.
    acetaminophen_codeine = models.IntegerField(db_column='ACETAMINOPHEN_CODEINE')  # Field name made lowercase.
    acyclovir = models.IntegerField(db_column='ACYCLOVIR')  # Field name made lowercase.
    advair_diskus = models.IntegerField(db_column='ADVAIR_DISKUS')  # Field name made lowercase.
    aggrenox = models.IntegerField(db_column='AGGRENOX')  # Field name made lowercase.
    alendronate_sodium = models.IntegerField(db_column='ALENDRONATE_SODIUM')  # Field name made lowercase.
    allopurinol = models.IntegerField(db_column='ALLOPURINOL')  # Field name made lowercase.
    alprazolam = models.IntegerField(db_column='ALPRAZOLAM')  # Field name made lowercase.
    amiodarone_hcl = models.IntegerField(db_column='AMIODARONE_HCL')  # Field name made lowercase.
    amitriptyline_hcl = models.IntegerField(db_column='AMITRIPTYLINE_HCL')  # Field name made lowercase.
    amlodipine_besylate = models.IntegerField(db_column='AMLODIPINE_BESYLATE')  # Field name made lowercase.
    amlodipine_besylate_benazepril = models.IntegerField(db_column='AMLODIPINE_BESYLATE_BENAZEPRIL')  # Field name made lowercase.
    amoxicillin = models.IntegerField(db_column='AMOXICILLIN')  # Field name made lowercase.
    amox_tr_potassium_clavulanate = models.IntegerField(db_column='AMOX_TR_POTASSIUM_CLAVULANATE')  # Field name made lowercase.
    amphetamine_salt_combo = models.IntegerField(db_column='AMPHETAMINE_SALT_COMBO')  # Field name made lowercase.
    atenolol = models.IntegerField(db_column='ATENOLOL')  # Field name made lowercase.
    atorvastatin_calcium = models.IntegerField(db_column='ATORVASTATIN_CALCIUM')  # Field name made lowercase.
    avodart = models.IntegerField(db_column='AVODART')  # Field name made lowercase.
    azithromycin = models.IntegerField(db_column='AZITHROMYCIN')  # Field name made lowercase.
    baclofen = models.IntegerField(db_column='BACLOFEN')  # Field name made lowercase.
    bd_ultra_fine_pen_needle = models.IntegerField(db_column='BD_ULTRA_FINE_PEN_NEEDLE')  # Field name made lowercase.
    benazepril_hcl = models.IntegerField(db_column='BENAZEPRIL_HCL')  # Field name made lowercase.
    benicar = models.IntegerField(db_column='BENICAR')  # Field name made lowercase.
    benicar_hct = models.IntegerField(db_column='BENICAR_HCT')  # Field name made lowercase.
    benztropine_mesylate = models.IntegerField(db_column='BENZTROPINE_MESYLATE')  # Field name made lowercase.
    bisoprolol_hydrochlorothiazide = models.IntegerField(db_column='BISOPROLOL_HYDROCHLOROTHIAZIDE')  # Field name made lowercase.
    brimonidine_tartrate = models.IntegerField(db_column='BRIMONIDINE_TARTRATE')  # Field name made lowercase.
    bumetanide = models.IntegerField(db_column='BUMETANIDE')  # Field name made lowercase.
    bupropion_hcl_sr = models.IntegerField(db_column='BUPROPION_HCL_SR')  # Field name made lowercase.
    bupropion_xl = models.IntegerField(db_column='BUPROPION_XL')  # Field name made lowercase.
    buspirone_hcl = models.IntegerField(db_column='BUSPIRONE_HCL')  # Field name made lowercase.
    bystolic = models.IntegerField(db_column='BYSTOLIC')  # Field name made lowercase.
    carbamazepine = models.IntegerField(db_column='CARBAMAZEPINE')  # Field name made lowercase.
    carbidopa_levodopa = models.IntegerField(db_column='CARBIDOPA_LEVODOPA')  # Field name made lowercase.
    carisoprodol = models.IntegerField(db_column='CARISOPRODOL')  # Field name made lowercase.
    cartia_xt = models.IntegerField(db_column='CARTIA_XT')  # Field name made lowercase.
    carvedilol = models.IntegerField(db_column='CARVEDILOL')  # Field name made lowercase.
    cefuroxime = models.IntegerField(db_column='CEFUROXIME')  # Field name made lowercase.
    celebrex = models.IntegerField(db_column='CELEBREX')  # Field name made lowercase.
    cephalexin = models.IntegerField(db_column='CEPHALEXIN')  # Field name made lowercase.
    chlorhexidine_gluconate = models.IntegerField(db_column='CHLORHEXIDINE_GLUCONATE')  # Field name made lowercase.
    chlorthalidone = models.IntegerField(db_column='CHLORTHALIDONE')  # Field name made lowercase.
    cilostazol = models.IntegerField(db_column='CILOSTAZOL')  # Field name made lowercase.
    ciprofloxacin_hcl = models.IntegerField(db_column='CIPROFLOXACIN_HCL')  # Field name made lowercase.
    citalopram_hbr = models.IntegerField(db_column='CITALOPRAM_HBR')  # Field name made lowercase.
    clindamycin_hcl = models.IntegerField(db_column='CLINDAMYCIN_HCL')  # Field name made lowercase.
    clobetasol_propionate = models.IntegerField(db_column='CLOBETASOL_PROPIONATE')  # Field name made lowercase.
    clonazepam = models.IntegerField(db_column='CLONAZEPAM')  # Field name made lowercase.
    clonidine_hcl = models.IntegerField(db_column='CLONIDINE_HCL')  # Field name made lowercase.
    clopidogrel = models.IntegerField(db_column='CLOPIDOGREL')  # Field name made lowercase.
    clotrimazole_betamethasone = models.IntegerField(db_column='CLOTRIMAZOLE_BETAMETHASONE')  # Field name made lowercase.
    colcrys = models.IntegerField(db_column='COLCRYS')  # Field name made lowercase.
    combivent_respimat = models.IntegerField(db_column='COMBIVENT_RESPIMAT')  # Field name made lowercase.
    crestor = models.IntegerField(db_column='CRESTOR')  # Field name made lowercase.
    cyclobenzaprine_hcl = models.IntegerField(db_column='CYCLOBENZAPRINE_HCL')  # Field name made lowercase.
    dexilant = models.IntegerField(db_column='DEXILANT')  # Field name made lowercase.
    diazepam = models.IntegerField(db_column='DIAZEPAM')  # Field name made lowercase.
    diclofenac_sodium = models.IntegerField(db_column='DICLOFENAC_SODIUM')  # Field name made lowercase.
    dicyclomine_hcl = models.IntegerField(db_column='DICYCLOMINE_HCL')  # Field name made lowercase.
    digox = models.IntegerField(db_column='DIGOX')  # Field name made lowercase.
    digoxin = models.IntegerField(db_column='DIGOXIN')  # Field name made lowercase.
    diltiazem_24hr_cd = models.IntegerField(db_column='DILTIAZEM_24HR_CD')  # Field name made lowercase.
    diltiazem_24hr_er = models.IntegerField(db_column='DILTIAZEM_24HR_ER')  # Field name made lowercase.
    diltiazem_er = models.IntegerField(db_column='DILTIAZEM_ER')  # Field name made lowercase.
    diltiazem_hcl = models.IntegerField(db_column='DILTIAZEM_HCL')  # Field name made lowercase.
    diovan = models.IntegerField(db_column='DIOVAN')  # Field name made lowercase.
    diphenoxylate_atropine = models.IntegerField(db_column='DIPHENOXYLATE_ATROPINE')  # Field name made lowercase.
    divalproex_sodium = models.IntegerField(db_column='DIVALPROEX_SODIUM')  # Field name made lowercase.
    divalproex_sodium_er = models.IntegerField(db_column='DIVALPROEX_SODIUM_ER')  # Field name made lowercase.
    donepezil_hcl = models.IntegerField(db_column='DONEPEZIL_HCL')  # Field name made lowercase.
    dorzolamide_timolol = models.IntegerField(db_column='DORZOLAMIDE_TIMOLOL')  # Field name made lowercase.
    doxazosin_mesylate = models.IntegerField(db_column='DOXAZOSIN_MESYLATE')  # Field name made lowercase.
    doxepin_hcl = models.IntegerField(db_column='DOXEPIN_HCL')  # Field name made lowercase.
    doxycycline_hyclate = models.IntegerField(db_column='DOXYCYCLINE_HYCLATE')  # Field name made lowercase.
    duloxetine_hcl = models.IntegerField(db_column='DULOXETINE_HCL')  # Field name made lowercase.
    enalapril_maleate = models.IntegerField(db_column='ENALAPRIL_MALEATE')  # Field name made lowercase.
    escitalopram_oxalate = models.IntegerField(db_column='ESCITALOPRAM_OXALATE')  # Field name made lowercase.
    estradiol = models.IntegerField(db_column='ESTRADIOL')  # Field name made lowercase.
    exelon = models.IntegerField(db_column='EXELON')  # Field name made lowercase.
    famotidine = models.IntegerField(db_column='FAMOTIDINE')  # Field name made lowercase.
    felodipine_er = models.IntegerField(db_column='FELODIPINE_ER')  # Field name made lowercase.
    fenofibrate = models.IntegerField(db_column='FENOFIBRATE')  # Field name made lowercase.
    fentanyl = models.IntegerField(db_column='FENTANYL')  # Field name made lowercase.
    finasteride = models.IntegerField(db_column='FINASTERIDE')  # Field name made lowercase.
    flovent_hfa = models.IntegerField(db_column='FLOVENT_HFA')  # Field name made lowercase.
    fluconazole = models.IntegerField(db_column='FLUCONAZOLE')  # Field name made lowercase.
    fluoxetine_hcl = models.IntegerField(db_column='FLUOXETINE_HCL')  # Field name made lowercase.
    fluticasone_propionate = models.IntegerField(db_column='FLUTICASONE_PROPIONATE')  # Field name made lowercase.
    furosemide = models.IntegerField(db_column='FUROSEMIDE')  # Field name made lowercase.
    gabapentin = models.IntegerField(db_column='GABAPENTIN')  # Field name made lowercase.
    gemfibrozil = models.IntegerField(db_column='GEMFIBROZIL')  # Field name made lowercase.
    glimepiride = models.IntegerField(db_column='GLIMEPIRIDE')  # Field name made lowercase.
    glipizide = models.IntegerField(db_column='GLIPIZIDE')  # Field name made lowercase.
    glipizide_er = models.IntegerField(db_column='GLIPIZIDE_ER')  # Field name made lowercase.
    glipizide_xl = models.IntegerField(db_column='GLIPIZIDE_XL')  # Field name made lowercase.
    glyburide = models.IntegerField(db_column='GLYBURIDE')  # Field name made lowercase.
    haloperidol = models.IntegerField(db_column='HALOPERIDOL')  # Field name made lowercase.
    humalog = models.IntegerField(db_column='HUMALOG')  # Field name made lowercase.
    hydralazine_hcl = models.IntegerField(db_column='HYDRALAZINE_HCL')  # Field name made lowercase.
    hydrochlorothiazide = models.IntegerField(db_column='HYDROCHLOROTHIAZIDE')  # Field name made lowercase.
    hydrocodone_acetaminophen = models.IntegerField(db_column='HYDROCODONE_ACETAMINOPHEN')  # Field name made lowercase.
    hydrocortisone = models.IntegerField(db_column='HYDROCORTISONE')  # Field name made lowercase.
    hydromorphone_hcl = models.IntegerField(db_column='HYDROMORPHONE_HCL')  # Field name made lowercase.
    hydroxyzine_hcl = models.IntegerField(db_column='HYDROXYZINE_HCL')  # Field name made lowercase.
    ibandronate_sodium = models.IntegerField(db_column='IBANDRONATE_SODIUM')  # Field name made lowercase.
    ibuprofen = models.IntegerField(db_column='IBUPROFEN')  # Field name made lowercase.
    insulin_syringe = models.IntegerField(db_column='INSULIN_SYRINGE')  # Field name made lowercase.
    ipratropium_bromide = models.IntegerField(db_column='IPRATROPIUM_BROMIDE')  # Field name made lowercase.
    irbesartan = models.IntegerField(db_column='IRBESARTAN')  # Field name made lowercase.
    isosorbide_mononitrate_er = models.IntegerField(db_column='ISOSORBIDE_MONONITRATE_ER')  # Field name made lowercase.
    jantoven = models.IntegerField(db_column='JANTOVEN')  # Field name made lowercase.
    janumet = models.IntegerField(db_column='JANUMET')  # Field name made lowercase.
    januvia = models.IntegerField(db_column='JANUVIA')  # Field name made lowercase.
    ketoconazole = models.IntegerField(db_column='KETOCONAZOLE')  # Field name made lowercase.
    klor_con_10 = models.IntegerField(db_column='KLOR_CON_10')  # Field name made lowercase.
    klor_con_m10 = models.IntegerField(db_column='KLOR_CON_M10')  # Field name made lowercase.
    klor_con_m20 = models.IntegerField(db_column='KLOR_CON_M20')  # Field name made lowercase.
    labetalol_hcl = models.IntegerField(db_column='LABETALOL_HCL')  # Field name made lowercase.
    lactulose = models.IntegerField(db_column='LACTULOSE')  # Field name made lowercase.
    lamotrigine = models.IntegerField(db_column='LAMOTRIGINE')  # Field name made lowercase.
    lansoprazole = models.IntegerField(db_column='LANSOPRAZOLE')  # Field name made lowercase.
    lantus = models.IntegerField(db_column='LANTUS')  # Field name made lowercase.
    lantus_solostar = models.IntegerField(db_column='LANTUS_SOLOSTAR')  # Field name made lowercase.
    latanoprost = models.IntegerField(db_column='LATANOPROST')  # Field name made lowercase.
    levemir = models.IntegerField(db_column='LEVEMIR')  # Field name made lowercase.
    levemir_flexpen = models.IntegerField(db_column='LEVEMIR_FLEXPEN')  # Field name made lowercase.
    levetiracetam = models.IntegerField(db_column='LEVETIRACETAM')  # Field name made lowercase.
    levofloxacin = models.IntegerField(db_column='LEVOFLOXACIN')  # Field name made lowercase.
    levothyroxine_sodium = models.IntegerField(db_column='LEVOTHYROXINE_SODIUM')  # Field name made lowercase.
    lidocaine = models.IntegerField(db_column='LIDOCAINE')  # Field name made lowercase.
    lisinopril = models.IntegerField(db_column='LISINOPRIL')  # Field name made lowercase.
    lisinopril_hydrochlorothiazide = models.IntegerField(db_column='LISINOPRIL_HYDROCHLOROTHIAZIDE')  # Field name made lowercase.
    lithium_carbonate = models.IntegerField(db_column='LITHIUM_CARBONATE')  # Field name made lowercase.
    lorazepam = models.IntegerField(db_column='LORAZEPAM')  # Field name made lowercase.
    losartan_hydrochlorothiazide = models.IntegerField(db_column='LOSARTAN_HYDROCHLOROTHIAZIDE')  # Field name made lowercase.
    losartan_potassium = models.IntegerField(db_column='LOSARTAN_POTASSIUM')  # Field name made lowercase.
    lovastatin = models.IntegerField(db_column='LOVASTATIN')  # Field name made lowercase.
    lovaza = models.IntegerField(db_column='LOVAZA')  # Field name made lowercase.
    lumigan = models.IntegerField(db_column='LUMIGAN')  # Field name made lowercase.
    lyrica = models.IntegerField(db_column='LYRICA')  # Field name made lowercase.
    meclizine_hcl = models.IntegerField(db_column='MECLIZINE_HCL')  # Field name made lowercase.
    meloxicam = models.IntegerField(db_column='MELOXICAM')  # Field name made lowercase.
    metformin_hcl = models.IntegerField(db_column='METFORMIN_HCL')  # Field name made lowercase.
    metformin_hcl_er = models.IntegerField(db_column='METFORMIN_HCL_ER')  # Field name made lowercase.
    methadone_hcl = models.IntegerField(db_column='METHADONE_HCL')  # Field name made lowercase.
    methocarbamol = models.IntegerField(db_column='METHOCARBAMOL')  # Field name made lowercase.
    methotrexate = models.IntegerField(db_column='METHOTREXATE')  # Field name made lowercase.
    methylprednisolone = models.IntegerField(db_column='METHYLPREDNISOLONE')  # Field name made lowercase.
    metoclopramide_hcl = models.IntegerField(db_column='METOCLOPRAMIDE_HCL')  # Field name made lowercase.
    metolazone = models.IntegerField(db_column='METOLAZONE')  # Field name made lowercase.
    metoprolol_succinate = models.IntegerField(db_column='METOPROLOL_SUCCINATE')  # Field name made lowercase.
    metoprolol_tartrate = models.IntegerField(db_column='METOPROLOL_TARTRATE')  # Field name made lowercase.
    metronidazole = models.IntegerField(db_column='METRONIDAZOLE')  # Field name made lowercase.
    mirtazapine = models.IntegerField(db_column='MIRTAZAPINE')  # Field name made lowercase.
    montelukast_sodium = models.IntegerField(db_column='MONTELUKAST_SODIUM')  # Field name made lowercase.
    morphine_sulfate = models.IntegerField(db_column='MORPHINE_SULFATE')  # Field name made lowercase.
    morphine_sulfate_er = models.IntegerField(db_column='MORPHINE_SULFATE_ER')  # Field name made lowercase.
    mupirocin = models.IntegerField(db_column='MUPIROCIN')  # Field name made lowercase.
    nabumetone = models.IntegerField(db_column='NABUMETONE')  # Field name made lowercase.
    namenda = models.IntegerField(db_column='NAMENDA')  # Field name made lowercase.
    namenda_xr = models.IntegerField(db_column='NAMENDA_XR')  # Field name made lowercase.
    naproxen = models.IntegerField(db_column='NAPROXEN')  # Field name made lowercase.
    nasonex = models.IntegerField(db_column='NASONEX')  # Field name made lowercase.
    nexium = models.IntegerField(db_column='NEXIUM')  # Field name made lowercase.
    niacin_er = models.IntegerField(db_column='NIACIN_ER')  # Field name made lowercase.
    nifedical_xl = models.IntegerField(db_column='NIFEDICAL_XL')  # Field name made lowercase.
    nifedipine_er = models.IntegerField(db_column='NIFEDIPINE_ER')  # Field name made lowercase.
    nitrofurantoin_mono_macro = models.IntegerField(db_column='NITROFURANTOIN_MONO_MACRO')  # Field name made lowercase.
    nitrostat = models.IntegerField(db_column='NITROSTAT')  # Field name made lowercase.
    nortriptyline_hcl = models.IntegerField(db_column='NORTRIPTYLINE_HCL')  # Field name made lowercase.
    novolog = models.IntegerField(db_column='NOVOLOG')  # Field name made lowercase.
    novolog_flexpen = models.IntegerField(db_column='NOVOLOG_FLEXPEN')  # Field name made lowercase.
    nystatin = models.IntegerField(db_column='NYSTATIN')  # Field name made lowercase.
    olanzapine = models.IntegerField(db_column='OLANZAPINE')  # Field name made lowercase.
    omeprazole = models.IntegerField(db_column='OMEPRAZOLE')  # Field name made lowercase.
    ondansetron_hcl = models.IntegerField(db_column='ONDANSETRON_HCL')  # Field name made lowercase.
    ondansetron_odt = models.IntegerField(db_column='ONDANSETRON_ODT')  # Field name made lowercase.
    onglyza = models.IntegerField(db_column='ONGLYZA')  # Field name made lowercase.
    oxcarbazepine = models.IntegerField(db_column='OXCARBAZEPINE')  # Field name made lowercase.
    oxybutynin_chloride = models.IntegerField(db_column='OXYBUTYNIN_CHLORIDE')  # Field name made lowercase.
    oxybutynin_chloride_er = models.IntegerField(db_column='OXYBUTYNIN_CHLORIDE_ER')  # Field name made lowercase.
    oxycodone_acetaminophen = models.IntegerField(db_column='OXYCODONE_ACETAMINOPHEN')  # Field name made lowercase.
    oxycodone_hcl = models.IntegerField(db_column='OXYCODONE_HCL')  # Field name made lowercase.
    oxycontin = models.IntegerField(db_column='OXYCONTIN')  # Field name made lowercase.
    pantoprazole_sodium = models.IntegerField(db_column='PANTOPRAZOLE_SODIUM')  # Field name made lowercase.
    paroxetine_hcl = models.IntegerField(db_column='PAROXETINE_HCL')  # Field name made lowercase.
    phenobarbital = models.IntegerField(db_column='PHENOBARBITAL')  # Field name made lowercase.
    phenytoin_sodium_extended = models.IntegerField(db_column='PHENYTOIN_SODIUM_EXTENDED')  # Field name made lowercase.
    pioglitazone_hcl = models.IntegerField(db_column='PIOGLITAZONE_HCL')  # Field name made lowercase.
    polyethylene_glycol_3350 = models.IntegerField(db_column='POLYETHYLENE_GLYCOL_3350')  # Field name made lowercase.
    potassium_chloride = models.IntegerField(db_column='POTASSIUM_CHLORIDE')  # Field name made lowercase.
    pradaxa = models.IntegerField(db_column='PRADAXA')  # Field name made lowercase.
    pramipexole_dihydrochloride = models.IntegerField(db_column='PRAMIPEXOLE_DIHYDROCHLORIDE')  # Field name made lowercase.
    pravastatin_sodium = models.IntegerField(db_column='PRAVASTATIN_SODIUM')  # Field name made lowercase.
    prednisone = models.IntegerField(db_column='PREDNISONE')  # Field name made lowercase.
    premarin = models.IntegerField(db_column='PREMARIN')  # Field name made lowercase.
    primidone = models.IntegerField(db_column='PRIMIDONE')  # Field name made lowercase.
    proair_hfa = models.IntegerField(db_column='PROAIR_HFA')  # Field name made lowercase.
    promethazine_hcl = models.IntegerField(db_column='PROMETHAZINE_HCL')  # Field name made lowercase.
    propranolol_hcl = models.IntegerField(db_column='PROPRANOLOL_HCL')  # Field name made lowercase.
    propranolol_hcl_er = models.IntegerField(db_column='PROPRANOLOL_HCL_ER')  # Field name made lowercase.
    quetiapine_fumarate = models.IntegerField(db_column='QUETIAPINE_FUMARATE')  # Field name made lowercase.
    quinapril_hcl = models.IntegerField(db_column='QUINAPRIL_HCL')  # Field name made lowercase.
    raloxifene_hcl = models.IntegerField(db_column='RALOXIFENE_HCL')  # Field name made lowercase.
    ramipril = models.IntegerField(db_column='RAMIPRIL')  # Field name made lowercase.
    ranexa = models.IntegerField(db_column='RANEXA')  # Field name made lowercase.
    ranitidine_hcl = models.IntegerField(db_column='RANITIDINE_HCL')  # Field name made lowercase.
    restasis = models.IntegerField(db_column='RESTASIS')  # Field name made lowercase.
    risperidone = models.IntegerField(db_column='RISPERIDONE')  # Field name made lowercase.
    ropinirole_hcl = models.IntegerField(db_column='ROPINIROLE_HCL')  # Field name made lowercase.
    seroquel_xr = models.IntegerField(db_column='SEROQUEL_XR')  # Field name made lowercase.
    sertraline_hcl = models.IntegerField(db_column='SERTRALINE_HCL')  # Field name made lowercase.
    simvastatin = models.IntegerField(db_column='SIMVASTATIN')  # Field name made lowercase.
    sotalol = models.IntegerField(db_column='SOTALOL')  # Field name made lowercase.
    spiriva = models.IntegerField(db_column='SPIRIVA')  # Field name made lowercase.
    spironolactone = models.IntegerField(db_column='SPIRONOLACTONE')  # Field name made lowercase.
    sucralfate = models.IntegerField(db_column='SUCRALFATE')  # Field name made lowercase.
    sulfamethoxazole_trimethoprim = models.IntegerField(db_column='SULFAMETHOXAZOLE_TRIMETHOPRIM')  # Field name made lowercase.
    sumatriptan_succinate = models.IntegerField(db_column='SUMATRIPTAN_SUCCINATE')  # Field name made lowercase.
    symbicort = models.IntegerField(db_column='SYMBICORT')  # Field name made lowercase.
    synthroid = models.IntegerField(db_column='SYNTHROID')  # Field name made lowercase.
    tamsulosin_hcl = models.IntegerField(db_column='TAMSULOSIN_HCL')  # Field name made lowercase.
    temazepam = models.IntegerField(db_column='TEMAZEPAM')  # Field name made lowercase.
    terazosin_hcl = models.IntegerField(db_column='TERAZOSIN_HCL')  # Field name made lowercase.
    timolol_maleate = models.IntegerField(db_column='TIMOLOL_MALEATE')  # Field name made lowercase.
    tizanidine_hcl = models.IntegerField(db_column='TIZANIDINE_HCL')  # Field name made lowercase.
    tolterodine_tartrate_er = models.IntegerField(db_column='TOLTERODINE_TARTRATE_ER')  # Field name made lowercase.
    topiramate = models.IntegerField(db_column='TOPIRAMATE')  # Field name made lowercase.
    toprol_xl = models.IntegerField(db_column='TOPROL_XL')  # Field name made lowercase.
    torsemide = models.IntegerField(db_column='TORSEMIDE')  # Field name made lowercase.
    tramadol_hcl = models.IntegerField(db_column='TRAMADOL_HCL')  # Field name made lowercase.
    travatan_z = models.IntegerField(db_column='TRAVATAN_Z')  # Field name made lowercase.
    trazodone_hcl = models.IntegerField(db_column='TRAZODONE_HCL')  # Field name made lowercase.
    triamcinolone_acetonide = models.IntegerField(db_column='TRIAMCINOLONE_ACETONIDE')  # Field name made lowercase.
    triamterene_hydrochlorothiazid = models.IntegerField(db_column='TRIAMTERENE_HYDROCHLOROTHIAZID')  # Field name made lowercase.
    valacyclovir = models.IntegerField(db_column='VALACYCLOVIR')  # Field name made lowercase.
    valsartan = models.IntegerField(db_column='VALSARTAN')  # Field name made lowercase.
    valsartan_hydrochlorothiazide = models.IntegerField(db_column='VALSARTAN_HYDROCHLOROTHIAZIDE')  # Field name made lowercase.
    venlafaxine_hcl = models.IntegerField(db_column='VENLAFAXINE_HCL')  # Field name made lowercase.
    venlafaxine_hcl_er = models.IntegerField(db_column='VENLAFAXINE_HCL_ER')  # Field name made lowercase.
    ventolin_hfa = models.IntegerField(db_column='VENTOLIN_HFA')  # Field name made lowercase.
    verapamil_er = models.IntegerField(db_column='VERAPAMIL_ER')  # Field name made lowercase.
    vesicare = models.IntegerField(db_column='VESICARE')  # Field name made lowercase.
    voltaren = models.IntegerField(db_column='VOLTAREN')  # Field name made lowercase.
    vytorin = models.IntegerField(db_column='VYTORIN')  # Field name made lowercase.
    warfarin_sodium = models.IntegerField(db_column='WARFARIN_SODIUM')  # Field name made lowercase.
    xarelto = models.IntegerField(db_column='XARELTO')  # Field name made lowercase.
    zetia = models.IntegerField(db_column='ZETIA')  # Field name made lowercase.
    ziprasidone_hcl = models.IntegerField(db_column='ZIPRASIDONE_HCL')  # Field name made lowercase.
    zolpidem_tartrate = models.IntegerField(db_column='ZOLPIDEM_TARTRATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescriber_info'


class Triple(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    drug = models.CharField(db_column='Drug', max_length=50)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'triple'




