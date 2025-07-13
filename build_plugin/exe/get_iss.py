# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 18:57
@Author   : wieszheng
@Software : PyCharm
"""
import sys
import os

app_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(app_dir)

from build_plugin.config import Config

appName = Config.appName  # 应用名称
appVersion = Config.appVersion  # 应用版本号
appVersion = appVersion[1:]  # 去掉第一位V
appDeveloper = Config.appDeveloper  # 应用开发者
appBlogs = Config.appBlogs  # 个人博客

buildDir = os.path.join(app_dir, 'build')
logoPath = os.path.join(app_dir, 'static', 'logo.ico')
appISSID = Config.appISSID  # 安装包唯一GUID

if not os.path.exists(buildDir):
    print(f"错误：构建目录不存在: {buildDir}")
    sys.exit(1)

if not os.path.exists(logoPath):
    print(f"错误：图标文件不存在: {logoPath}")
    sys.exit(1)


# 获取配置文件内容
def get_iss():
    return '''; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

#define MyAppName "''' + appName + '''"
#define MyAppVersion "''' + appVersion + '''"
#define MyAppPublisher "''' + appDeveloper + '''"
#define MyAppURL "''' + appBlogs + '''"
#define MyAppExeName "''' + appName + '''.exe"
#define MyAppAssocName MyAppName + " 文件"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
AppId={{''' + appISSID + '''}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes

OutputDir=''' + buildDir + '''
OutputBaseFilename=''' + appName + '''-V''' + appVersion + '''_Windows
SetupIconFile=''' + logoPath + '''
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimp"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "''' + buildDir + r'''\{#MyAppName}\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

'''


# 生成配置文件
issDir = os.path.dirname(__file__)
issFilePath = os.path.join(issDir, 'InnoSetup.iss')

# 检查源文件是否存在
sourceDir = os.path.join(buildDir, appName)
if not os.path.exists(sourceDir):
    sys.exit(1)

with open(issFilePath, 'w', encoding='utf-8') as f:
    f.write(get_iss())
