# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_tcpdump communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from re import match

# Add your library functions here.

def tcpdump_rate(sw)

    capture = sw('cat /tmp/interface.cap'.format(**locals()),
                 shell='bash_swns')
    with open ("/tmp/interface.cap", "r") as pcap:
    capture =  pcap.read()

    packets = data.splitlines()
    total_packets = len(packets)
    last_packet = packets[len(packets)-1]
    fields = last_packet.split()
    timestamp = datetime.datetime.strptime(fields[0], '%H:%M:%S.%f').time()
    msec = (timestamp.hour *60*60 + timestamp.minute * 60 + timestamp.second) * 1000 + (timestamp.microsecond/1000)
    rate = total_packets * 1000 / msec
    return rate
 
def tcpdump_capture_interface(sw, options, interface_id, wait_time):
    cmd_output = sw('tcpdump -D'.format(**locals()),
                    shell='bash_swns')
    interface_re = (r'(?P<linux_interface>\d)\.' + interface_id +
                    r'\s[\[Up, Running\]]')
    re_result = re.search(interface_re, cmd_output)
    assert re_result
    result = re_result.groupdict()

    sw('tcpdump -ni ' + result['linux_interface'] +
        options + '-ttttt'
        '> /tmp/interface.cap 2>&1 &'.format(**locals()),
        shell='bash_swns')
    time.sleep(wait_time)
    sw('killall tcpdump'.format(**locals()),
        shell='bash_swns')
    capture = sw('cat /tmp/interface.cap'.format(**locals()),
                 shell='bash_swns')
    sw('rm /tmp/interface.cap'.format(**locals()),
       shell='bash_swns')
    return capture

__all__ = [
    'tcpdump_capture_interface'
]
