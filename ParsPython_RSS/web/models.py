# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Dslinktypes(models.Model):
    inid = models.IntegerField(primary_key=True)
    intype = models.SmallIntegerField(null=True, blank=True)
    stname = models.CharField(max_length=255, blank=True)
    stinversename = models.CharField(max_length=255, blank=True)
    inorder = models.IntegerField(null=True, blank=True)
    imicon = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'dslinktypes'

class Dstypes(models.Model):
    inid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=255, blank=True)
    inidkeyattribute = models.IntegerField(null=True, blank=True)
    indefaultstate = models.IntegerField(null=True, blank=True)
    binoversions = models.BooleanField(null=True, blank=True)
    biabstract = models.BooleanField(null=True, blank=True)
    bidocument = models.BooleanField(null=True, blank=True)
    bicanbeproject = models.BooleanField(null=True, blank=True)
    imicon = models.TextField(blank=True) # This field type is a guess.
    iniddocumentviewer = models.IntegerField(null=True, blank=True)
    bitech = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'dstypes'

class Dsattributes(models.Model):
    inid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=255)
    intype = models.SmallIntegerField(null=True, blank=True)
    stdefault = models.CharField(max_length=255, blank=True)
    bisystem = models.BooleanField(null=True, blank=True)
    indefaccess = models.SmallIntegerField(null=True, blank=True)
    bionlylistitems = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'dsattributes'

class Rltypesandtypes(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidparent = models.IntegerField(null=True, blank=True)
    inidchild = models.IntegerField(null=True, blank=True)
    inidlinktype = models.IntegerField(null=True, blank=True)
    biquantity = models.SmallIntegerField(null=True, blank=True)
    inherited = models.IntegerField(null=True, blank=True)
    inmultilink = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rltypesandtypes'

class Rltypesandattributes(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidtype = models.IntegerField(null=True, blank=True)
    inidattribute = models.IntegerField(null=True, blank=True)
    biobligatory = models.BooleanField(null=True, blank=True)
    strule = models.CharField(max_length=255, blank=True)
    inherited = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rltypesandattributes'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = u'auth_group'

class Rezppi(models.Model):
    naim = models.CharField(max_length=255, blank=True)
    grere = models.CharField(max_length=100, blank=True)
    okp = models.CharField(max_length=255, blank=True)
    os = models.CharField(max_length=255, blank=True)
    vhodit = models.CharField(max_length=255, blank=True)
    kolvo = models.FloatField(null=True, blank=True)
    itogo = models.FloatField(null=True, blank=True)
    prim = models.CharField(max_length=255, blank=True)
    sort1 = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'rezppi'

class Zakppi(models.Model):
    naim = models.CharField(max_length=255, blank=True)
    norm = models.CharField(max_length=255, blank=True)
    prov = models.CharField(max_length=255, blank=True)
    razrab = models.CharField(max_length=255, blank=True)
    utv = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'zakppi'

class Rezvpr(models.Model):
    typ = models.CharField(max_length=255, blank=True)
    kudavh = models.CharField(max_length=255, blank=True)
    dn = models.CharField(max_length=255, blank=True)
    naim = models.CharField(max_length=255, blank=True)
    kol = models.FloatField(null=True, blank=True)
    itogo = models.FloatField(null=True, blank=True)
    ilevel = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    sort1 = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'rezvpr'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class Gpi(models.Model):
    typ_pred = models.CharField(max_length=2, blank=True)
    kod_pred = models.CharField(max_length=20, blank=True)
    nomn = models.CharField(max_length=8, blank=True)
    naim_pred = models.CharField(max_length=30, blank=True)
    ed_pr = models.CharField(max_length=3, blank=True)
    massa = models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)
    rasz01 = models.CharField(max_length=5, blank=True)
    rasz02 = models.CharField(max_length=5, blank=True)
    rasz03 = models.CharField(max_length=5, blank=True)
    rasz04 = models.CharField(max_length=5, blank=True)
    rasz05 = models.CharField(max_length=5, blank=True)
    rasz06 = models.CharField(max_length=5, blank=True)
    rasz07 = models.CharField(max_length=5, blank=True)
    rasz08 = models.CharField(max_length=5, blank=True)
    rasz09 = models.CharField(max_length=5, blank=True)
    rasz10 = models.CharField(max_length=5, blank=True)
    rasz11 = models.CharField(max_length=5, blank=True)
    rasz12 = models.CharField(max_length=5, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    n_izv = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'gpi'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class Gpd(models.Model):
    typ_pred = models.CharField(max_length=2, blank=True)
    kod_pred = models.CharField(max_length=20, blank=True)
    naim_pred = models.CharField(max_length=30, blank=True)
    ed_pr = models.CharField(max_length=3, blank=True)
    massa = models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)
    kolzag = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    razmer1 = models.CharField(max_length=8, blank=True)
    razmer2 = models.CharField(max_length=8, blank=True)
    razmer3 = models.CharField(max_length=8, blank=True)
    rasz01 = models.CharField(max_length=5, blank=True)
    rasz02 = models.CharField(max_length=5, blank=True)
    rasz03 = models.CharField(max_length=5, blank=True)
    rasz04 = models.CharField(max_length=5, blank=True)
    rasz05 = models.CharField(max_length=5, blank=True)
    rasz06 = models.CharField(max_length=5, blank=True)
    rasz07 = models.CharField(max_length=5, blank=True)
    rasz08 = models.CharField(max_length=5, blank=True)
    rasz09 = models.CharField(max_length=5, blank=True)
    rasz10 = models.CharField(max_length=5, blank=True)
    rasz11 = models.CharField(max_length=5, blank=True)
    rasz12 = models.CharField(max_length=5, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    n_izv = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'gpd'

class Si(models.Model):
    typ_predk = models.CharField(max_length=2, blank=True)
    kod_predk = models.CharField(max_length=20, blank=True)
    typ_preds = models.CharField(max_length=2, blank=True)
    kod_preds = models.CharField(max_length=20, blank=True)
    kol = models.DecimalField(null=True, max_digits=13, decimal_places=6, blank=True)
    priz_use = models.DecimalField(null=True, max_digits=1, decimal_places=0, blank=True)
    nom_oper = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    rasz01 = models.CharField(max_length=5, blank=True)
    rasz02 = models.CharField(max_length=5, blank=True)
    rasz03 = models.CharField(max_length=5, blank=True)
    rasz04 = models.CharField(max_length=5, blank=True)
    rasz05 = models.CharField(max_length=5, blank=True)
    rasz06 = models.CharField(max_length=5, blank=True)
    rasz07 = models.CharField(max_length=5, blank=True)
    rasz08 = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = u'si'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class Ptn(models.Model):
    kniga = models.CharField(max_length=4, blank=True)
    kod_pred = models.CharField(max_length=20, blank=True)
    kod_zex = models.CharField(max_length=5, blank=True)
    uch = models.CharField(max_length=2, blank=True)
    nom_oper = models.CharField(max_length=3, blank=True)
    kod_wr = models.CharField(max_length=3, blank=True)
    shn = models.CharField(max_length=1, blank=True)
    wo = models.CharField(max_length=2, blank=True)
    ts = models.CharField(max_length=2, blank=True)
    pr = models.CharField(max_length=1, blank=True)
    sne = models.CharField(max_length=1, blank=True)
    norma = models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)
    normpzw = models.DecimalField(null=True, max_digits=5, decimal_places=3, blank=True)
    rasc = models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)
    rascpzw = models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)
    pi = models.CharField(max_length=2, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    reserv = models.CharField(max_length=30, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    typ_pred = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'ptn'

class Mater(models.Model):
    kod_pred = models.CharField(max_length=20, blank=True)
    ves = models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)
    kod_preds = models.CharField(max_length=20, blank=True)
    ed_izm = models.CharField(max_length=10, blank=True)
    kod_zex = models.CharField(max_length=5, blank=True)
    norma = models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True)
    data = models.DateTimeField(null=True, blank=True)
    typ_pred = models.CharField(max_length=2, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    kod_preds1 = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = u'mater'

class Gpm(models.Model):
    typ_pred = models.CharField(max_length=2, blank=True)
    kod_pred = models.CharField(max_length=20, blank=True)
    naim_pred = models.CharField(max_length=150, blank=True)
    ed_pr = models.CharField(max_length=3, blank=True)
    ed_kn = models.CharField(max_length=3, blank=True)
    ed_mt = models.CharField(max_length=3, blank=True)
    massa = models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)
    sortam = models.CharField(max_length=16, blank=True)
    gost_s = models.CharField(max_length=40, blank=True)
    marka = models.CharField(max_length=40, blank=True)
    gost_m = models.CharField(max_length=40, blank=True)
    profil = models.CharField(max_length=10, blank=True)
    razmer = models.CharField(max_length=21, blank=True)
    postav = models.CharField(max_length=78, blank=True)
    n_bill = models.CharField(max_length=35, blank=True)
    ed_izm = models.CharField(max_length=10, blank=True)
    price = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    razdel = models.CharField(max_length=2, blank=True)
    osn = models.DecimalField(null=True, max_digits=1, decimal_places=0, blank=True)
    class Meta:
        db_table = u'gpm'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class Gp80(models.Model):
    typ_pred = models.CharField(max_length=2, blank=True)
    kod_pred = models.CharField(max_length=20, blank=True)
    naim_pred = models.CharField(max_length=43, blank=True)
    ed_pr = models.CharField(max_length=3, blank=True)
    massa = models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)
    kolzag = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    razmer1 = models.CharField(max_length=8, blank=True)
    razmer2 = models.CharField(max_length=8, blank=True)
    razmer3 = models.CharField(max_length=8, blank=True)
    rasz01 = models.CharField(max_length=5, blank=True)
    rasz02 = models.CharField(max_length=5, blank=True)
    rasz03 = models.CharField(max_length=5, blank=True)
    rasz04 = models.CharField(max_length=5, blank=True)
    rasz05 = models.CharField(max_length=5, blank=True)
    rasz06 = models.CharField(max_length=5, blank=True)
    rasz07 = models.CharField(max_length=5, blank=True)
    rasz08 = models.CharField(max_length=5, blank=True)
    rasz09 = models.CharField(max_length=5, blank=True)
    rasz10 = models.CharField(max_length=5, blank=True)
    rasz11 = models.CharField(max_length=5, blank=True)
    rasz12 = models.CharField(max_length=5, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    n_izv = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'gp80'

class Pokritia(models.Model):
    kod_pred = models.CharField(max_length=20, blank=True)
    ves = models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)
    kod_preds = models.CharField(max_length=20, blank=True)
    ed_izm = models.CharField(max_length=10, blank=True)
    kod_zex = models.CharField(max_length=5, blank=True)
    norma = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = u'pokritia'

class Drag(models.Model):
    data_vvoda = models.DateTimeField(null=True, blank=True)
    nom_izv = models.CharField(max_length=3, blank=True)
    d_n = models.CharField(max_length=20, blank=True)
    naim = models.CharField(max_length=18, blank=True)
    td = models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)
    shd = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dd = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tz1 = models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)
    shz1 = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dz1 = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    kdz1 = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    tz2 = models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)
    shz2 = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dz2 = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    kdz2 = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    pm1 = models.CharField(max_length=2, blank=True)
    kp1 = models.CharField(max_length=4, blank=True)
    zex = models.CharField(max_length=5, blank=True)
    spokr = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    pr = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    v03 = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    b03 = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    n03 = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    ko1 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do1 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz1 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko2 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do2 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz2 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko3 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do3 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz3 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko4 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do4 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz4 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko5 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do5 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz5 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko6 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do6 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz6 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko7 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do7 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz7 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko8 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do8 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz8 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko9 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do9 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz9 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ko10 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    do10 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    diz10 = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    l_str = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    typ_pred = models.CharField(max_length=2, blank=True)
    srt = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = u'drag'

class M2018(models.Model):
    data_vv = models.DateTimeField(null=True, blank=True)
    nom_izv = models.CharField(max_length=3, blank=True)
    pm1 = models.CharField(max_length=2, blank=True)
    km = models.CharField(max_length=12, blank=True)
    kp1 = models.CharField(max_length=4, blank=True)
    naim_mat = models.CharField(max_length=60, blank=True)
    shifr_p = models.CharField(max_length=10, blank=True)
    nr = models.DecimalField(null=True, max_digits=12, decimal_places=8, blank=True)
    unpr = models.DecimalField(null=True, max_digits=12, decimal_places=8, blank=True)
    v03 = models.DecimalField(null=True, max_digits=12, decimal_places=8, blank=True)
    b03 = models.DecimalField(null=True, max_digits=12, decimal_places=8, blank=True)
    kfp = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kzt = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kzp = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat1 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks1 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat2 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks2 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat3 = models.CharField(max_length=3, blank=True)
    ks3 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat4 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks4 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat5 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks5 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat6 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks6 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    kmat7 = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    ks7 = models.DecimalField(null=True, max_digits=6, decimal_places=4, blank=True)
    class Meta:
        db_table = u'm2018'

class Drag2(models.Model):
    d_n = models.CharField(max_length=20, blank=True)
    naim_mat = models.CharField(max_length=20, blank=True)
    nr = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    class Meta:
        db_table = u'drag2'

class Drag3(models.Model):
    d_n = models.CharField(max_length=20, blank=True)
    pm1 = models.CharField(max_length=2, blank=True)
    kp1 = models.CharField(max_length=4, blank=True)
    zex = models.CharField(max_length=5, blank=True)
    naim_mat = models.CharField(max_length=20, blank=True)
    pr = models.DecimalField(null=True, max_digits=13, decimal_places=8, blank=True)
    class Meta:
        db_table = u'drag3'

class RezPtn2(models.Model):
    kod_pred = models.CharField(max_length=20, blank=True)
    zex = models.CharField(max_length=5, blank=True)
    kod_wr = models.CharField(max_length=3, blank=True)
    naim_wr = models.CharField(max_length=40, blank=True)
    sne = models.CharField(max_length=1, blank=True)
    shn = models.CharField(max_length=1, blank=True)
    trud = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    trud_tosn = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    nom_oper = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'rez_ptn2'

class RezPtn1(models.Model):
    zex = models.CharField(max_length=5, blank=True)
    kod_wr = models.CharField(max_length=3, blank=True)
    naim_wr = models.CharField(max_length=40, blank=True)
    trud = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    trud_tosn = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    class Meta:
        db_table = u'rez_ptn1'

class Dsstates(models.Model):
    inid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=255, blank=True)
    imicon = models.TextField(blank=True) # This field type is a guess.
    bisavelinkhistory = models.BooleanField(null=True, blank=True)
    class Meta:
        db_table = u'dsstates'

class Stversions(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidmain = models.IntegerField(null=True, blank=True)
    inidstate = models.ForeignKey(Dsstates, null=True, db_column='inidstate', blank=True)
    stnumber = models.IntegerField(null=True, blank=True)
    inowner = models.IntegerField(null=True, blank=True)
    dtdateofcreate = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'stversions'

class Rvwattributes1(models.Model):
    name = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    idversion = models.IntegerField(null=True, blank=True)
    idattr = models.IntegerField(null=True, blank=True)
    attrtype = models.SmallIntegerField(null=True, blank=True)
    asinteger = models.IntegerField(null=True, blank=True)
    asfloat = models.FloatField(null=True, blank=True)
    asdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'rvwattributes1'

class Rvwrelations1(models.Model):
    relationname = models.CharField(max_length=255, blank=True)
    inversename = models.CharField(max_length=255, blank=True)
    id = models.IntegerField(null=True, blank=True)
    idparent = models.IntegerField(null=True, blank=True)
    idchild = models.IntegerField(null=True, blank=True)
    idlinktype = models.IntegerField(null=True, blank=True)
    minquantity = models.FloatField(null=True, blank=True)
    maxquantity = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'rvwrelations1'

class Rvwversions1(models.Model):
    type = models.CharField(max_length=255, blank=True)
    id = models.IntegerField(null=True, blank=True)
    idtype = models.IntegerField(null=True, blank=True)
    idproduct = models.IntegerField(null=True, blank=True)
    product = models.CharField(max_length=255, blank=True)
    idstate = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)
    dateofcreate = models.DateField(null=True, blank=True)
    idowner = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rvwversions1'

class Rvwrelationattributes1(models.Model):
    name = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
    idrelation = models.IntegerField(null=True, blank=True)
    idattr = models.IntegerField(null=True, blank=True)
    attrtype = models.SmallIntegerField(null=True, blank=True)
    asinteger = models.IntegerField(null=True, blank=True)
    asfloat = models.FloatField(null=True, blank=True)
    asdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'rvwrelationattributes1'

class Stmain(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidtype = models.IntegerField(null=True, blank=True)
    stkeyattr = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'stmain'

class Stattributes(models.Model):
    inid = models.IntegerField()
    inidversion = models.IntegerField(null=True, blank=True)
    inidattr = models.IntegerField(null=True, blank=True)
    stvalue = models.CharField(max_length=255, blank=True)
    invalue = models.IntegerField(null=True, blank=True)
    revalue = models.FloatField(null=True, blank=True)
    dtvalue = models.DateTimeField(null=True, blank=True)
    inidunit = models.IntegerField(null=True, blank=True)
    inidexternal = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    dtmodified = models.DateTimeField(null=True, blank=True)
    inidorgowner = models.IntegerField(null=True, blank=True)
    dtsynchdate = models.DateTimeField(null=True, blank=True)
    stguid = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'stattributes'

class Stlinks(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidparent = models.IntegerField()
    inidchild = models.IntegerField()
    inidtyperel = models.IntegerField()
    inmaxquantity = models.FloatField(null=True, blank=True)
    inminquantity = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'stlinks'

class Stlinkattributes(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidlink = models.IntegerField(null=True, blank=True)
    inidlinkattr = models.IntegerField(null=True, blank=True)
    stvalue = models.CharField(max_length=255, blank=True)
    invalue = models.IntegerField(null=True, blank=True)
    revalue = models.FloatField(null=True, blank=True)
    dtvalue = models.DateTimeField(null=True, blank=True)
    inidunit = models.IntegerField(null=True, blank=True)
    inidexternal = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    dtmodified = models.DateTimeField(null=True, blank=True)
    inidorgowner = models.IntegerField(null=True, blank=True)
    dtsynchdate = models.DateTimeField(null=True, blank=True)
    stguid = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'stlinkattributes'

class RezMat1(models.Model):
    d_n = models.CharField(max_length=255, blank=True)
    qty1 = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    kod_mat = models.CharField(max_length=255, blank=True)
    naim_mat = models.CharField(max_length=255, blank=True)
    zex = models.CharField(max_length=255, blank=True)
    ed_izm = models.CharField(max_length=255, blank=True)
    norm_det = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    norm_izd = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    class Meta:
        db_table = u'rez_mat1'

class Sprwr(models.Model):
    kod_wr = models.CharField(max_length=3, blank=True)
    naim_wr = models.CharField(max_length=40, blank=True)
    pzw = models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)
    class Meta:
        db_table = u'sprwr'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class Rltypesandlinkattributes(models.Model):
    inid = models.IntegerField(primary_key=True)
    inidtypeandtype = models.IntegerField(null=True, blank=True)
    inidattribute = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rltypesandlinkattributes'

class Rabd26Res(models.Model):
    sort = models.IntegerField(null=True, blank=True)
    naim = models.CharField(max_length=255, blank=True)
    kudavh = models.CharField(max_length=255, blank=True)
    obozn = models.CharField(max_length=255, blank=True)
    kol = models.FloatField(null=True, blank=True)
    kol_izd = models.FloatField(null=True, blank=True)
    metall = models.CharField(max_length=100, blank=True)
    massa = models.FloatField(null=True, blank=True)
    mass_izd = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'rabd26_res'

class Rabd262Res(models.Model):
    d_n = models.CharField(max_length=255, blank=True)
    pm1 = models.CharField(max_length=2, blank=True)
    kp1 = models.CharField(max_length=4, blank=True)
    zex = models.CharField(max_length=5, blank=True)
    kol_izd = models.FloatField(null=True, blank=True)
    metall = models.CharField(max_length=100, blank=True)
    massa = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'rabd262_res'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

