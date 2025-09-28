root@isupply-erpnext-15-stg:/etc/systemd/system# ps aux 
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.5 167748 10408 ?        Ss   Jul10   2:16 /sbin/init
root           2  0.0  0.0      0     0 ?        S    Jul10   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Jul10   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Jul10   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   Jul10   0:00 [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   Jul10   0:00 [netns]
root           8  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/0:0H-events_highpri]
root          10  0.0  0.0      0     0 ?        I<   Jul10   0:00 [mm_percpu_wq]
root          11  0.0  0.0      0     0 ?        S    Jul10   0:00 [rcu_tasks_rude_]
root          12  0.0  0.0      0     0 ?        S    Jul10   0:00 [rcu_tasks_trace]
root          13  0.0  0.0      0     0 ?        S    Jul10   0:48 [ksoftirqd/0]
root          14  0.1  0.0      0     0 ?        I    Jul10  77:36 [rcu_sched]
root          15  0.0  0.0      0     0 ?        S    Jul10   0:20 [migration/0]
root          16  0.0  0.0      0     0 ?        S    Jul10   0:00 [idle_inject/0]
root          18  0.0  0.0      0     0 ?        S    Jul10   0:00 [cpuhp/0]
root          19  0.0  0.0      0     0 ?        S    Jul10   0:00 [cpuhp/1]
root          20  0.0  0.0      0     0 ?        S    Jul10   0:00 [idle_inject/1]
root          21  0.0  0.0      0     0 ?        S    Jul10   0:20 [migration/1]
root          22  0.0  0.0      0     0 ?        S    Jul10   1:09 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/1:0H-events_highpri]
root          25  0.0  0.0      0     0 ?        S    Jul10   0:00 [kdevtmpfs]
root          26  0.0  0.0      0     0 ?        I<   Jul10   0:00 [inet_frag_wq]
root          27  0.0  0.0      0     0 ?        S    Jul10   0:00 [kauditd]
root          28  0.0  0.0      0     0 ?        S    Jul10   0:01 [khungtaskd]
root          29  0.0  0.0      0     0 ?        S    Jul10   0:00 [oom_reaper]
root          30  0.0  0.0      0     0 ?        I<   Jul10   0:00 [writeback]
root          31  0.0  0.0      0     0 ?        S    Jul10   4:19 [kcompactd0]
root          32  0.0  0.0      0     0 ?        SN   Jul10   0:00 [ksmd]
root          33  0.0  0.0      0     0 ?        SN   Jul10   0:00 [khugepaged]
root          80  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kintegrityd]
root          81  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kblockd]
root          82  0.0  0.0      0     0 ?        I<   Jul10   0:00 [blkcg_punt_bio]
root          83  0.0  0.0      0     0 ?        I<   Jul10   0:00 [tpm_dev_wq]
root          84  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ata_sff]
root          85  0.0  0.0      0     0 ?        I<   Jul10   0:00 [md]
root          86  0.0  0.0      0     0 ?        I<   Jul10   0:00 [edac-poller]
root          87  0.0  0.0      0     0 ?        I<   Jul10   0:00 [devfreq_wq]
root          88  0.0  0.0      0     0 ?        S    Jul10   0:00 [watchdogd]
root          90  0.0  0.0      0     0 ?        I<   Jul10   1:02 [kworker/0:1H-kblockd]
root          92  0.0  0.0      0     0 ?        S    Jul10   1:17 [kswapd0]
root          93  0.0  0.0      0     0 ?        S    Jul10   0:00 [ecryptfs-kthrea]
root          95  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kthrotld]
root          96  0.0  0.0      0     0 ?        I<   Jul10   0:00 [acpi_thermal_pm]
root          98  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_0]
root          99  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_0]
root         100  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_1]
root         101  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_1]
root         103  0.0  0.0      0     0 ?        I<   Jul10   0:00 [vfio-irqfd-clea]
root         104  0.0  0.0      0     0 ?        I<   Jul10   0:00 [mld]
root         105  0.0  0.0      0     0 ?        I<   Jul10   1:06 [kworker/1:1H-kblockd]
root         106  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ipv6_addrconf]
root         115  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kstrp]
root         118  0.0  0.0      0     0 ?        I<   Jul10   0:00 [zswap-shrink]
root         119  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/u5:0]
root         124  0.0  0.0      0     0 ?        I<   Jul10   0:00 [charger_manager]
root         164  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_2]
root         165  0.0  0.0      0     0 ?        I<   Jul10   0:00 [cryptd]
root         167  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_2]
root         240  0.0  0.0      0     0 ?        I<   Jul10   0:00 [raid5wq]
root         288  0.0  0.0      0     0 ?        S    Jul10   1:27 [jbd2/vda1-8]
root         289  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ext4-rsv-conver]
root         361  0.0  1.5  89220 31164 ?        S<s  Jul10   3:50 /lib/systemd/systemd-journald
root         388  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kaluad]
root         390  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpath_rdacd]
root         392  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpathd]
root         393  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpath_handlerd]
root         394  0.0  1.3 289316 27100 ?        SLsl Jul10   7:46 /sbin/multipathd -d -s
systemd+     504  0.0  0.1  89388  3460 ?        Ssl  Jul10   0:06 /lib/systemd/systemd-timesyncd
systemd+     624  0.0  0.2  16128  4180 ?        Ss   Jul10   0:17 /lib/systemd/systemd-networkd
systemd+     626  0.0  0.4  26596  8992 ?        Ss   Jul10   0:13 /lib/systemd/systemd-resolved
root         669  0.0  0.2  11552  4548 ?        Ss   Jul10   0:05 /lib/systemd/systemd-udevd
avahi        722  0.0  0.1   7720  2764 ?        Ss   Jul10   0:00 avahi-daemon: running [isupply-erpnext-15-stg.local]
message+     723  0.0  0.2   8884  4172 ?        Ss   Jul10   0:05 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         728  0.0  0.1  82800  3004 ?        Ssl  Jul10   3:00 /usr/sbin/irqbalance --foreground
root         729  0.0  0.6  33176 12396 ?        Ss   Jul10   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         730  0.0  0.1 234512  2728 ?        Ssl  Jul10   0:00 /usr/libexec/polkitd --no-debug
root         734  0.0  0.2  15512  4684 ?        Ss   Jul10   0:07 /lib/systemd/systemd-logind
root         737  0.0  0.1  16504  3160 ?        Ss   Jul10   0:25 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
avahi        738  0.0  0.0   7444   336 ?        S    Jul10   0:00 avahi-daemon: chroot helper
root         760  0.0  0.1   7288  2424 ?        Ss   Jul10   0:08 /usr/sbin/cron -f -P
redis        761  0.1  0.3  69804  6244 ?        Ssl  Jul10 125:47 /usr/bin/redis-server 127.0.0.1:6379
root         765  0.0  1.0  37412 20396 ?        Ss   Jul10  24:10 /usr/bin/python3 /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
root         778  0.0  0.2 317880  5348 ?        Ssl  Jul10   0:00 /usr/sbin/ModemManager
root         788  0.0  0.0   6220   792 ttyS0    Ss+  Jul10   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,57600,38400,9600 ttyS0 vt220
root         793  0.0  0.0   6176   860 tty1     Ss+  Jul10   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         798  0.0  0.0  18416  1912 ?        Ss   Jul10   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data     799  0.0  0.4  24344  8848 ?        S    Jul10   0:08 nginx: worker process
www-data     800  0.0  0.5  26624 11520 ?        S    Jul10  19:51 nginx: worker process
www-data     801  0.0  0.0  19016  1988 ?        S    Jul10   0:27 nginx: cache manager process
root         816  0.0  0.2  15440  5596 ?        Ss   Jul10   3:47 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         878  0.0  0.5 110140 11844 ?        Ssl  Jul10   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql        897  0.2 19.8 1625544 398220 ?      Ssl  Jul10 180:52 /usr/sbin/mariadbd
frappe       948  0.0  2.2 795916 46084 ?        Sl   Jul10   0:57 /usr/local/bin/node /home/frappe/frappe-bench/apps/frappe/socketio.js
frappe       949  0.2  0.8  85676 16456 ?        Sl   Jul10 149:18 /usr/bin/redis-server 127.0.0.1:13000
frappe       950  0.1  0.3  79020  6416 ?        Sl   Jul10 138:06 /usr/bin/redis-server 127.0.0.1:11000
root        1260  0.0  0.0      0     0 ?        I<   Jul10   0:00 [dio/vda1]
root        7549  0.0  0.2 296012  5180 ?        Ssl  Jul10   0:30 /usr/libexec/packagekitd
frappe     98846  0.0  3.2 104260 65200 ?        S    Jul17  12:14 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe     98855  0.0  3.0 100476 61744 ?        SN   Jul17  45:28 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe schedule
frappe     98856  0.0  1.9 140340 39416 ?        SNl  Jul17  51:25 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe worker --queue short,default
frappe     98857  0.0  1.9 140324 39488 ?        SNl  Jul17  51:26 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe worker --queue long,default,short
root      223582  0.0  0.2 1232960 5424 ?        Ssl  Jul24   0:15 /opt/digitalocean/bin/droplet-agent
do-agent  234090  0.0  0.5 1238596 10896 ?       Ssl  Jul25  11:37 /opt/digitalocean/bin/do-agent --syslog
syslog    339398  0.0  0.2 222404  4748 ?        Ssl  Jul30   0:27 /usr/sbin/rsyslogd -n -iNONE
frappe    828096  0.0  5.5 151052 111384 ?       S    Aug22   8:00 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    828196  0.0  5.4 146308 109340 ?       S    Aug22   5:13 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
root      835232  0.0  1.1 1997228 22288 ?       Ssl  Aug23   0:36 /usr/lib/snapd/snapd
frappe    849222  0.0  5.3 144592 106640 ?       S    Aug24   2:50 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    849223  0.0  5.4 143724 109120 ?       S    Aug24   2:35 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    852892  0.0  5.0 137788 102532 ?       S    Aug24   1:29 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
root      911993  0.0  0.0      0     0 ?        I    06:43   0:06 [kworker/1:0-events]
root      914346  0.0  0.0      0     0 ?        I    10:23   0:03 [kworker/0:1-events]
root      914472  0.0  0.0      0     0 ?        I    10:23   0:00 [kworker/u4:3-events_unbound]
root      914531  0.0  0.0      0     0 ?        I    10:30   0:00 [kworker/u4:0-flush-252:0]
root      914883  0.0  0.0      0     0 ?        I    11:14   0:00 [kworker/u4:1-events_unbound]
root      915327  0.0  0.0      0     0 ?        I    11:26   0:00 [kworker/0:3-events]
root      915941  0.0  0.5  17456 11540 ?        Ss   11:31   0:00 sshd: root@pts/0
root      915946  0.0  0.4  17100  9436 ?        Ss   11:31   0:00 /lib/systemd/systemd --user
root      915947  0.0  0.2 170660  5128 ?        S    11:31   0:00 (sd-pam)
root      915948  0.0  0.0      0     0 ?        I    11:31   0:00 [kworker/1:1-events]
root      916032  0.0  0.4  12980  9100 pts/0    Ss   11:31   0:00 -bash
root      916421  0.0  0.1  10464  3252 pts/0    R+   11:46   0:00 ps aux
root@isupply-erpnext-15-stg:/etc/systemd/system# root@isupply-erpnext-15-stg:/etc/systemd/system# ps aux 
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.5 167748 10408 ?        Ss   Jul10   2:16 /sbin/init
root           2  0.0  0.0      0     0 ?        S    Jul10   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Jul10   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Jul10   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   Jul10   0:00 [slub_flushwq]
root           6  0.0  0.0      0     0 ?        I<   Jul10   0:00 [netns]
root           8  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/0:0H-events_highpri]
root          10  0.0  0.0      0     0 ?        I<   Jul10   0:00 [mm_percpu_wq]
root          11  0.0  0.0      0     0 ?        S    Jul10   0:00 [rcu_tasks_rude_]
root          12  0.0  0.0      0     0 ?        S    Jul10   0:00 [rcu_tasks_trace]
root          13  0.0  0.0      0     0 ?        S    Jul10   0:48 [ksoftirqd/0]
root          14  0.1  0.0      0     0 ?        I    Jul10  77:36 [rcu_sched]
root          15  0.0  0.0      0     0 ?        S    Jul10   0:20 [migration/0]
root          16  0.0  0.0      0     0 ?        S    Jul10   0:00 [idle_inject/0]
root          18  0.0  0.0      0     0 ?        S    Jul10   0:00 [cpuhp/0]
root          19  0.0  0.0      0     0 ?        S    Jul10   0:00 [cpuhp/1]
root          20  0.0  0.0      0     0 ?        S    Jul10   0:00 [idle_inject/1]
root          21  0.0  0.0      0     0 ?        S    Jul10   0:20 [migration/1]
root          22  0.0  0.0      0     0 ?        S    Jul10   1:09 [ksoftirqd/1]
root          24  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/1:0H-events_highpri]
root          25  0.0  0.0      0     0 ?        S    Jul10   0:00 [kdevtmpfs]
root          26  0.0  0.0      0     0 ?        I<   Jul10   0:00 [inet_frag_wq]
root          27  0.0  0.0      0     0 ?        S    Jul10   0:00 [kauditd]
root          28  0.0  0.0      0     0 ?        S    Jul10   0:01 [khungtaskd]
root          29  0.0  0.0      0     0 ?        S    Jul10   0:00 [oom_reaper]
root          30  0.0  0.0      0     0 ?        I<   Jul10   0:00 [writeback]
root          31  0.0  0.0      0     0 ?        S    Jul10   4:19 [kcompactd0]
root          32  0.0  0.0      0     0 ?        SN   Jul10   0:00 [ksmd]
root          33  0.0  0.0      0     0 ?        SN   Jul10   0:00 [khugepaged]
root          80  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kintegrityd]
root          81  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kblockd]
root          82  0.0  0.0      0     0 ?        I<   Jul10   0:00 [blkcg_punt_bio]
root          83  0.0  0.0      0     0 ?        I<   Jul10   0:00 [tpm_dev_wq]
root          84  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ata_sff]
root          85  0.0  0.0      0     0 ?        I<   Jul10   0:00 [md]
root          86  0.0  0.0      0     0 ?        I<   Jul10   0:00 [edac-poller]
root          87  0.0  0.0      0     0 ?        I<   Jul10   0:00 [devfreq_wq]
root          88  0.0  0.0      0     0 ?        S    Jul10   0:00 [watchdogd]
root          90  0.0  0.0      0     0 ?        I<   Jul10   1:02 [kworker/0:1H-kblockd]
root          92  0.0  0.0      0     0 ?        S    Jul10   1:17 [kswapd0]
root          93  0.0  0.0      0     0 ?        S    Jul10   0:00 [ecryptfs-kthrea]
root          95  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kthrotld]
root          96  0.0  0.0      0     0 ?        I<   Jul10   0:00 [acpi_thermal_pm]
root          98  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_0]
root          99  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_0]
root         100  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_1]
root         101  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_1]
root         103  0.0  0.0      0     0 ?        I<   Jul10   0:00 [vfio-irqfd-clea]
root         104  0.0  0.0      0     0 ?        I<   Jul10   0:00 [mld]
root         105  0.0  0.0      0     0 ?        I<   Jul10   1:06 [kworker/1:1H-kblockd]
root         106  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ipv6_addrconf]
root         115  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kstrp]
root         118  0.0  0.0      0     0 ?        I<   Jul10   0:00 [zswap-shrink]
root         119  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kworker/u5:0]
root         124  0.0  0.0      0     0 ?        I<   Jul10   0:00 [charger_manager]
root         164  0.0  0.0      0     0 ?        S    Jul10   0:00 [scsi_eh_2]
root         165  0.0  0.0      0     0 ?        I<   Jul10   0:00 [cryptd]
root         167  0.0  0.0      0     0 ?        I<   Jul10   0:00 [scsi_tmf_2]
root         240  0.0  0.0      0     0 ?        I<   Jul10   0:00 [raid5wq]
root         288  0.0  0.0      0     0 ?        S    Jul10   1:27 [jbd2/vda1-8]
root         289  0.0  0.0      0     0 ?        I<   Jul10   0:00 [ext4-rsv-conver]
root         361  0.0  1.5  89220 31164 ?        S<s  Jul10   3:50 /lib/systemd/systemd-journald
root         388  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kaluad]
root         390  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpath_rdacd]
root         392  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpathd]
root         393  0.0  0.0      0     0 ?        I<   Jul10   0:00 [kmpath_handlerd]
root         394  0.0  1.3 289316 27100 ?        SLsl Jul10   7:46 /sbin/multipathd -d -s
systemd+     504  0.0  0.1  89388  3460 ?        Ssl  Jul10   0:06 /lib/systemd/systemd-timesyncd
systemd+     624  0.0  0.2  16128  4180 ?        Ss   Jul10   0:17 /lib/systemd/systemd-networkd
systemd+     626  0.0  0.4  26596  8992 ?        Ss   Jul10   0:13 /lib/systemd/systemd-resolved
root         669  0.0  0.2  11552  4548 ?        Ss   Jul10   0:05 /lib/systemd/systemd-udevd
avahi        722  0.0  0.1   7720  2764 ?        Ss   Jul10   0:00 avahi-daemon: running [isupply-erpnext-15-stg.local]
message+     723  0.0  0.2   8884  4172 ?        Ss   Jul10   0:05 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         728  0.0  0.1  82800  3004 ?        Ssl  Jul10   3:00 /usr/sbin/irqbalance --foreground
root         729  0.0  0.6  33176 12396 ?        Ss   Jul10   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         730  0.0  0.1 234512  2728 ?        Ssl  Jul10   0:00 /usr/libexec/polkitd --no-debug
root         734  0.0  0.2  15512  4684 ?        Ss   Jul10   0:07 /lib/systemd/systemd-logind
root         737  0.0  0.1  16504  3160 ?        Ss   Jul10   0:25 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
avahi        738  0.0  0.0   7444   336 ?        S    Jul10   0:00 avahi-daemon: chroot helper
root         760  0.0  0.1   7288  2424 ?        Ss   Jul10   0:08 /usr/sbin/cron -f -P
redis        761  0.1  0.3  69804  6244 ?        Ssl  Jul10 125:47 /usr/bin/redis-server 127.0.0.1:6379
root         765  0.0  1.0  37412 20396 ?        Ss   Jul10  24:10 /usr/bin/python3 /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
root         778  0.0  0.2 317880  5348 ?        Ssl  Jul10   0:00 /usr/sbin/ModemManager
root         788  0.0  0.0   6220   792 ttyS0    Ss+  Jul10   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,57600,38400,9600 ttyS0 vt220
root         793  0.0  0.0   6176   860 tty1     Ss+  Jul10   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         798  0.0  0.0  18416  1912 ?        Ss   Jul10   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data     799  0.0  0.4  24344  8848 ?        S    Jul10   0:08 nginx: worker process
www-data     800  0.0  0.5  26624 11520 ?        S    Jul10  19:51 nginx: worker process
www-data     801  0.0  0.0  19016  1988 ?        S    Jul10   0:27 nginx: cache manager process
root         816  0.0  0.2  15440  5596 ?        Ss   Jul10   3:47 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         878  0.0  0.5 110140 11844 ?        Ssl  Jul10   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql        897  0.2 19.8 1625544 398220 ?      Ssl  Jul10 180:52 /usr/sbin/mariadbd
frappe       948  0.0  2.2 795916 46084 ?        Sl   Jul10   0:57 /usr/local/bin/node /home/frappe/frappe-bench/apps/frappe/socketio.js
frappe       949  0.2  0.8  85676 16456 ?        Sl   Jul10 149:18 /usr/bin/redis-server 127.0.0.1:13000
frappe       950  0.1  0.3  79020  6416 ?        Sl   Jul10 138:06 /usr/bin/redis-server 127.0.0.1:11000
root        1260  0.0  0.0      0     0 ?        I<   Jul10   0:00 [dio/vda1]
root        7549  0.0  0.2 296012  5180 ?        Ssl  Jul10   0:30 /usr/libexec/packagekitd
frappe     98846  0.0  3.2 104260 65200 ?        S    Jul17  12:14 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe     98855  0.0  3.0 100476 61744 ?        SN   Jul17  45:28 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe schedule
frappe     98856  0.0  1.9 140340 39416 ?        SNl  Jul17  51:25 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe worker --queue short,default
frappe     98857  0.0  1.9 140324 39488 ?        SNl  Jul17  51:26 /home/frappe/frappe-bench/env/bin/python -m frappe.utils.bench_helper frappe worker --queue long,default,short
root      223582  0.0  0.2 1232960 5424 ?        Ssl  Jul24   0:15 /opt/digitalocean/bin/droplet-agent
do-agent  234090  0.0  0.5 1238596 10896 ?       Ssl  Jul25  11:37 /opt/digitalocean/bin/do-agent --syslog
syslog    339398  0.0  0.2 222404  4748 ?        Ssl  Jul30   0:27 /usr/sbin/rsyslogd -n -iNONE
frappe    828096  0.0  5.5 151052 111384 ?       S    Aug22   8:00 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    828196  0.0  5.4 146308 109340 ?       S    Aug22   5:13 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
root      835232  0.0  1.1 1997228 22288 ?       Ssl  Aug23   0:36 /usr/lib/snapd/snapd
frappe    849222  0.0  5.3 144592 106640 ?       S    Aug24   2:50 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    849223  0.0  5.4 143724 109120 ?       S    Aug24   2:35 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
frappe    852892  0.0  5.0 137788 102532 ?       S    Aug24   1:29 /home/frappe/frappe-bench/env/bin/python /home/frappe/frappe-bench/env/bin/gunicorn -b 127.0.0.1:8000 -w 5 --max-requests 5000 --max-requ
root      911993  0.0  0.0      0     0 ?        I    06:43   0:06 [kworker/1:0-events]
root      914346  0.0  0.0      0     0 ?        I    10:23   0:03 [kworker/0:1-events]
root      914472  0.0  0.0      0     0 ?        I    10:23   0:00 [kworker/u4:3-events_unbound]
root      914531  0.0  0.0      0     0 ?        I    10:30   0:00 [kworker/u4:0-flush-252:0]
root      914883  0.0  0.0      0     0 ?        I    11:14   0:00 [kworker/u4:1-events_unbound]
root      915327  0.0  0.0      0     0 ?        I    11:26   0:00 [kworker/0:3-events]
root      915941  0.0  0.5  17456 11540 ?        Ss   11:31   0:00 sshd: root@pts/0
root      915946  0.0  0.4  17100  9436 ?        Ss   11:31   0:00 /lib/systemd/systemd --user
root      915947  0.0  0.2 170660  5128 ?        S    11:31   0:00 (sd-pam)
root      915948  0.0  0.0      0     0 ?        I    11:31   0:00 [kworker/1:1-events]
root      916032  0.0  0.4  12980  9100 pts/0    Ss   11:31   0:00 -bash
root      916421  0.0  0.1  10464  3252 pts/0    R+   11:46   0:00 ps aux
root@isupply-erpnext-15-stg:/etc/systemd/system# 
