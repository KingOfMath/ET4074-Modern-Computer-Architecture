# coding=utf-8
import re

class pattern:
    ta_log_000_execution_time = re.compile(r"Execution Cycles:\s+(\d+)")
    ta_log_000_total_cycle = re.compile(r"Total Cycles:\s+(\d+)")
    pcntl_main_IPC = re.compile(r"\s+1\s+(\d+).(\d+)")
    config_issue_width = re.compile(r'RES: IssueWidth\s+{?(\d+)}?')
    config_memLoad = re.compile(r'RES: MemLoad\s+{?(\d+)}?')
    config_memStore = re.compile(r'RES: MemStore\s+{?(\d+)}?')
    config_memPft = re.compile(r'RES: MemPft\s+{?(\d+)}?')
    config_alu_0 = re.compile(r'RES: Alu.0\s+{?(\d+)}?')
    config_mpy_0 = re.compile(r'RES: Mpy.0\s+{?(\d+)}?')
    config_mem_0 = re.compile(r'RES: Memory.0\s+{?(\d+)}?')
    config_r0 = re.compile(r'REG: \$r0\s+{?(\d+)}?')
    config_b0 = re.compile(r'REG: \$b0\s+{?(\d+)}?')

def read_ta_log_000_exec(fileName="ta.log.000"):
    with open(fileName,'r') as file:
        currentLine = file.readline()
        while currentLine:
            if pattern.ta_log_000_execution_time.match(currentLine):
                return int(pattern.ta_log_000_execution_time.match(currentLine).group(1))
            currentLine = file.readline()

def read_ta_log_000_total(fileName="ta.log.000"):
    with open(fileName,'r') as file:
        currentLine = file.readline()
        while currentLine:
            if pattern.ta_log_000_total_cycle.match(currentLine):
                return int(pattern.ta_log_000_total_cycle.match(currentLine).group(1))
            currentLine = file.readline()

def read_pcntl_main_IPC(fileName="pcntl.txt"):
    with open(fileName,'r') as file:
        currentLine = file.readline()
        values = []
        while currentLine:
            if pattern.pcntl_main_IPC.match(currentLine):
                values.append(float(pattern.pcntl_main_IPC.match(currentLine).group(1)+
                "."+pattern.pcntl_main_IPC.match(currentLine).group(2)))
            currentLine = file.readline()
        return 0 if len(values)==0 else values[-1]









