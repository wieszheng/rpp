# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 17:23
@Author   : wieszheng
@Software : PyCharm
"""
import os
import sys

buildPath = 'build'  # 存放最终打包成app的相对路径
console = False  # 是否展示终端
appName = "RPP"  # 项目名称
version = "1.0.01"  # 版本号

# 添加文件到打包中
addDll = ""
# 添加文件夹到打包中
addModules = ""


def spec_first_part():
    return f'''# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import PyInstaller.config

# 存放最终打包成app的相对路径
buildPath = '{buildPath}'
PyInstaller.config.CONF['distpath'] = buildPath

# 存放打包成app的中间文件的相对路径
cachePath = os.path.join(buildPath, 'cache')
if not os.path.exists(cachePath):
    os.makedirs(cachePath)
PyInstaller.config.CONF['workpath'] = cachePath

# icon相对路径
icoPath = os.path.join('static', 'app.ico' if sys.platform.lower() == 'win32' else 'app.icns')

# 项目名称
appName = '{appName}'

# 版本号
version = '{version}'


a = Analysis(['main.py'],
            pathex=[],
            binaries=[{addDll}],
            datas=[{addModules}],
            hiddenimports=[],
            hookspath=[],
            hooksconfig={{}},
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data)

'''


# 打包为一个APP文件
def spec_package_part_app():
    return f'''
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=appName,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console={console},
        disable_windowed_traceback=False,
        target_arch=None,  # x86_64, arm64, universal2
        codesign_identity=None,
        entitlements_file=None)
coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name=appName)
app = BUNDLE(coll,
            name=appName+'.app',
            icon=icoPath,
            version=version,
            bundle_identifier=None)
    
'''


# 打包为一个exe文件
def spec_package_part_exe():
    return f'''
exe = EXE(pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name=appName,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console={console},
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icoPath)
    
'''


# 以文件夹形式存在
def spec_unpackage_part_exe():
    return f'''
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=appName,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console={console},
        disable_windowed_traceback=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icoPath)
coll = COLLECT(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            strip=False,
            upx=True,
            upx_exclude=[],
            name=appName)
    
'''


spec_dir = os.path.dirname(__file__)

system = sys.platform.lower()

if system == 'win32':
    console = False
    # windows.spec
    with open(os.path.join(spec_dir, 'build_windows.spec'), 'w+', encoding='utf-8') as f:
        f.write(spec_first_part() + spec_package_part_exe())
    # windows-folder.spec
    with open(os.path.join(spec_dir, 'build_windows-folder.spec'), 'w+', encoding='utf-8') as f:
        f.write(spec_first_part() + spec_unpackage_part_exe())

elif system == 'linux':
    console = False
    with open(os.path.join(spec_dir, 'build_linux.spec'), 'w+', encoding='utf-8') as f:
        f.write(spec_first_part() + spec_package_part_exe())
elif system == 'darwin':
    console = False
    with open(os.path.join(spec_dir, 'build_macos.spec'), 'w+', encoding='utf-8') as f:
        f.write(spec_first_part() + spec_package_part_app())

else:
    raise NotImplementedError(f"不支持的平台: {system}")
