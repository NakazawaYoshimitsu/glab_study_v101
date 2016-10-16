#-----------------------------------------------------------------------
#	bihin アプリケーションのmodels
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.db import models

# Create your models here.

#-----------------------------------------------------------------------
#	備品データの選択項目
#-----------------------------------------------------------------------
PCTYPE_CHOICES = (
    (0, 'ノートパソコン'),
    (1, 'デスクトップパソコン' )
)
SHISAN_CHOICES = (
    (0, '購入品'),
    (1, 'リース' )
)
STATUS_CHOICES = (
    (0, '保管棚'),
    (1, '貸出中'),
    (2, '廃棄'),
)
#-----------------------------------------------------------------------
#	Bihin：
#   Bihin DB のモデルを定義する.
#-----------------------------------------------------------------------
class Bihin(models.Model):
    """備品"""
    bihin_no = models.CharField('管理No', unique=True, max_length=255, help_text='<small><small>ex.) JSL.NT.123456</small></small>')
    bihin_type = models.IntegerField('種別', choices=PCTYPE_CHOICES)
    bihin_manufct = models.CharField('メーカー', max_length=255, help_text='<small><small>ex.) Apple/DELL/lenovo</small></small>')
    bihin_name = models.CharField('名称', max_length=255)
    bihin_os = models.CharField('OS', max_length=255)
    bihin_cpu = models.CharField('CPU', max_length=255)
    bihin_hdd = models.CharField('HDD容量', max_length=255)
    bihin_mem = models.CharField('メモリ', max_length=255)
    bihin_mediadrv = models.CharField('メディアドライブ', blank=True, max_length=255)
    bihin_dispsize = models.CharField('付属品：ディスプレイ(size)', blank=True, max_length=255)
    bihin_dispno = models.CharField('付属品：ディスプレイ(管理No)', blank=True, max_length=255)
    bihin_keyno = models.CharField('付属品：キーボード(管理No)', blank=True, max_length=255)
    bihin_mouseno = models.CharField('付属品：マウス(管理No)', blank=True, max_length=255)
    bihin_shisan = models.IntegerField('資産', choices=SHISAN_CHOICES)
    bihin_date = models.DateField('登録日', help_text='<small><small>ex.) 2016-09-12</small></small>')
    bihin_lease = models.DateField('リース期限日', null=True, blank=True, help_text='<small><small>ex.) 2016-09-12</small></small>')
    bihin_ipaddr = models.CharField('IPアドレス', blank=True, max_length=255)
    bihin_sts = models.IntegerField('状態', choices=STATUS_CHOICES)
    bihin_user = models.CharField('使用者', blank=True, max_length=255)
    bihin_prj = models.CharField('使用プロジェクト', blank=True, max_length=255)
    bihin_text = models.TextField('備考', null=True)

