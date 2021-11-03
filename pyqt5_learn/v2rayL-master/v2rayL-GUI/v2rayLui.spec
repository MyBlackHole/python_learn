# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['v2rayLui.py'],
             pathex=['config.py', 'sub2conf_api.py', 'v2rayL_api.py', 'v2rayL_threads.py', 'utils.py', '/media/black/BlackHole/Documents/PycharmProjects/PyQt5/v2rayL-master/v2rayL-GUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='v2rayLui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='images/logo.ico')
