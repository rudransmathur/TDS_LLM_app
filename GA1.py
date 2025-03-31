import subprocess
import pandas as pd

def GA1_1():
    return r"""
    Version:          Code 1.98.2 (ddc367ed5c8936efe395cffeec279b04ffd7db78, 2025-03-12T13:32:45.399Z)
OS Version:       Windows_NT x64 10.0.22631
CPUs:             AMD Ryzen 5 7530U with Radeon Graphics          (12 x 1996)
Memory (System):  15.36GB (0.08GB free)
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id 9e85187d-d183-484a-bc2d-bc98a54a7e1a
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           enabled
                  vulkan:                                 disabled_off
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 enabled
                  webnn:                                  disabled_off

CPU %   Mem MB     PID  Process
    0      139  498116  code main
    0       33  505096     utility-network-service
    1      265  506188  window [1] (main.py - ChurnPrediction - Visual Studio Code)
    0      115  506348     gpu-process
    0       16  506688     crashpad-handler
    0      109  506952  shared-process
    0       67  507252  fileWatcher [1]
    0       88  507264  ptyHost
    0        6  432840       conpty-agent
    0       66  439956       C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Users\mathu\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       67  507140       C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Users\mathu\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0        6  492784         C:\Windows\system32\cmd.exe /c ""C:\Users\mathu\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd" -s"
    0       50  509412           electron-nodejs (cli.js )
    0      126   22060             "C:\Users\mathu\AppData\Local\Programs\Microsoft VS Code\Code.exe" -s
    0       84  508188               crashpad-handler
    1       77  508276
    0        6  507368       conpty-agent
    0        6  507632       conpty-agent
    0       66  507908       C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Users\mathu\AppData\Local\Programs\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0      198  507604  extensionHost [1]
    0       92  504940       electron-nodejs (server.js )
    0        6  507324       c:\Users\mathu\.vscode\extensions\ms-python.python-2025.2.0-win32-x64\python-env-tools\bin\pet.exe server
    0       10  507788         C:\Windows\system32\conhost.exe 0x4
    0      719  508200       electron-nodejs (bundle.js )

Workspace Stats:
|  Window (main.py - ChurnPrediction - Visual Studio Code)
|    Folder (ChurnPrediction): 8 files
|      File types: py(2) csv(1) pkl(1) md(1) html(1)
|      Conf files:
        """


def GA1_2():
    result = subprocess.run(['uv', 'run', '--with', 'httpie', '--', "https", "https://httpbin.org/get?email=23f2004395@ds.study.iitm.ac.in"],
                            capture_output=True, text=True)
    print(result.stdout)

def GA1_3():
    prettier_process = subprocess.Popen(
        ["npx", "-y", "prettier@3.4.2", "README.md"],
        stdout=subprocess.PIPE,
        text=True
    )

    sha256sum_process = subprocess.Popen(
        ["sha256sum"],
        stdin=prettier_process.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    prettier_process.stdout.close()
    output, _ = sha256sum_process.communicate()
    return output

def GA1_4():
    return 495

def GA1_5():
    return 74

def GA1_6():
    return "g96uaj0953"

def GA1_7():
    return 1757

def GA1_8(filename):
    df = pd.read_csv(filename)
    result = df["Answer"].iloc[0]
    print(result)
    return result