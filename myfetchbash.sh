#!/bin/bash

echo "         _       **  "
echo "        | |      __  "
echo "     ___| |     |  | "
echo "    / __  |     |  | "
echo "   | (__| |    /|  | "
echo "    \_____|   / /\ | "
echo "              \ \/ / "
echo "               \__/  "
echo "                     "
echo ""
date
echo "OS:       $(lsb_release -d | awk '{print $2,$3,$4}')"
echo "Hostname: $(uname -n)"
echo "Release:  $(uname -r)"
echo "Kernel:   $(uname -v)"
echo "Platform: $(uname -p)"
echo "CPU:      $(cat /proc/cpuinfo | grep -m 1 "model name"| awk -F ':' '/model name/ {print $2}')"
echo "Disk:              "
df -h /
echo ""
echo "Adresy IPv4:"
ifconfig | grep "inet " | awk '{print $2}'
echo ""
echo "Adresy IPv6:"
ifconfig | grep "inet6 " | awk '{print $2}'

