# -*- mode: python -*-

block_cipher = None


a = Analysis(['alien.py', 'alien_invasion.py', 'asuna.py', 'bullet.py', 'button.py', 'game_functions.py', 'game_stats.py', 'scoreboard.py', 'settings.py', 'ship.py'],
             pathex=['E:\\PyWorkSpace\\Aliens War'],
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
          name='alien',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon\\alien.ico')
