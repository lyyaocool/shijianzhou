# -*- mode: python -*-

block_cipher = None


a = Analysis(['day03.py'],
             pathex=['C:\\Users\\lenovo\\Desktop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='day03',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
