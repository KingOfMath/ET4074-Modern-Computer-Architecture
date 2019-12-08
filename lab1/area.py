# coding=utf-8
from pattern import *
import subprocess
import os
import os.path

def read_area_value(fileName="configuration.mm"):
    A1_ALU = 3273
    A1_Mult = 40614
    A1_LWSW = 1500
    A64_GPR = 26388
    A8_BR = 258
    A_misc = 6739
    A1_Connection = 1000
    issue_width = memLoad = memStore = memPft = alu = mpy = mem = r0 = b0 = 0
    with open(fileName, 'r') as file:
        currentLine = file.readline()
        data = []
        while currentLine:
            if pattern.config_issue_width.match(currentLine):
                issue_width = int(pattern.config_issue_width.match(currentLine).group(1))
                data.append(issue_width)
            if pattern.config_memLoad.match(currentLine):
                memLoad = int(pattern.config_memLoad.match(currentLine).group(1))
                data.append(memLoad)
            if pattern.config_memStore.match(currentLine):
                memStore = int(pattern.config_memStore.match(currentLine).group(1))
                data.append(memStore)
            if pattern.config_memPft.match(currentLine):
                memPft = int(pattern.config_memPft.match(currentLine).group(1))
                data.append(memPft)
            if pattern.config_alu_0.match(currentLine):
                alu = int(pattern.config_alu_0.match(currentLine).group(1))
                data.append(alu)
            if pattern.config_mpy_0.match(currentLine):
                mpy = int(pattern.config_mpy_0.match(currentLine).group(1))
                data.append(mpy)
            if pattern.config_mem_0.match(currentLine):
                mem = int(pattern.config_mem_0.match(currentLine).group(1))
                data.append(mem)
            if pattern.config_r0.match(currentLine):
                r0 = int(pattern.config_r0.match(currentLine).group(1))
                data.append(r0)
            if pattern.config_b0.match(currentLine):
                b0 = int(pattern.config_b0.match(currentLine).group(1))
                data.append(b0)
            currentLine = file.readline()
    total = (A64_GPR / 64) * r0 * pow((issue_width/4),2) + mpy * A1_Mult + A1_LWSW * mem + alu * A1_ALU + (
            A8_BR / 8) * b0
    data.append(total)
    return data

def run(bashName):
    subprocess.call(bashName,shell=True)

def loop(total_num=10):
    total_data = []
    for i in range(1,total_num):
        os.chdir("test"+str(i))
        data = []
        data.append(read_area_value('test.mm'))
        if os.path.isfile('convolution_ta_log'):
            #data.append(read_ta_log_000_total('convolution_ta_log'))
            data.append(read_ta_log_000_exec('convolution_ta_log'))
            data.append(read_pcntl_main_IPC('convolution_pcntl.txt'))
        else:
            data.append(0)
            data.append(0)
            #data.append(0)
			
        if os.path.isfile('engine_ta_log'):
            #data.append(read_ta_log_000_total('engine_ta_log'))
            data.append(read_ta_log_000_exec('engine_ta_log'))
            data.append(read_pcntl_main_IPC('engine_pcntl.txt'))
        else:
            data.append(0)
            data.append(0)
            #data.append(0)
        
        os.chdir("..")
        total_data.append(data)
    return total_data

# TODO: visualization
def visualization():
    pass
