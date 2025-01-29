# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('venv/lib/python3.12/site-packages/uiautomator2/assets/u2.jar', 'venv/lib/python3.12/site-packages/uiautomator2/assets'), ('venv/lib/python3.12/site-packages/setuptools/config/distutils.schema.json', 'venv/lib/python3.12/site-packages/setuptools/config'), ('venv/lib/python3.12/site-packages/setuptools/config/setuptools.schema.json', 'venv/lib/python3.12/site-packages/setuptools/config'), ('venv/lib/python3.12/site-packages/retry-0.9.2.dist-info/metadata.json', 'venv/lib/python3.12/site-packages/retry-0.9.2.dist-info'), ('venv/lib/python3.12/site-packages/retry-0.9.2.dist-info/pbr.json', 'venv/lib/python3.12/site-packages/retry-0.9.2.dist-info'), ('venv/lib/python3.12/site-packages/uiautomator2/assets/version.json', 'venv/lib/python3.12/site-packages/uiautomator2/assets'), ('venv/lib/python3.12/site-packages/adbutils-2.8.0.dist-info/pbr.json', 'venv/lib/python3.12/site-packages/adbutils-2.8.0.dist-info'), ('venv/lib/python3.12/site-packages/decorator-5.1.1.dist-info/pbr.json', 'venv/lib/python3.12/site-packages/decorator-5.1.1.dist-info'), ('venv/lib/python3.12/site-packages/cigam-0.0.3.dist-info/metadata.json', 'venv/lib/python3.12/site-packages/cigam-0.0.3.dist-info'), ('venv/lib/python3.12/site-packages/setuptools/command/launcher manifest.xml', 'venv/lib/python3.12/site-packages/setuptools/command'), ('venv/lib/python3.12/site-packages/lxml/isoschematron/resources/xsl', 'venv/lib/python3.12/site-packages/lxml/isoschematron/resources'), ('venv/lib/python3.12/site-packages/lxml/isoschematron/resources/rng', 'venv/lib/python3.12/site-packages/lxml/isoschematron/resources'), ('/home/setu/Projects/CrashScopeLLM/spl3/venv/lib/python3.12/site-packages/uiautomator2/assets/sync.sh', 'uiautomator2/assets'), ('/home/setu/Projects/CrashScopeLLM/spl3/venv/lib/python3.12/site-packages/uiautomator2/assets/u2.jar', 'uiautomator2/assets'), ('/home/setu/Projects/CrashScopeLLM/spl3/venv/lib/python3.12/site-packages/uiautomator2/assets/version.json', 'uiautomator2/assets'), ('/home/setu/Projects/CrashScopeLLM/spl3/venv/lib/python3.12/site-packages/uiautomator2/assets/app-uiautomator.apk', 'uiautomator2/assets'), ('/home/setu/Projects/CrashScopeLLM/spl3/venv/lib/python3.12/site-packages/uiautomator2/assets/.gitignore', 'uiautomator2/assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='spl3exec',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
